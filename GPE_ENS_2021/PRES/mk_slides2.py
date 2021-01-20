#! /usr/bin/python3.6
'''whatever'''

import os, re, time, sys
import subprocess

import json #serialise
import requests
from gtts import gTTS

class Voices():
    '''vv'''
    voices = {'K' : 'en-GB_KateV3Voice',
              'M' : 'en-US_MichaelV3Voice',
              'KK' : 'en-US_KevinV3Voice',
              'LI' : 'zh-CNLiNaVoice',
              'O' : 'en-US_OliviaV3Voice',
              'R' : 'fr-FR_ReneeV3Voice'
             }
    
    def __init__(self):
        if not os.path.isfile('script.json'):
            self.inventory = {}
        else:
            self.inventory = json.load(open('script.json', 'r'))

    def string2fn(self, xx):
        '''ff'''
        '''hash function
        strip punctuation
        return first 3 words with sep=_'''

        words = re.sub(r'[^\w\s]', '', xx).lower().split() #strip punctuation - > lowercase
        #check and pad
        if len(words) < 3:
            words.extend(['blah']*3)
        return '_'.join(words[:3]) + '.mp3'

    def get_audio(self, to_say):

        actor, txt = to_say
        FN = self.string2fn(txt)
        print('Doing', FN)
        
        if actor in self.voices:
            url = 'https://text-to-speech-demo.ng.bluemix.net/api/v3/synthesize'
            params = {'text' : txt,
                      'voice' : self.voices[actor],
                      'download' : 'true',
                      'accept' : 'audio/mp3'
            }
         
            r = requests.get(url, params=params)

            with open('%s'%FN, 'wb') as FP:
                FP.write(r.content)

        else: #assume it's a language tag and ask google
            tts = gTTS(txt, lang=actor.lower())
            tts.save(FN)

    def add(self, txts):

        for tt in txts:
            actor, lines = tt
            FN = self.string2fn(lines)
            key = actor + FN
            if key in self.inventory and self.inventory[key] == lines:
                print('skipping', FN)
                continue
            self.get_audio(tt)
            time.sleep(20)

        with open('script.json', 'w') as FP:
            json.dump({actor + self.string2fn(lines) : lines for  actor,lines  in txts}, FP)
        print('DONE')
        
    def __repr__(self):
        return str('\n'.join(self.inventory.keys()))
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: mk_slides.py file.md')
        sys.exit(1)
    FN = sys.argv[1]

    with open(FN, 'r') as FP:
        md = FP.read()
    voices = Voices()
    print(voices)
    string2fn = voices.string2fn #delegate this
    
    #I have special tags for speach and changing font size in math
    #!![voice key](text) for speech 
    # voices key is one of M, K, O
    #percentage$...$ for resizing TeX fonts
    PP_MEDIA = re.compile(r'!!\[(.*?)\]\((.*?)\)', re.DOTALL)
    PP_MATH = re.compile(r'(\d+)(\$.*?\$)', re.DOTALL)
    PP_IMG = re.compile(r'(\d+)!\[(.*?)\]\((.*?)\)', re.DOTALL)

    #global
    spoken_text = []
    
    def media_cb(match):
        wrap = '<div class="wrap">%s</div>\n\n'
        src = match.group(2)
        print("<< ", src)
        #this is typically a youtube video
        if 'http' in src:
            wrapper = wrap%'''<iframe src="{}" allowfullscreen="true"> </iframe>'''
            return wrapper.format(src)

        #local html file - this is loaded lazily, so animations start on view
        if 'html' in src:
            wrapper = wrap%'''<iframe data-src="{}" > </iframe>'''
            return wrapper.format(src)

        if 'mp4' in src:
            wrapper = wrap%'''<video src="{}" data-autoplay> </video>'''
            return wrapper.format(src)

        if 'mp3' in src:
            wrapper = '''<audio src="{}" data-autoplay> </audio>'''
            return wrapper.format(src)

        # default is audio
        spoken_text.append(match.groups())
        wrapper = '<audio  data-autoplay ><source src="{}" ></audio>'
        return wrapper.format(string2fn(src))
    
    def math_cb(match):
        wrapper = '<span style="font-size: {}%">{}</span>'
        return wrapper.format(match.group(1), match.group(2))
    
    def img_cb(match):
        wrapper = '<img src="{}" alt="{}" width="{}" >'
        return wrapper.format(match.group(3), match.group(2), match.group(1))
   
    print('>>', PP_IMG.findall(md))
    #make the html first as it is local
    xx = re.sub(PP_MEDIA , media_cb, md)
    xx = re.sub(PP_IMG, img_cb, xx)
    md_with_tags = re.sub(PP_MATH, math_cb, xx)

    with open('tmp.md', 'w') as fp:
        fp.write(md_with_tags)
        
    #split this (past col 80) so that we can replace for -o later if we want
    pandoc_it = 'pandoc -t revealjs -c mycss.css -s -o slides.html tmp.md'.split()
    pandoc_it.extend('-V revealjs-url=https://unpkg.com/reveal.js@3.9.2/ --mathjax -i'.split())
    print(' '.join(pandoc_it))
    subprocess.call(pandoc_it)

    #this has a lot of latency
    print(spoken_text)

    if spoken_text != []:
        voices.add(spoken_text)
