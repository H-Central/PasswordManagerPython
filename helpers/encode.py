from cryptography.fernet import Fernet
import json

def genKEY():
    key = Fernet.generate_key()
    with open('.key', 'wb') as key_file:
        key_file.write(key)
    f = Fernet(key)

def loadKEY():
    with open('.key', 'wb') as key_file:
        key_file.read(key)
    f = Fernet(key_file)

def crypter():
    loadKEY()
    with open('data.json', 'r') as file:
        data = json.load(file)

    json_string = json.dumps(data)
    encrypted = f.encrypt(json_string.encode())

    with open('data_crypt.json', 'wb') as file:
        file.write(encrypted)

def decrypt():
    loadKEY()
    with open('data_crypt', 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    decrypted_json = json.loads(decrypted_data)

    with open('data_decrypt.json', 'w') as file:
        json.dump(decrypted_json, file)
