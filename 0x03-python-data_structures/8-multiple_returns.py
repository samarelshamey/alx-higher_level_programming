#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence = None
        return sentence[0]
    else:
        return (len(sentence), sentence[0])
