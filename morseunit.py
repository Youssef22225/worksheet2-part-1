import unittest
import morse

class TestMorse(unittest.TestCase):
    def test_encode_us_word(self):
        self.assertEqual(morse.encode('us'), '..- ...')

    def test_encode_us_word_fail(self):
        self.assertNotEquals(morse.encode('us'), '..-')

    def test_encode_msg(self):
        self.assertEqual(morse.encode('u s'), '..- / ...')

    def test_encode_msg_hello_world(self):
        self.assertEqual(morse.encode('hello world'), '.... . .-.. .-.. --- / .-- --- .-. .-.. -..')

    def test_encode_msg_symbol(self):
        self.assertEqual(morse.encode('us ?'), '..- ... / ..--.')    
        
    def test_decode_us_word(self):
        self.assertEqual(morse.decode('..- ...'), 'us')

    def test_decode_us_word_fail(self):
        self.assertNotEquals(morse.decode('..-'), 'us')

    def test_decode_msg(self):
        self.assertEqual(morse.decode('..- / ...'), 'u s')

    def test_decode_msg_hello_world(self):
        self.assertEqual(morse.decode('.... . .-.. .-.. --- / .-- --- .-. .-.. -..'), 'hello world')

    def test_decode_msg_symbol(self):
        self.assertEqual(morse.decode('..- ... / ..--.'), 'us ?')  


if __name__ == '__main__':
    unittest.main()