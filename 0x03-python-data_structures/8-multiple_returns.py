#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        Len = (0, None)
    else:
        Len = len(sentence), sentence[0]
    return Len
