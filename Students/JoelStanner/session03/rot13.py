"""session03 task 2"""
from string import maketrans

trans_table = maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
)


def rot13(string):
    """Return a string encrypted with the ROT13 cypher."""
    return string.translate(trans_table)

if __name__ == '__main__':
    test_string = "Hello. I am a nifty test string"

    assert rot13(test_string) == "Uryyb. V nz n avsgl grfg fgevat"
    assert rot13("Uryyb. V nz n avsgl grfg fgevat") == test_string
    print("All tests pass.")
