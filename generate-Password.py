import random
import pickle

info = {}

with open("game.asdasd","br") as readfile:
    info = pickle.load(readfile)
print(info)

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+?:><}{[]~`"
len_password = int (input("enter number of letters in password:"))

password = "".join(random.sample(s,len_password))
print(password)

answer = input("would you like to keep this password?")

if("yes" in answer):
    account_name = input("enter account name:")
    info[account_name] = password
    with open("game.asdasd","bw") as filewrite:
        pickle.dump(info,filewrite,protocol=2)

else:
    print("ok")
