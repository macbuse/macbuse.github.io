#! /home/gregmcshane/anaconda3/bin/python3.6 

import re, sys, os
from svgpathtools import svg2paths, wsvg

pp_path = re.compile('<path(.*?)\s(d=".*?)/>', re.DOTALL)
pp_metadata = re.compile('<metadata>.*?<metadata/>', re.DOTALL)

wrapper = '''
<animate id="{}"
 attributeName="stroke-dashoffset"
 begin="{}"
 dur="{}"
 values="{}"
 fill="freeze" />
 '''

bkground = '''
<g id="back_ground" >
<path d="M0+0L640+0L640+480L0+480L0+0Z" opacity="1" fill="#{}"/>
</g>
'''

def mk_anim(src_fn, 
            out_fn=None):


    def path_cb(mm):
    # this has to be nested because of the pop from the list 
        path_num, ll = lengths.pop(0)
    
        dash = 'stroke-dashoffset="{}"\nstroke-dasharray="{} {}" '.format(ll,ll,ll)
        
        curve =  '<path {}\n{}\n{}\n>'.format(mm.group(1),
                                            dash,
                                            mm.group(2))
    
        anim =  wrapper.format('an%d'%path_num, 
                           '0s' if path_num == 0  else 'an%d.end'%( path_num-1), 
                           '{:.2f}s'.format(ll/800), #this is the duration
                           '%d;0'%ll)  

        return curve  + anim + '</path>'

    
    if not out_fn:
        out_fn = src_fn.split('.')[0] + '_anim' +'.svg'
        
    paths, attributes = svg2paths(src_fn)
    
    with open(src_fn,'r') as fp:
        data = fp.read()

    #delete the thumbnail
    data = re.sub(pp_metadata,'', data)

    lengths = [ (k, int(p.length()) ) for k,p in enumerate(paths) ]
    uu = lengths[:] # copy for debugging

    data = re.sub(pp_path,path_cb, data) #add the animations
    data = data.replace('<defs', '<defs/>' + bkground.format('ffdd00')) #add a backgrouns

    with open(out_fn,'w') as fp:
        fp.write(data)
   
    
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print('usage: animate_svg.py file.svg')
        sys.exit(1)
        
    fn = sys.argv[1]
    mk_anim(fn)
    
    
    
