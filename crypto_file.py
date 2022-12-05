from cryptography.fernet import Fernet
from sys import argv
from os.path import exists

def decrypt_file(key: str, file_name: str) -> str:

    with open(file_name, "rb") as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    data = fernet.decrypt(encrypted_data)

    if ".encrypted" in file_name:
        file_name = file_name.replace(".encrypted", "")
    
    with open(file_name, "wb") as f:
        f.write(data)
        
    return file_name

def encrypt_file(key: str, file_name: str) -> str:
    
    with open(file_name, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_name + ".encrypted", "wb") as f:
        f.write(encrypted_data)

    with open("key.key", "wb") as f:
        f.write(key)
        
    return file_name + ".encrypted"

def get_key(folder: str) -> str:
    
    key = Fernet.generate_key()
    file_path = folder + "key.key"
    with open(file_path, "wb") as f:
        f.write(key)
    
    return file_path


def Help():
    
    print("Usage: crypto_file [option] [file] [key]")
    print("Options:")
    print(" -e, --encrypt: Encrypt a file")
    print(" -d, --decrypt: Decrypt a file")
    print(" -g, --generate: Generate a key")
    print(" -h, --help: Show this help")
    
    print("Example: crypto_file -e file.txt key.key")
    print("Example: crypto_file -e file.txt tmFbNuJ-GJah1VoBx-T0aFa1pXROGajnvEC-XgKa5l4=")
    print("Example: crypto_file -d file.txt.encrypted key.key")
    print("Example: crypto_file -d file.txt.encrypted tmFbNuJ-GJah1VoBx-T0aFa1pXROGajnvEC-XgKa5l4=")
    print("Example: crypto_file -g")
    

def decrypt_file_wrapper(file_name: str, key: str):
    
    if not exists(file_name):
        print("File not found")
        return
    
    try:
        file = decrypt_file(key, file_name)
        print("File decrypted: " + file)
    except Exception as e:
        print("Error decrypting file")
        print(e)
        
def encrypt_file_wrapper(file_name: str, key: str):
    
    if not exists(file_name):
        print("File not found")
        return
    
    try:
        file = encrypt_file(key, file_name)
        print("File encrypted: " + file)
    except Exception as e:
        print("Error encrypting file")
        print(e)
    
def get_key_wrapper():
    
    key = get_key("./")
    print("Key generated: " + key)


if __name__ == "__main__":

    if len(argv) >= 2:

        option = argv[1]
        file_name = argv[2] if len(argv) >= 3 else None
        key = argv[3] if len(argv) >= 4 else None
        
        if key is not None:
            if exists(key):
                with open(key, "rb") as f:
                    key = f.read()

        if option == "-d" or option == "--decrypt":
            decrypt_file_wrapper(file_name, key)

        elif option == "-e" or option == "--encrypt":
            encrypt_file_wrapper(file_name, key)

        elif option == "-g" or option == "--generate":
            get_key_wrapper()

        elif option == "-h" or option == "--help":
            Help()

        else:
            print("Error: invalid option")
            Help()

    else:
        Help()
        input("Press enter to exit")
