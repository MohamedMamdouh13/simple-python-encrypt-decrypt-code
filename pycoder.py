#created by Mohamed Mamdouh
from cryptography.fernet import Fernet
print ("welcome to the most complex encoder ever!")
message = input("please enter the text you want to encrypt : ")
print("------------------------------------")
key = Fernet.generate_key()

Fernet = Fernet(key)
encryptedMessage = Fernet.encrypt(message.encode())
print("original string: ", message)
print("------------------------------------")
print("encrypted string: ", encryptedMessage)
print("------------------------------------")
decryptedMessage = Fernet.decrypt(encryptedMessage).decode()

print("decrypted string: ", decryptedMessage)

print("created by Mohamed Mamdouh :)")
