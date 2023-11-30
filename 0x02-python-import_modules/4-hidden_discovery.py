#!/usr/bin/python3
# 4-hidden_discovery.py
if __name__ == "__main__":
    '''4-hidden_discovery.py'''
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] != "__":
            print("{:s}".format(i))
