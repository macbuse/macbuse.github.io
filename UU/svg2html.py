#! /home/gregmcshane/anaconda3/bin/python3.6 
'''
embed an svg file in html
with css animation
'''

import re, sys,  argparse
from svgpathtools import svg2paths

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <style>
  body {{
  background-color: #ffffff;
    }}
  {}
  </style>
    
</head>
<body>
{}
</body>
  '''

ANIM_PARAMS = ''' 
#{} {{ stroke-dasharray:  {};
      stroke-dashoffset: {};
      opacity : 0;
      animation: offset {:.2f}s linear forwards;
      animation-delay: {:.2f}s;
      animation-iteration-count: 1;
    }} '''

ANIM_LOOP = '''
@keyframes offset {
    to {
    stroke-dashoffset: 0;  opacity: 1;
    }
'''

PP_PATH = re.compile('<path(.*?)\sd=', re.DOTALL)
PP_METADATA = re.compile('<metadata>.*?</metadata>',re.DOTALL)
#PP_LAYER = re.compile('<g.*?layerName="f.*?">.*?</g>',re.DOTALL)
PP_LAYER = re.compile('(<g.*?)Name="(.*?)">(.*?)</g>',re.DOTALL)
PP_UNITS = re.compile('(\d+)pt')

def units_cb(mm):
    return '%spx'%mm.group(1)

def mk_anim(src_fn, 
            speed=1.,
            top_first=False):
    
    def path_cb(mm):
        return '<path id="%s" %s d='%(path_ids.pop(0), mm.group(1))

    def layer_cb(mm):
        head, name, payload = mm.groups()
        layer_text =  '%s="">%s</g>'%(head,payload)
        if 'fix' in name:
            fixed_layers.append(layer_text)
            return '#'*10 + '\n'
        return layer_text

    def paste_cb(mm):
        return fixed_layers.pop(0)

    with open(src_fn, 'r') as FP:
        data = FP.read()
    
    #ditch the metadata - there's a thumbnail :(
    data = re.sub(PP_METADATA, '', data)
    data = re.sub(PP_UNITS, units_cb, data)
    fixed_layers = []
    data = re.sub(PP_LAYER, layer_cb, data)

    with open('tmp.svg','w') as FP:
        FP.write(data)

    paths, attributes = svg2paths('tmp.svg')
    lengths = [int(x.length()) for x in paths]
    path_ids = ['p%d'%k for k, x in enumerate(paths)]
    # give the paths unique ids
    svg = re.sub(PP_PATH, path_cb, data)
    #paste the fixed layers back in
    PP_X = re.compile('#'*10)
    svg = re.sub(PP_X, paste_cb, svg)

    from  itertools import accumulate
    rolling = list(accumulate(lengths) )
    if top_first:
        rolling = [rolling[-1] - x for x in rolling]

    animations = [ ANIM_PARAMS.format('p%d'%k,
                                     length,
                                     length,
                                     length/500/speed, #duration in secs
                                     delay/500/speed  #delay in secs
                                     ) 
         for k,length,delay in zip(range(len(lengths)), lengths, rolling)  ]

    animations.append(ANIM_LOOP)
    style = ' '.join(animations)

    with open('%s.html'%src_fn.split('.')[0], 'w') as FP:
        FP.write(HTML.format(style, svg))

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("FN")
    PARSER.add_argument("-s", dest='speed', default=1.0)
    PARSER.add_argument("-r", dest='reversed', action='store_true', default=False)
    ARGS = PARSER.parse_args()

    if len(sys.argv) < 2:
        print('usage: %s file.svg'%sys.argv[0])
        sys.exit(1)

    mk_anim(ARGS.FN, speed=float(ARGS.speed), top_first=ARGS.reversed)
