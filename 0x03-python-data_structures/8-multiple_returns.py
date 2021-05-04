!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
        if len(i) == 0:
            return (0, None)
    return (i, sentence[0])
