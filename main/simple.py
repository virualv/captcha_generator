import random
def ve_code():
    _code = ''
    for i in range(4):
        _code += chr(random.choice([random.randrange(48,58),random.randrange(65,91),random.randrange(97,123)]))
    return _code
print(ve_code())
