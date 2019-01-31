#!/usr/bin/python
import sys, getopt, argparse


parser = argparse.ArgumentParser(prog='shellcode-cleaner', description='Takes pasted shellcode and cleans it however you like.', epilog="Default is to strip ALL of these characters. It'll strip spaces as well.")
parser.add_argument('-n', action='store_true', help="strip newline (\\n) characters")
parser.add_argument('-r', action='store_true', help="strip (\\r) characters")
parser.add_argument('-q', action='store_true', help="strip quotation marks (\"\") AND single quotes")
parser.add_argument('-x', action='store_true', help="strip (\\x) characters")
parser.add_argument('-s', action='store_true', help="strip semicolons (;)")
args = parser.parse_args()
print "Shellcode (Press Enter then Control+D to submit):"
dirty_shellcode = sys.stdin.read() 
args_dict = {
  "n": args.n,
  "r": args.r,
  "q": args.q,
  "x": args.x,
  "s": args.s
}
#Clean up spacing first
clean_shellcode = dirty_shellcode.replace(' ', '')
#This is for the "default option" to actually work. If any flag is set it will be set to false and the operation under the flags will proceed. If none are set, then the default operaiton to strip ALL the bad chars will occur.
default_flag=True
for key, value in args_dict.iteritems():
    if value == True:
        default_flag=False
        if key == 'n' :
            clean_shellcode = clean_shellcode.replace('\n', '')
        elif key == 'r' :
            clean_shellcode = clean_shellcode.replace('\r', '')
        elif key == 'q' :
            clean_shellcode = clean_shellcode.replace('"', '').replace('\'', '')
        elif key == 'x' :
            clean_shellcode = clean_shellcode.replace('\\x', '')
        elif key == 's' :
            clean_shellcode = clean_shellcode.replace(';', '')
if default_flag == True:
    clean_shellcode = dirty_shellcode.replace('\n', '').replace('\r', '').replace('"', '').replace('\\x', '').replace(';', '').replace(' ', '')
print clean_shellcode