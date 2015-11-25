#!/usr/bin/python3

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename):
    outputfile = "[Encrypted]"+filename
    blocksize = AES.block_size
    IV = Random.new().read(blocksize)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    chunksize = 64*1024
    filesize = str(os.path.getsize(filename)).zfill(blocksize)
    with open(filename, 'rb') as infile:
        with open(outputfile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk)%blocksize != 0:
                    chunk += b"\0" * (blocksize - len(chunk)%blocksize)
                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    chunksize = 64*1024
    outputfile = filename[11:]
    blocksize = AES.block_size
    with open(filename, 'rb') as infile:
        filesize = int(infile.read(blocksize))
        IV = infile.read(blocksize)
        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputfile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if(len(chunk) == 0):
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()



