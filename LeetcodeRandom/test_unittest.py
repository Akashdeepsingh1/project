from LeetcodeRandom import unittest
from LeetcodeRandom.unittest import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook ()
        phonebook.add("bob", "12345")
        number = phonebook.lookup("bob")
        self.assertEqual("12345", number)



