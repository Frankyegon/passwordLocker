#!/usr/bin/env python3.8

import random
import pyperclip
from password import Details

def create_details(aname,uname,passw,email):
    '''
    Function to create a new user details
    '''
    new_details = Details(aname,uname,passw,email)
    return new_details

def save_details(details):
    '''
    Function to save user details
    '''
    details.save_details()   

def del_details(details):
    '''
    Function to delete a user details
    '''
    details.delete_details()

def find_details(account):
    '''
    Function that finds a user details by number and returns the user details
    '''
    return Details.find_by_account(account)

def check_existing_detailss(account):
    '''
    Function that check if a user details exists with that number and return a Boolean
    '''
    return Details.details_exist(account)

def display_details():
    '''
    Function that returns all the saved user detailss
    '''
    return Details.display_details()

def copy_email():
    '''
    Function that copies email of all the saved user detailss
    '''
    return Details.copy_email()

def main():
    print("Hello Welcome to your user details list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new user details, dc - display user detailss, fc -find a user details, copy - copy password, ex -exit the user details list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                        
                            print("New user details")
                            print("-"*10)

                            print ("Account name ....")
                            a_name = input()

                            print("User name ...")
                            u_name = input()

                            print("Password ...")

                            enter_pass = input("for password; enter type/generate:  ").lower()

                            if enter_pass == 'generate':

                                s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+?:><}{[]~`"
                                len_password = int (input("enter number of letters in password:"))
                                p_word = "".join(random.sample(s,len_password))

                            elif enter_pass == 'type':
                                p_word = input("type your password: ")
                            
                            else:
                                print("for password; either answer type or generate:  ")


                            print("Email address ...")
                            e_address = input()

                            save_details(create_details(a_name,u_name,p_word,e_address)) # create and save new user details.
                            print ('\n')
                            print(f"New Details {a_name} {u_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_details():
                                    print("Here is a list of all your user details")
                                    print('\n')

                                    for details in display_details():
                                            print(f"account name: {details.account_name}\n user name: {details.user_name}\n password:  {details.pass_word}\n email: {details.email}")
                            else:
                                    print('\n')
                                    print("You dont seem to have any user details saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the account name you want to search for")

                            search_account = input()
                            if check_existing_detailss(search_account):
                                    search_details = find_details(search_account)
                                    print(f"{search_details.account_name} {search_details.user_name}")
                                    print('-' * 20)

                                    print(f"Username: {search_details.user_name}")
                                    print(f"Password: {search_details.pass_word}")
                                    print(f"Email address:  {search_details.email}")

                                    pyperclip.copy(search_details.pass_word)
                                    #copy_email

                                    print(f"password has been copied")
                            else:
                                    print("That account name does not exist")

                    
                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
    
if __name__ == '__main__':

    main()