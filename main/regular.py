import random
def ve_code():
    _code = ''
    for i in range(4):
        a = random.randrange(48,58)
        b = random.randrange(65,91)
        c = random.randrange(97,123)
        random_num = random.choice([a,b,c])
        _code += chr(random_num)
    return _code
print(ve_code())
