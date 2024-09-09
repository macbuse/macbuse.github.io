import sys
import re

def open_file_in_read_mode():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    open_file_in_read_mode()
