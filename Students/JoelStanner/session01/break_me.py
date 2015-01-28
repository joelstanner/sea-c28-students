"""
Write 4 functions to throw NameError, TypeError, SyntaxError, AttributeError
"""

def badName():
    a = noSuchThing
    return a

badName()

def badType():
    b = "42"
    return b / 3

badType()

def badSyntax():
    returnz somstuff

badSyntax()

def badAttribute():
    abcd = "SPAM"
    return

badAttribute.abcde
