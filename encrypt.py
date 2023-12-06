import os, sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from getpass import getpass

def encrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename + ".enc"
    filesize = str(os.path.getsize(filename)).zfill(16)
    iv = Random.new().read(AES.block_size)

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            # storing hash of key at beginning of the file to help with password checking
            keyHash = SHA256.new(key).digest()
            outfile.write(keyHash)

            outfile.write(filesize.encode('utf-8'))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b'\x00' * (16 - (len(chunk) % 16))
                
                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = os.path.splitext(filename)[0]

    with open(filename, 'rb') as infile:
        # checking if password is the same as the one used for encryption
        fileKeyHash = infile.read(32)
        if SHA256.new(key).digest() != fileKeyHash:
            print("Password is incorrect or the file is corrupted")
            return
        
        filesize = int(infile.read(16))
        iv = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def Main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")

    if choice == 'E':
        filename = input("File to encrypt: ")
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        password = getpass(prompt="Password: ")
        encrypt(getKey(password), filename)
        print( "Done.")
    elif choice == 'D':
        filename = input("File to decrypt: ")
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        elif not filename.endswith(".enc"):
            print(f"{filename} does not appear to be an encrypted file.")
            return
        password = getpass(prompt="Password: ")
        decrypt(getKey(password), filename)
        print("Done.")
    else:
        print("Invalid option.")

if __name__== '__main__':
    Main()

