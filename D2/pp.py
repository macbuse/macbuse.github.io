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

ANIM_PARAMS_NOFILL = ''' 
#{} {{ stroke-dasharray:  {};
      stroke-dashoffset: {};
      opacity : 0.5;
      animation: offset {:.2f}s linear forwards;
      animation-delay: {:.2f}s;
      animation-iteration-count: 1;
    }} '''

ANIM_PARAMS_FILL = ''' 
#{} {{ stroke-dasharray:  {};
      stroke-dashoffset: {};
      opacity : 0.0;
      animation: alpha {:.2f}s linear forwards;
      animation-delay: {:.2f}s;
      animation-iteration-count: 1;
    }} '''

ANIM_OFF = '''
@keyframes offset {
    to {
    stroke-dashoffset: 0; opacity: 1;
    }
'''

ANIM_ALPHA = '''
@keyframes alpha {
    to {
    opacity: 1;
    }
'''
ANIM_ALPHA = ''
PP_PATH = re.compile('<path(.*?)\sd=', re.DOTALL)
PP_METADATA = re.compile('<metadata>.*?</metadata>',re.DOTALL)
PP_UNITS = re.compile('(\d+)pt')

ANIM = []

def units_cb(mm):
    return '%spx'%mm.group(1)

def mk_anim(src_fn, 
            speed=1.,
            top_first=False):
    
    def path_cb(mm):
        if 'baba' in mm.group(1):
            ANIM.append(ANIM_PARAMS_FILL)
        else:
            ANIM.append(ANIM_PARAMS_NOFILL)
        return '<path id="%s" %s d='%(path_ids.pop(0), mm.group(1))

    with open(src_fn, 'r') as FP:
        data = FP.read()

    #ditch the metadata - there's a thumbnail :(
    data = re.sub(PP_METADATA, '', data)

    paths, attributes = svg2paths(src_fn)
    path_ids = ['p%d'%k for k, x in enumerate(paths)]
    #path_ids_cp = path_ids[:] #make a copy for debugging

    data = re.sub(PP_UNITS, units_cb, data)
    svg = re.sub(PP_PATH, path_cb, data)

    paths, attributes = svg2paths(src_fn)

    lengths = [int(x.length()) for x in paths]

    rolling = [0]
    for cv_len in lengths:
        rolling.append(rolling[-1] + cv_len)
    if top_first:
        rolling = [rolling[-1] - x for x in rolling]

    animations = [ANIM.pop(0).format('p%d'%k,
                                     length,
                                     length,
                                     length/500/speed, #duration in secs
                                     delay/500/speed  #delay in secs
                                     )
         for k,length,delay in zip(range(len(lengths)), lengths, rolling)  ]

    animations.extend([ANIM_ALPHA, ANIM_OFF])
    style = ' '.join(animations)

    print(style[-300:])

    with open('%s.html'%src_fn.split('.')[0], 'w') as FP:
        FP.write(HTML.format(style, svg))

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("FN")
    PARSER.add_argument("-s", dest='speed', default=1.0)
    PARSER.add_argument("-r", dest='r', action='store_true', default=False)
    ARGS = PARSER.parse_args()

    if len(sys.argv) < 2:
        print('usage: %s file.svg'%sys.argv[0])
        sys.exit(1)

    mk_anim(ARGS.FN, speed=float(ARGS.speed), top_first=ARGS.r)
