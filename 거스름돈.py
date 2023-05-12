# -*- coding: cp949 -*-
'''
n = 1260 
count = 0

# ū ������ ȭ����� ���ʴ�� Ȯ���ϱ�
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # �ش� ȭ��� �Ž��� �� �� �ִ� ������ ���� ����
    n %= coin

print(count)
'''

n = 1260 # 1260��
count =  0 # �ʱ� ī��Ʈ ���� 0

coin_types = [500, 100, 50, 10]

for type in coin_types:
    count = count + (n//type)
    n = n % type

# print(count)
print(count)
