#!/usr/bin/python3
import argparse
from pwn import xor

def decrypt_file(filename, xor_hex):
    # Read the encrypted file
    encrypted_data = open(filename, 'rb').read()
    # Decrypt the file using XOR hex -> (ffd8.. ) => something into \xff\xd8
    decrypted_data = xor(encrypted_data, bytes.fromhex(xor_hex))
    #  the decrypted data to a new file
    '''Now the decrypted flag will contain the actual key which is used to encrypt
    so now we can get the flag from the key'''
    output_filename = 'key_of_' + filename.replace('png','txt')
    with open(output_filename, 'wb') as file:
        file.write(decrypted_data[0:10])
        print('\tKEY :  '+decrypted_data[0:10].decode())
        file.write(b'\n')

def retrive(filename,key):
    original_data_for_flag = open(filename, 'rb').read()
    output_file_name_flag='final_flag_'+filename
    flag=open(output_file_name_flag,'wb')
    flag.write(xor(original_data_for_flag,key))
    print('Done successful '+output_file_name_flag)
    flag.close()

def main():
    parser = argparse.ArgumentParser(description='XOR encryption and decryption tool')
    parser.add_argument('filename', type=str, help='Name of the file to encrypt or decrypt')
    parser.add_argument('key', type=str, help='XOR key for encryption or decryption')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decrypt', action='store_true', help='Perform decryption And Ge the KEY')
    group.add_argument('-f', '--flag',action='store_true',help='final flag  from key')
    args = parser.parse_args()
    filename = args.filename

 
    if args.decrypt:
        xor_hex = args.key.replace(" ", "")
        decrypt_file(filename, xor_hex)
    elif args.flag:
        xor_hex=args.key.encode()
        retrive(filename,xor_hex)

if __name__ == '__main__':
    main()

#8950 4e47 0d0a 1a0a 0000 000d 4948