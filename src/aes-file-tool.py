#!/usr/bin/python3

import os, sys, getopt
import utiltool

def usage():
    print ("./aes-file-tool.py <options>")
    print ("OPTIONS")
    print ("-h|--help Display this help dialogue")
    print ("-e|--encrypt <file to encrypt>")
    print ("-d|--decrypt <file to decrypt>")
    print ("-p|--password <password>")
    print ("Eg. ./aes-file-tool.py -e cutekittens.jpg -p halelujah")

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
            password= a

    if (encrypt and decrypt)
        print ("[!]Error: Please Select Either Encryption or Decryption")
        usage()
        print ("[!]EXITING NOW")
        sys.exit(-1)

    if (password == '')
        print ("[!]Error: Password Not Set, Please enter a password")
        usage()
        print ("[!]EXITING NOW")
        sys.exit(-1)

    if (encrypt == True):
        print("[*]Encrypting "+filename+" with password "+password)
        utiltool.encrypt(utiltool.getKey(password), filename)
        print("[*]Done")
    elif (decrypt == True):
        print("[*]Decrypting "+filename+" with password "+password)
        utiltool.decrypt(utiltool.getKey(password), filename)
        print("[*]Done")

if __name__ == '__main__':
    print("\n*")
    print("* AES File Encryptor ")
    print("* Author: Th0rin")
    print("*\n")

    main(sys.argv[1:])
