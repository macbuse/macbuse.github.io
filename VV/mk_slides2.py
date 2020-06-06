#! /home/gregmcshane/anaconda3/bin/python3.6 

from gtts import gTTS
import requests
import subprocess

import os, re, time
import json #serialise

class Voices():
    voices ={'K' : 'en-GB_KateV3Voice',
         'M' : 'en-US_MichaelV3Voice',
         'O' : 'en-US_OliviaV3Voice',
          'R' : 'fr-FR_ReneeV3Voice'
        }
    
    def __init__(self):
        if not os.path.isfile('script.json'):
            self.inventory = {}
        else:
            self.inventory = json.load(open('script.json','r'))
             
    def string2fn(self, xx):
        '''hash function
        strip punctuation
         return first 3 words with sep=_'''
        #strip punctuation - > lowercase
        u = re.sub(r'[^\w\s]','', xx).lower().split()
        #check and pad
        if len(u) < 3:
            u.extend(['blah']*3)
        return '_'.join(u[:3]) + '.mp3'

    def get_audio(self,to_say):

        actor, txt = to_say
        fn = self.string2fn(txt)
        print('Doing', fn)
        
        if actor in self.voices:
            url = 'https://text-to-speech-demo.ng.bluemix.net/api/v3/synthesize'
            params = {'text' : txt,
            'voice' : self.voices[actor],
            'download' : 'true',
            'accept' : 'audio/mp3'
            }

            r = requests.get(url, params=params)

            with open('%s'%fn,'wb') as fp:
                fp.write(r.content)

        else: #assume it's a language tag and ask google
            tts = gTTS(txt, lang=actor.lower())
            tts.save(fn)

    def add(self, txts):

        for tt in txts:
            actor, lines = tt
            fn = self.string2fn(lines)

            if fn in self.inventory and self.inventory[fn] == lines:
                print('skipping', fn)
                continue
            self.get_audio(tt)
            time.sleep(20)

        with open('script.json','w') as fp:
            actor, lines = list( zip(* txts))
            json.dump( { self.string2fn(x) : x for x in lines} , fp)
    
        print('DONE')
        
    def __repr__(self):
        return str('\n'.join(self.inventory.keys()))
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('usage: mk_slides.py file.md')
        sys.exit(1)
    fn = sys.argv[1]

    with open(fn,'r') as fp:
        md = fp.read()
        
    voices = Voices()
    print(voices)
    string2fn = voices.string2fn #delegate this
    
    #I have special tags for speach and changing font size in math
    #!![voice key](text) for speech 
    # voices key is one of M, K, O
    #percentage$...$ for resizing TeX fonts
    pp_media  = re.compile(r'!!\[(.*?)\]\((.*?)\)',re.DOTALL)
    pp_math =  re.compile(r'(\d+)(\$.*?\$)',re.DOTALL)
    pp_img =  re.compile(r'(\d+)!\[(.*?)\]\((.*?)\)',re.DOTALL)

    #global
    spoken_text = []
    
    def media_cb(match):
        src = match.group(2)
        print("<< ", src)
        if 'http' in src :
            wrapper = '''<div class="wrap"><iframe src="{}" allowfullscreen="true"> </iframe></wrap>\n\n'''
            return wrapper.format( src)

        #local html file
        if 'html' in src :
            wrapper = '''<div class="wrap"><iframe src="{}" > </iframe></wrap>\n\n'''
            return wrapper.format( src)

        if 'mp4' in src:
            wrapper = '''<div class="wrap"><video src="{}" data-autoplay> </video></wrap>\n\n'''
            return wrapper.format( src)

        # default is audio
        spoken_text.append(match.groups())
        wrapper = '<audio  data-autoplay ><source src="{}" ></audio>'
        return wrapper.format(string2fn(src) )
    
    def math_cb(match):
        wrapper = '<div style="font-size: {}%">{}</div>'
        return wrapper.format(match.group(1), match.group(2))
    
    def img_cb(match):
        wrapper = '<img src="{}" alt="{}" width="{}" >'
        return wrapper.format(match.group(3), match.group(2), match.group(1))
   
   
    print('>>', pp_img.findall(md))
    #make the html first as it is local
    xx = re.sub(pp_media , media_cb, md)
    xx = re.sub(pp_img, img_cb, xx)
    md_with_tags = re.sub(pp_math, math_cb, xx)

    with open('tmp.md','w') as fp:
        fp.write(md_with_tags)
        
    #split this (past col 80) so that we can replace for -o later if we want
    pandoc_it = 'pandoc -t revealjs -c mycss.css -s -o slides.html tmp.md'.split()
    pandoc_it.extend('-V revealjs-url=https://unpkg.com/reveal.js@3.9.2/ --mathjax -i'.split())

    subprocess.call(pandoc_it)
    
    #this has a lot of latency
    print(spoken_text)

    if spoken_text != []:
        voices.add(spoken_text)
