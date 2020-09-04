import pickle
import pyperclip

m_password = input("enter master password: ")

if (m_password == "yegon"):
    account_name = input ("enter account name: ")
    with open("game.asdasd","br") as readfile:
        info = pickle.load(readfile)

    if account_name in info:
        pyperclip.copy(info[account_name])
        print ("password copied onto clipboard")

    else:
        print("account name or password not found")

else:
    print("incorrect master password")
