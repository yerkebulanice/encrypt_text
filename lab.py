import os

def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in message:
            ind = message.find(chars)
            ind += key
            encrypted +=  message[ind]
    return encrypted

def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in message:
            ind = message.find(chars)
            ind -= key
            decrypted +=  message[ind]
    return decrypted

def main():
    filePath = str(input('Upload your file which you want to encrypt: '))
    message = open(filePath, "r")
    message = message.read()
    print(message)
    text_count = message.split()
    number_of_text = len(text_count)
    print('Count of words: ', number_of_text)
    message = message.lower()
    key = int(input('Enter your key, please(It should be number between [1 - 26]): '))
    choice = input('Encrypt or Decrypt? [E/D]: ')
    encrypted = open("encrypted.txt", "w")
    if choice.lower().startswith('e'):
        encrypted_text = encrypt(message, key)
        print('Encrypted text: ', encrypted_text)
        encrypted.write(encrypted_text)
        print('Your encrypted text saved at: ', os.path.abspath("encrypted.txt"))
    else:
        print('Decrypted text: ', decrypt(message, key))

if __name__ == '__main__':
    main()