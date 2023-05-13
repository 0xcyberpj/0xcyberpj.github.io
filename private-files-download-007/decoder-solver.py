#!/usr/bin/python3
import re
import argparse
def decoder(filename):
    # Read the encoded binary from the file
    with open(filename, 'r') as encoded_file:
        encoded_binary = encoded_file.read().strip().split(' ')
    # Replacing  zero-width space and zero-width non-joiner characters with 0s and 1s :)
    replaced_binary = [b.replace('\u200b','1').replace('\u200c','0') for b in encoded_binary]
    plain_ascii = [int(b, 2) for b in replaced_binary]
    plain_text = ''.join([chr(a) for a in plain_ascii])
    return plain_text
    
parser = argparse.ArgumentParser(description='Decoding function	')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--decode', metavar='ENCODED_TEXT', help='Decode encoded text')
parser.add_argument('-f', '--file', metavar='FILE', help='File containing encoded text (if not passed, use -d input instead)')
args = parser.parse_args()

if args.decode:
    if args.file:
        plain_text = decoder(args.file)
    else:
        plain_text = decoder(args.decode)
new_flag=''
for i in plain_text:
	if(ord(i)>1000):
		continue
	else:
		new_flag+=i
pattern = re.findall(r'TB\{[^{}]*\}', new_flag)
print('H'+pattern[0])	

		
