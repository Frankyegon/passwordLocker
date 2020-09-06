import pyperclip

class Details: 
    """
    Class that generates new instances of user details.
    """

    details_list = [] # Empty user details list

     # Init method up here
    def save_details(self):

        '''
        save_user details method saves user details objects into user details_list
        '''

        Details.details_list.append(self)
        

    def delete_details(self):

        '''
        delete_user details method deletes a saved user details from the user details_list
        '''

        Details.details_list.remove(self)

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a account name and returns a user details that matches that account number.

        Args:
            account: Account name to search for
        Returns :
            user details of person that matches the account name.
        '''

        for details in cls.details_list:
            if details.account_name == account:
                return details

    @classmethod
    def details_exist(cls,account):
        '''
        Method that checks if a user details exists from the user details list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user details exists
        '''
        for details in cls.details_list:
            if details.account_name == account:
                    return True

        return False

    @classmethod
    def display_details(cls):
        '''
        method that returns the user details list
        '''
        return cls.details_list

    @classmethod
    def copy_email(cls,email):
        details_found = Details.find_by_account(account)
        pyperclip.copy(details_found.email)

    def __init__(self,account_name,user_name,password,email):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.pass_word = password
        self.email = email


