#!/usr/bin/python3

import os, sys, getopt
import utiltool
import random, string
from Crypto.Hash import MD5, SHA256

def usage():
    print ("USAGE:")
    print ("./filecrypt.py <options>")
    print ("OPTIONS")
    print ("-h|--help Display this help dialogue")
    print ("-e|--encrypt <file to encrypt>")
    print ("-d|--decrypt <file to decrypt>")
    print ("-p|--password <password>")
    print ("Eg. ./filecrypt.py -e cutekittens.jpg -p halelujah")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "he:d:p:", ["help", "encrypt=", "decrypt=", "password="])
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
            password = a

    if (encrypt==decrypt):
        print ("[!]Error: Mode Not Set")
        choice = input("Would you like to encrypt or decrypt? (e/d): ")
        if (choice.lower() == 'e' or choice.lower() == 'encrypt'):
            encrypt = True
        elif (choice.lower() == 'd' or choice.lower() == 'decrypt'):
            decrypt = True
        else:
            print ("[!]Invalid Options, Exiting")
            sys.exit(-1)
        filename = input("Please Enter the Filename: ")

    if (password == ''):
        print ("\n[!]Error: Password Not Set")
        if (decrypt):
            password = input("Please enter the password: ")
            if (password == ''):
                print ("Please Try again.")
                sys.exit(-1)
        else:
            option = input("Would you like to generate a random password? (y/n): ")
            if (option.lower() == 'y' or option.lower()=='yes'):
                password = ''.join(random.SystemRandom().choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(20))
            elif (option.lower() == 'n' or option.lower()=='no'):
                password = input("Please enter the password: ")
            else:
                print ("[!]Please Try again. Exiting Now")
                sys.exit(-1)

    hasher = MD5.new()
    hasher.update(password.encode('utf8'))
    key = hasher.hexdigest()
    blocksize = 16
    operator = utiltool.AES_Cipher(key,blocksize)
    filesize = str(os.path.getsize(filename)).zfill(blocksize)

    if (encrypt == True):
        print("\n[*]Encrypting "+filename+" with password "+password)
        if (option == 'y'):
            print ("[!]Please Take note of the password")
        with open(filename, 'rb+') as infile:
            with open(filename, 'rb+') as outfile:
                operator.encrypt(infile, outfile, filesize)
        print("[*]Done")

    elif (decrypt == True):
        print("\n[*]Decrypting "+filename+" with password "+password)
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
