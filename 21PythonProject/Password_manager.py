# import lirabry to encode and decode your password
from cryptography.fernet import Fernet

'''# write key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''

# load key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# combine key with master password
key = load_key()
fer = Fernet(key)


# view function
def view():
    # use with to automatic close the file after read text
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # remove /n when read line
            data = line.rstrip()
            # split text by "|"
            user_name, passw = data.split("|")
            print("User :", user_name, ", Password :", fer.decrypt(passw.encode()).decode())

# add function
def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    # use with to automatic close the file after write text
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Add a new password or view existing ones (view/add)? Otherwise, press q to exit.")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue    