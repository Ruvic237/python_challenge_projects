from Exeption import cap
import unittest 

class TestCap(unittest.TestCase):
    
    def test_one(self):
        text = 'python'
        result = cap(text)
        self.assertEqual(result,'Python')
    
    def test_two(self):
        text = 'john reper'
        result = cap(text)
        self.assertEqual(result,'John Reper')
            
if __name__ == '__main__':
    unittest.main()
    
                