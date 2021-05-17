#!/usr/bin/python3
def def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except:
        raise
