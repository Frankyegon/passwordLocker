import unittest # Importing the unittest module
import pyperclip
from password import Details # Importing the user details class

class TestDetails(unittest.TestCase):

    '''
    Test class that defines test cases for the user details class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_details = Details("Frankyegon","twitter","password","james@ms.com") # create user details object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_details.account_name,"James")
        self.assertEqual(self.new_details.user_name,"Muriuki")
        self.assertEqual(self.new_details.pass_word,"0712345678")
        self.assertEqual(self.new_details.email,"james@ms.com")

    def test_save_details(self):
        '''
        test_save_user details test case to test if the user details object is saved into
         the user details list
        '''
        self.new_details.save_details() # saving the new user details
        self.assertEqual(len(Details.details_list),1)

# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Details.details_list = []


    def test_save_multiple_details(self):
            '''
            test_save_multiple_user details to check if we can save multiple user details
            objects to our user details_list
            '''
            self.new_details.save_details()
            test_details = Details("Test","user","0712345678","test@user.com") # new user details
            test_details.save_details()
            self.assertEqual(len(Details.details_list),2)

    # More tests above
    def test_delete_details(self):
            '''
            test_delete_user details to test if we can remove a user details from our user details list
            '''
            self.new_details.save_details()
            test_details = Details("Test","user","0712345678","test@user.com") # new user details
            test_details.save_details()

            self.new_details.delete_details()# Deleting a user details object
            self.assertEqual(len(Details.details_list),1)

    def test_find_details_by_number(self):
        '''
        test to check if we can find a user details by phone number and display information
        '''

        self.new_details.save_details()
        test_details = Details("Test","user","0711223344","test@user.com") # new user details
        test_details.save_details()

        found_details = Details.find_by_number("0711223344")

        self.assertEqual(found_details.email,test_details.email)

    def test_details_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user details.
        '''

        self.new_details.save_details()
        test_details = Details("Test","user","0711223344","test@user.com") # new user details
        test_details.save_details()

        details_exists = Details.details_exist("0711223344")

        self.assertTrue(details_exists)

    def test_display_all_details(self):
        '''
        method that returns a list of all user detailss saved
        '''

        self.assertEqual(Details.display_details(),Details.details_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user details
        '''

        self.new_details.save_details()
        Details.copy_email("0712345678")

        self.assertEqual(self.new_details.email,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()