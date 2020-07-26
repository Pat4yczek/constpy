import math

class ConstPy:
    _const = {
        'pi': math.pi,
        'e': math.e
    }

    def get(self, key):
        return self._const[key]

    def set(self, dict):
        for key, item in dict:
            self._const[key] = item

if __name__ == '__main__':
    pass