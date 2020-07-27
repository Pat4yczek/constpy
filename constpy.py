import math

_const = {}
_const['pi'] = math.pi
_const['e'] = math.pi

def get(key):
    return _const[key]

def set(dictonary):
    for key, item in dictonary:
        _const[key] = item

