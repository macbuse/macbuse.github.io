tt = ' '.join(guesses)
guess = 'slane'

ss  = list(zip(guess, mm))
sub += ''.join([x for x,y in ss if y == '*' and x not in sub])
nsub += ''.join([x for x,y in ss if y == 'x' ])

if nsub:
    #fails if the guess is an anagram 
    tt = re.sub(r'[{}]'.format(nsub),'',tt)
tt = [w for w in tt.split() if len(w) == len(guesses[0])]

tt = [w for w in tt if all( x in w for x in sub )]

chks1 = [i for i,y in enumerate(mm) if y == '_']
for i in chks1:
    tt = [w for w in tt if w[i] == guess[i]]
    
#I had to fix this to have memory
#and not be stateless

for i,y in enumerate(mm):
    if y == '*':
        forbidden[i] += guess[i]
        
for i,x in enumerate(forbidden):
    if not forbidden[i]: continue
    tt = [w for w in tt if w[i] not in forbidden[i]]

