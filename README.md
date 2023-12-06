# file-encryptor

Project Title: File Encryption and Decryption Utility

Description:
This project is a Python-based tool for encrypting and decrypting files using AES. It provides a command-line interface allowing users to encrypt files with a password and decrypt them using the same password. Key features include:

Password-Based Encryption: Utilizes SHA256 for hashing the password, which is then used as the key for AES encryption.
Secure File Handling: Encrypts and decrypts files of any size, processing data in chunks.
Integrity Checking: Incorporates a mechanism to verify the correctness of the password during decryption by storing a hash of the encryption key within the encrypted file.
Padding for Block Alignment: Automatically pads the last block of data during encryption and removes this padding after decryption.

Usage:

Run the script in a Python environment.
Choose between encryption (E) and decryption (D) options.
Provide the filename and the password.

Security Note:
This tool is intended for educational purposes and should be used with caution for encrypting sensitive data. The implementation demonstrates basic cryptographic concepts but may not meet all the security standards required for more demanding applications.

