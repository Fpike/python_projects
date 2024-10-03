'''
Take string as argument and return first 5 characters + '...' if string is longer than 5 characters.
e.g. Hello, world! --> Hello...
'''

'''
Test empty string
'''
from lib.make_snippet import make_snippet

def return_empty_string_if_none_set():
    actual = make_snippet('')
    expected = ''
    assert actual == expected