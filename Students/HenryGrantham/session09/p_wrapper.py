# -*- coding: utf-8 -*-


def p_wrapper(func):
    """Wraps original output in an HTML 'p' tag
    """
    def wrapped(text):
        beg_str = u"<p> "
        end_str = u" </p>"
        result = u"{}{}{}".format(beg_str, func(text), end_str)
        return result
    return wrapped


@p_wrapper
def return_a_string(string):
    """Returns a string
    """
    print string
    return string
