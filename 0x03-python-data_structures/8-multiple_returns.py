#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    Len = len(sentence)
    first = sentence[0]
    return (Len, first)
