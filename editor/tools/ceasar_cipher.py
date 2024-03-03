"""
@author:liazylee
@license: Apache Licence
@time: 19/02/2024 15:00
@contact: li233111@gmail.com
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# shift 9 length of alphabet
shift = 9
shift_dict = {}
for i in range(26):
    shift_dict[chr(97 + (i + shift) % 26)] = chr(97 + i)
    shift_dict[chr(65 + (i + shift) % 26)] = chr(65 + i)

print(shift_dict)


def caesar_cipher(s: str) -> str:
    return ''.join([shift_dict[c] if c.isalpha() else c for c in s])


print(caesar_cipher(
    'cqnan xwln fjb j ljc wjvnm vjc fqx fxan j orwn kxfuna qjc qn bcadcb mxfw cqn ujwn frcq j anpju anoajrw'
    'lqjbqrwp vrln jwm jexrmrwp cqn ajc'))

monoalphabetic_str = 'yqderboxphvftsgzamlcjuwink'
monoalphabetic_dict = {}
for i in range(26):
    monoalphabetic_dict[monoalphabetic_str[i]] = chr(97 + i)
    monoalphabetic_dict[monoalphabetic_str[i].upper()] = chr(65 + i)
print(monoalphabetic_dict)


def monoalphabetic_cipher(s: str) -> str:
    return ''.join([monoalphabetic_dict[c] if c.isalpha() else c for c in s])


print(monoalphabetic_cipher('y fgso cptr yog, ps y oyfyin bym, bym ywyn...'
                            'pc pl y eymv cptr bgm cxr mrqrffpgs.'))


def homophonic_substitution_cipher(s: str) -> str:
    pass
