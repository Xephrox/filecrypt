#!/usr/bin/python3

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

class AES_Cipher:
    def __init__(self, key, blocksize):
        self._key = key
        self._blocksize = blocksize

    def encrypt(self, infile, outfile, filesize):
        blocksize = self._blocksize
        IV = Random.new().read(blocksize)
        key = self._key
        encryptor = AES.new(key, AES.MODE_CBC, IV)
        chunksize = blocksize*1024
        outfile.write(filesize.encode('utf-8'))
        outfile.write(IV)

        while True:
            chunk = infile.read(chunksize)
            if len(chunk) == 0:
                break
            elif len(chunk)%blocksize != 0:
                padding_length = (blocksize - len(chunk)%(blocksize))
                chunk += padding_length * chr(padding_length).encode('utf-8')
            outfile.write(encryptor.encrypt(chunk))

    def decrypt(self, infile, outfile):
        blocksize = self._blocksize
        chunksize = blocksize*1024
        filesize = int(infile.read(blocksize))
        IV = infile.read(blocksize)
        key = self._key
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        nextchunk = b''
        while True:
            chunk, nextchunk = nextchunk, decryptor.decrypt(infile.read(chunksize))
            if (len(chunk) == 0):
                continue
            if(len(nextchunk) == 0):
                padding_length = chunk[-1]
                chunk = chunk[:-padding_length]
                outfile.write(chunk)
                break
            outfile.write(chunk)

