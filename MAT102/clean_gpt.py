#!/usr/bin/python3.9 
import sys, os
import re
import subprocess

def open_file_in_read_mode():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # print(os.getcwd())
    ss = open_file_in_read_mode()
    if not ss:
        sys.exit(1)

    tt = re.sub(r'\\\(\s*',r'$',ss)
    tt = re.sub(r'\s*\\\)',r'$',tt)
    tt = re.sub(r'\s*\\\]',r'$$',tt)
    tt = re.sub(r'\\\[\s*',r'$$',tt)


    fn = sys.argv[1]
    fn = fn.split(".")[0]
    
    with open("./tt.md","w") as fp:
        fp.write(tt)

    #remember to split before passing to subprocess
    pandoc_it = f'pandoc -s tt.md -o {fn}.html'.split()
    pandoc_it.extend('--mathml --metadata title=Correction'.split())
    subprocess.call(pandoc_it)
    print("Done")



