from cryptography.fernet import Fernet
import json

key = Fernet.generate_key()

def crypter():
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

    with open('data.json', 'r') as file:
        data = json.load(file)

    json_string = json.dumps(data)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(json_string.encode())

    with open('encrypted_file.json', 'wb') as file:
        file.write(encrypted)

def decrypt():
    with open('encrypted_file.json', 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = Fernet.decrypt(encrypted_data)
    decrypted_json = json.loads(decrypted_data)

    with open('decrypted_file.json', 'w') as file:
        json.dump(decrypted_json, file)

decrypt()