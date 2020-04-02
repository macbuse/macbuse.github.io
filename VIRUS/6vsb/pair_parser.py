#!/usr/bin/env python


import re, os, sys

sys.stdout.write('starting run\n'+'_'*20 + '\n'*2)

import pandas as pd
import numpy as np

def txt2csv(fn, 
            tag='',
            base_dir = './'):
    
    if not os.path.isfile(fn):
        sys.stdout.write(fn + ' does NOT exist\n')
        return 
    
    with open(fn ,'r') as fp:
        txt = fp.read()
        
    sys.stdout.write('>> opened ' + fn + '\n')
    header, body = txt .split('----------\n') 

    hp = re.compile('COL\s+\d+(.*)')
    tp = re.compile('([^\s]+?)\.pdb')
    
    mm = tp.search(header)
    if mm:
        name = mm.group(1)
    else:
        name = ''
    
    col_names = [ x.strip().split(' ')[0] for x in hp.findall(header)]
    
    #make unique column names for pandas
    names = {}
    for k,x in enumerate(col_names):
        if x not in names:
            names[x] = 0
            continue
        names[x] += 1
        col_names[k] += str(names[x])
 
    #kill the last line
    body = re.sub(';.*','',body)
    #replace [space] by the delimitor
    body = re.sub('[ ]+',',', body)
    
    num_cols = len(body[:2000].split('\n')[0].split(',')) 
    #add extra column names if necessary
    if num_cols > len(col_names):
        sys.stdout.write ('>>>%s fixing columns\n'%fn)
        col_names.extend(['COL %d'%(k + 1 + len(col_names))  
                                for k in range(num_cols - len(col_names))])
    
    return name, ''.join([ ','.join(col_names),'\n', body[:-1]])


def merge_tables(df1,df2):
    
    #fix _ convention
    donors, acceptors = df1['Donor'].values, df1['Acceptor'].values

    acceptors[acceptors == '_'] = donors[acceptors == '_']  
    df1['Acceptor'] = pd.Series(acceptors, index=df1.index)

    #fix NC- convention as we are taking logs later
    df2.loc[df2['Density']<0, 'Density'] = 1.

    #add the column 
    ee = np.log(19000) - np.log( df2['Density'].values)
    df1['-log Density'] = pd.Series(ee, index=df1.index)
    
    return df1
 

    
def totals4residues(df, col='-log Density'):
    
    all_bonds, residues = [], []
    
    for rr in ['Donor','Acceptor']:
        #these now should look like  A0001 etc.
        names = df[rr].values
        all_bonds.extend(list(zip( names,df[col])))
        residues.extend(names)

    totals = { x:[] for x in set(residues)}

    for x,y in all_bonds:
        totals[x].append(y)
      
    
    #this is only for debugging###
    T  = list( zip(* sorted(totals.items()) ) )
    A,B = T
    
    ddf = pd.DataFrame({'RES': A, 'VAL': [str(x) for x in B]})
    ddf.to_excel('debug.xls',
                float_format="%.2f")
    
    #####
        
    for x,y in totals.items():
        totals[x] = sum(y)
  
    return totals

def res2str(x):
    chain, num = x
    return chain + '%04d' % num

def str2res(x):
    return x[0], int(x[1:])

def mk_smoothed_table(totals):
    
    new_table = {}

    totals = totals4residues(df)

    for curr, val  in totals.items():
        chain, num = str2res(curr)
        prev =  res2str([chain, num-1])
        for res in [prev, curr]:
            if res not in new_table:
                new_table[res] = []
            new_table[res].append(val)

    for a,b in new_table.items():
        new_table[a] = sum(b)*.5
        
    return new_table

def new_format(df):
    
    donors = df['Donor'].values
    chains = sorted(list(set([x[0] for x in donors])))
    num_rows = max([ int(x[1:]) for x in donors]) + 2
    
    #this is a bit of a cheat but np.ndarray is easier to use than pd
    rows = np.zeros((num_rows, len(chains))) 
    for k, c in enumerate(chains):
        tdf = df[df['Donor'].str.contains(c) ]
        #drop the letter that denotes the chain to get the residue 
        res  = np.array([ int(x[1:]) for x in tdf['Donor'].values])
        bif = [k for k, v in enumerate(res[1:]) if res[k] == res[k-1]] 
        if bif != []:
            print(c + ' :'  + ' '.join([repr(x) for x in bif]))
        
        res = np.delete(res,bif)
        vals = np.delete(tdf['-log Density'].values, bif)
        
        rows[ res.astype(dtype='int32'), k] = vals
    
    #these are the rows to keep
    non_null = np.where(np.sum(rows, axis=1) > 0)[0]
    #add the residue nums at the end
    rows = np.append(rows, 
                     np.arange(num_rows).reshape((num_rows,1)),
                    axis=1)
    
    #drop the rows and make the df
    dff = pd.DataFrame(data=rows[non_null ,:])
    chains.append('res')
    dff.columns = chains
    return dff


if __name__ == '__main__':

    fns = ['hb-stress.txt', 'full_out.txt']
    pdb_name = 'generic'
    csv_fns =[]
    
    for fn in fns:
        result = txt2csv(fn)
        if result:
            name, csv = result
            if name != '':
                pdb_name = name
                
            #save this for later
            csv_fns.append(pdb_name + '_greg_' + fn.split('.')[0] + '.csv')
            
            with open(csv_fns[-1], 'w') as fp:
                fp.write(csv)
        
    
    sys.stdout.write('merging tables\n')
    stresses, densities = csv_fns
    
    df = merge_tables(pd.read_csv(stresses), 
                      pd.read_csv(densities))
    #save a preliminary excel
    df.to_excel(pdb_name + '_merged_stress_density.xls',
               float_format="%.2f")
    # CSV version 
    df.to_csv(pdb_name + '_merged_stress_density.csv',
               float_format="%.2f")
    
    sys.stdout.write('saving donor | Acceptor | -log Density | stress\n' )
    for res in ['Donor', 'Acceptor']:
        names = [ '%s%04d'%x for x in zip(df[res], df[res+'1']) ]
        df[res] = pd.Series( names, index=df.index)

    cols = ['Donor', 'Acceptor', '-log Density', 'Stress']
    df[cols].to_excel(pdb_name + '_residue_density.xls', 
                      float_format="%.2f")
    
    sys.stdout.write('making smoothed data\n')
    totals = totals4residues(df)
    RR, EE = list( zip(* sorted( mk_smoothed_table(totals).items()) )  )
    ndf = pd.DataFrame( {'residue' : RR, 'energy' : EE})
    ndf.to_excel(pdb_name + '_smoothed.xls', 
                 float_format="%.2f")
    
    
    sys.stdout.write('making %s_one_chain_per_col.csv\n\n'%pdb_name)
    new_format(df).to_csv('%s_one_chain_per_col.csv'%pdb_name)
    

    sys.stdout.write('Done')
