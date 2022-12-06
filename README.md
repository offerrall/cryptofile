# Description
This is a small Python script that allows you to encrypt and decrypt files and folders using the Fernet algorithm from the Python cryptography library.

# Usage
crypto_file [option] [file/folder] [key]

# Options
- -e, --encrypt: Encrypt a file or folder
- -d, --decrypt: Decrypt a file or folder
- -g, --generate: Generate a key
- -h, --help: Show this help

# Examples
Encrypt a file
- crypto_file.py -e file.txt key.key
- crypto_file.py -e file.txt tmFbNuJ-GJah1VoBx-T0aFa1pXROGajnvEC-XgKa5l4=

# Decrypt a file
- crypto_file.py -d file.txt.encrypted key.key
- crypto_file.py -d file.txt.encrypted tmFbNuJ-GJah1VoBx-T0aFa1pXROGajnvEC-XgKa5l4=

# Generate a key:
crypto_file.py -g

# Requirements
pip install cryptography
