from unittest import TestCase
from Using_LIst import operation_on_list, my_list


class TestListOperation(TestCase):
    def test_operation_on_list(self):
        test_list = [33, 42.23, 0, 3, 100, True, 'string']
        result = operation_on_list(my_list)
        self.assertListEqual(result, [33, 42.23, 0, 100, True, 'string'])

    def test_my_list(self):
        test_list = ['Mary', 'had', 'a', 'little', 'lamb']
        result = my_list(test_list)
        self.assertListEqual(result,['Mary', 'had', 'a', 'ram'])


if __name__ == '__main__':
    unittest.main()

