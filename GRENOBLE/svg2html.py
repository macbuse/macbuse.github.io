#!  /home/macbuse/anaconda3/bin/python3.9
import re, sys
from svgpathtools import svg2paths

html = '''<!DOCTYPE html>
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

anim_params = '''    
#{} {{ stroke-dasharray:  {};
      stroke-dashoffset: {};
      animation: offset {:.2f}s linear forwards;
      animation-delay: {:.2f}s;
      animation-iteration-count: 1;
    }} '''

anim_loop = '''
@keyframes offset {
    to {
    stroke-dashoffset: 0;
    }
'''
   

pp_path = re.compile('<path(.*?)\sd=', re.DOTALL)
pp_metadata = re.compile('<metadata>.*?</metadata>',re.DOTALL)
pp_units = re.compile('(\d+)pt')

def units_cb(mm):
    return '%spx'%mm.group(1)


def mk_anim(src_fn):
    
    def path_cb(mm):
        return '<path id="%s" %s d='%(path_ids.pop(0), mm.group(1))

    with open(src_fn, 'r') as fp:
        data = fp.read()
    
    #ditch the metadata - there's a thumbnail :(
    data = re.sub(pp_metadata, '', data)

    paths, attributes = svg2paths(src_fn)
    path_ids = ['p%d'%k for k, _ in enumerate(paths) ]

    data = re.sub(pp_units, units_cb, data)
    svg = re.sub(pp_path, path_cb, data)

    paths, attributes = svg2paths(src_fn)

    lengths = [ int(x.length()) for x in paths]

    rolling = [0]
    for l in lengths:
        rolling.append(rolling[-1] + l)

    animations = [ anim_params.format('p%d'%k,l,l,l/500, d/500) 
                                  for k,l,d in zip(range(len(lengths)), lengths, rolling)  ]

    animations.append(anim_loop)

    style = ' '.join(animations)
    #write the HTML file the name should match the SVG 
    with open('%s.html'%src_fn.split('.')[0],'w') as fp:
        fp.write(html.format(style, svg))
        

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print('usage: %s file.svg'%sys.argv[0])
        sys.exit(1)
        
    fn = sys.argv[1]
    mk_anim(fn)
    
