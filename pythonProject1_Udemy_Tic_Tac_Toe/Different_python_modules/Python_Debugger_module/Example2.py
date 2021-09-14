import os
import pdb


def get_path(filename):
    """Returns file path if no file then return empty string"""
    head, tail = os.path.split(filename)
    pdb.set_trace()
    return head


# filename = 'C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\Python_Debugger_module\\Example1.py'
filename = __file__
print(f"path={get_path(filename)}")
