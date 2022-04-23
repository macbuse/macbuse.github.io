#! /home/gregmcshane/anaconda3/bin/python3

import requests
import re, sys
TeX_template  = '''
\\documentclass[14pt]{amsart}
\\begin{document}
{\\Large Wiki Math}

%s
\\end{document}
'''

TeX_pp = r'<math.*?alttext="\{\\displaystyle (.*?)\}"'
pp = re.compile(TeX_pp, re.DOTALL)

def pull_math(url):
    r = requests.get(url, allow_redirects=True)
    res = pp.findall(r.content.decode('utf-8'), re.DOTALL)
    if res == []: 
        print('nomath :(')
        sys.exit(0)
    res = ['$ %s$\n'%x for x in res]
    fn = "%s.tex"%url.split('/')[-1]
    print(fn)
    with open(fn,'w') as fp:
        fp.write(TeX_template%'\n'.join(res))
                                        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = 'https://en.wikipedia.org/wiki/Markov_number'

    pull_math(url)

                                                    
