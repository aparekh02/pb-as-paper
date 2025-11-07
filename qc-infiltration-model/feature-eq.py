import math

def soiltypehmi(x):
    """y = -exp(-x) + 1"""
    return -math.exp(-x) + 1

def runoffhmi(x):
    """y = exp(-256*10/x)"""
    return math.exp(-256 * 10 / x)

def pHPbhmi(x):
    """y = 1/(1+exp(x-3))"""
    return 1 / (1 + math.exp(x - 3))

def pHAshmi(x):
    """y = (1/1000)(x*5)/(1+x*5)"""
    return (1/1000) * (x * 5) / (1 + x * 5)