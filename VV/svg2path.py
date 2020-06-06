import re

pp = re.compile('d="(M.*?)"',re.DOTALL)

with open('ss.svg','r') as fp:
    data  = fp.read()

mm = pp.search(data)

with open('ss','w') as fp:
    fp.write(mm.group(0))
