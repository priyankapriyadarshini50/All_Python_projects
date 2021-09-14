import unittest
import Caesar_Cipher_prog  # The module


class TestCaesarMethod(unittest.TestCase):
    def test_update_cipher_msg(self):
        result = Caesar_Cipher_prog.update_cipher_msg('abcde')
        self.assertEqual(result, 'BCDEF')
        # using context manager
        # with self.assertRaises(TypeError):
            # Caesar_Cipher_prog.update_cipher_msg('1234')

    def test_decrypt_msg(self):
        self.assertEqual(Caesar_Cipher_prog.decrypt_msg('BCDEF'), 'ABCDE')


if __name__ == '__main__':
    unittest.main()
