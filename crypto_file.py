from cryptography.fernet import Fernet
from sys import argv
from os.path import exists, isdir
from os import listdir

def decrypt_file(key: str, file_name: str) -> str:
    """decrypts a file and returns the name of the decrypted file

    Args:
        key (str): key to decrypt the file
        file_name (str): name of the file to decrypt

    Returns:
        str: name of the decrypted file
    """

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
    """encrypts a file and returns the name of the encrypted file

    Args:
        key (str): key to encrypt the file
        file_name (str): name of the file to encrypt

    Returns:
        str: name of the encrypted file
    """
    
    with open(file_name, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_name + ".encrypted", "wb") as f:
        f.write(encrypted_data)
        
    return file_name + ".encrypted"

def get_key(folder: str) -> str:
    """generates a key and saves it into a file
    
    Args:
        folder (str): folder to save the key
    
    Returns:
        str: key generated
    """
    
    key = Fernet.generate_key()
    file_path = folder + "key.key"
    with open(file_path, "wb") as f:
        f.write(key)
    
    return file_path


def Help():
    """prints the help message"""
    
    print("Usage: crypto_file [option] [file] [key]")
    print("Options:")
    print(" -e, --encrypt: Encrypt a file or folder")
    print(" -d, --decrypt: Decrypt a file or folder")
    print(" -g, --generate: Generate a key")
    print(" -h, --help: Show this help")
    
    print("Example: crypto_file -e file.txt key.key")
    print("Example: crypto_file -e file.txt tmFbNuJ-GJah1VoBx-T0aFa1pXROGajnvEC-XgKa5l4=")
    print("Example: crypto_file -d file.txt.encrypted key.key")
    print("Example: crypto_file -d file.txt.encrypted tmFbNuJ-GJah1VoBx-T0aFa1pXROGajnvEC-XgKa5l4=")
    print("Example: crypto_file -g")
    

def decrypt_file_wrapper(file_or_folder: str, key: str):
    """decrypts a file and returns the name of the decrypted file
    
    Args:
        file_or_folder (str): name of the file or folder to decrypt
        key (str): key to decrypt the file
    
    Returns:
        str: name of the decrypted file
    """
    
    folder = False
    
    if isdir(file_or_folder):
        folder = True
        if not file_or_folder.endswith("/"):
            file_or_folder += "/"

        if not exists(file_or_folder):
            print("Folder not found")
            return
    else:
        if not exists(file_or_folder):
            print("File not found")
            return
    
    if folder:
        for file in listdir(file_or_folder):
            try:
                file = decrypt_file(key, file_or_folder + file)
                print("File decrypted: " + file)
            except Exception as e:
                print("Error decrypting file " + file)
                print(e)
    else:
        try:
            file = decrypt_file(key, file_or_folder)
            print("File decrypted: " + file)
        except Exception as e:
            print("Error decrypting file " + file_or_folder)
            print(e)
        
def encrypt_file_wrapper(file_or_folder: str, key: str):
    """encrypts a file and returns the name of the encrypted file
    
    Args:
        file_or_folder (str): name of the file or folder to encrypt
        key (str): key to encrypt the file
    
    Returns:
        str: name of the encrypted file
    """
    
    folder = False
    
    if isdir(file_or_folder):
        folder = True
        if not file_or_folder.endswith("/"):
            file_or_folder += "/"

        if not exists(file_or_folder):
            print("Folder not found")
            return
    else:
        if not exists(file_or_folder):
            print("File not found")
            return
    
    if folder:
        for file in listdir(file_or_folder):
            try:
                file = encrypt_file(key, file_or_folder + file)
                print("File encrypted: " + file)
            except Exception as e:
                print("Error encrypting file " + file)
                print(e)
    else:
        try:
            file = encrypt_file(key, file_or_folder)
            print("File encrypted: " + file)
        except Exception as e:
            print("Error encrypting file")
            print(e)
    
def get_key_wrapper():
    """generates a key and saves it into a file"""
    
    try:
        key = get_key("./")
        print("Key generated: " + key)
    except Exception as e:
        print("Error generating key")
        print(e)


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

