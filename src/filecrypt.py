#!/usr/bin/python3

import os, sys, getopt
import utiltool
from Crypto.Hash import MD5, SHA256

def usage():
    print ("./filecrypt.py <options>")
    print ("OPTIONS")
    print ("-h|--help Display this help dialogue")
    print ("-e|--encrypt <file to encrypt>")
    print ("-d|--decrypt <file to decrypt>")
    print ("-p|--password <password>")
    print ("-s|--security <low|high>")
    print ("Eg. ./filecrypt.py -e cutekittens.jpg -p halelujah -s high")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "he:d:p:s:", ["help", "encrypt=", "decrypt=", "password=", "security="])
    except(getopt.GetoptError):
        usage()
        sys.exit(-1)

    encrypt = False
    decrypt = False
    password = ''
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-e", "--encrypt"):
            filename = a
            encrypt = True
        elif o in ("-d", "--decrypt"):
            filename = a
            decrypt = True
        elif o in ("-p", "--password"):
            password= a
        elif o in ("-s", "--security"):
            security = a

    if (encrypt and decrypt):
        print ("[!]Error: Please Select Either Encryption or Decryption")
        usage()
        print ("[!]EXITING NOW")
        sys.exit(-1)

    if (password == ''):
        print ("[!]Error: Password Not Set, Please enter a password")
        usage()
        print ("[!]EXITING NOW")
        sys.exit(-1)

    #TEMP key and blocksizes
    if (security == "low"):
        hasher = MD5.new()
        hasher.update(password.encode('utf8'))
        key = hasher.hexdigest()
    elif (security == "high"):
        hasher = SHA256.new(password.encode('utf-8'))
        key = hasher.digest()
    else:
        print ("[!] Error: Invalid Security Option")
        usage()
        print ("[!]EXITING NOW")
        sys.exit(-1)

    blocksize = 16
    operator = utiltool.AES_Cipher(key,blocksize)
    filesize = str(os.path.getsize(filename)).zfill(blocksize)
    if (encrypt == True):
        print("[*]Encrypting "+filename+" with password "+password)
        with open(filename, 'rb+') as infile:
            with open(filename, 'rb+') as outfile:
                operator.encrypt(infile, outfile, filesize)
        print("[*]Done")

    elif (decrypt == True):
        print("[*]Decrypting "+filename+" with password "+password)
        with open(filename, 'rb+') as infile:
            with open(filename, 'rb+') as outfile:
                operator.decrypt(infile, outfile)
        print("[*]Done")

if __name__ == '__main__':
    print("\n*")
    print("* File Cipher Program")
    print("* Author: Th0rin")
    print("*\n")

    main(sys.argv[1:])
