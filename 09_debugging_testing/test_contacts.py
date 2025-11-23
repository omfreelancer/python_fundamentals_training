import unittest
from mini_debug_contact_book import validate_phone, add_contact, search_contact, remove_contact

class TestValidate(unittest.TestCase):
    def test_validate_phone_true(self):
        self.assertTrue(validate_phone("12345678"))
    
    def test_validate_phone_emptyinput(self):
        self.assertFalse(validate_phone(""))

    def test_validate_phone_more_than_8(self):
        self.assertFalse(validate_phone("123456789"))

    def test_validate_phone_less_than_8(self):
        self.assertFalse(validate_phone("1234"),)

    def test_validate_phone_letters_input(self):
        self.assertFalse(validate_phone("123ah23"))

    def test_validate_phone_symbols_input(self):
        self.assertFalse(validate_phone("12?-12@"))

class TestAdd(unittest.TestCase):
   
    def test_add_contact_success(self):
        contacts = [
    {"name": "Ali", "phone": "+21212345678"}
]
        self.assertTrue(add_contact(contacts,"Molay","87654321"))
        self.assertEqual(len(contacts),2)
        self.assertEqual(contacts[1]["name"],"Molay")
        self.assertEqual(contacts[1]["phone"],"+21287654321")
        self.assertNotIn("email",contacts[1])

    def test_add_contact_duplicate(self):
        contacts = [
    {"name": "Ali", "phone": "+21212345678"}
]
        self.assertFalse(add_contact(contacts,"Ali","21345678"))
        self.assertEqual(len(contacts),1)
        self.assertEqual(contacts[0]["name"],"Ali")
        self.assertEqual(contacts[0]["phone"],"+21212345678")

class TestSearch(unittest.TestCase):

    def test_search_contact_exact_match(self):
        contacts = [
    {"name": "Ali", "phone": "+21212345678"},
    {"name": "Sara", "phone": "+21287654321"}
]

        result = search_contact(contacts, "Ali")
        self.assertIsInstance(result,list)
        self.assertEqual(len(result),1)
        self.assertEqual(result[0]["name"], "Ali")

    def test_search_contact_partial_match(self):
        contacts = [
    {"name": "Ali", "phone": "+21212345678"},
    {"name": "Sara", "phone": "+21287654321"}
]
        result = search_contact(contacts, "A")
        self.assertEqual(len(result), 2)

class TestRemove(unittest.TestCase):
    
    def test_remove_contact_success(self):
        contacts = [
    {"name": "Ali", "phone": "+21212345678"},
    {"name": "Sara", "phone": "+21287654321"}
]
        
        result = remove_contact(contacts, "Ali")

        self.assertTrue(result)
        self.assertEqual(len(contacts),1)
        self.assertEqual(contacts[0]["name"],"Sara")
    
    def test_remove_contact_not_found(self):
        contacts = [
    {"name": "Ali", "phone": "+21212345678"},
    {"name": "Sara", "phone": "+21287654321"}
]

        result = remove_contact(contacts, "karim")

        self.assertFalse(result)
        self.assertEqual(len(contacts), 2)
        self.assertEqual(contacts[0]["name"], "Ali")
        self.assertEqual(contacts[1]["name"], "Sara")

if __name__ == "__main__":
    unittest.main()