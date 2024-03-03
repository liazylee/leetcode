"""
@author:liazylee
@license: Apache Licence
@time: 03/03/2024 22:50
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
CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
SYMBOL_SET = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
CHARACTER_SET += SYMBOL_SET
import random


def generate_password(length: int) -> str:
    return ''.join(random.choices(CHARACTER_SET, k=length))


def generate_txt_file(file_name: str) -> None:
    with open(file_name, 'w') as f:
        for _ in range(10000000):
            f.write(generate_password(random.randint(8, 15)) + '\n')


generate_txt_file('password2.txt')
