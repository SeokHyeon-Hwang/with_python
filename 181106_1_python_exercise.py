# -*- coding: utf-8 -*-
"""[황석현]의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vnVHiJZnbhlODnY29c8g1VbPf45SUZ81
"""

### 문자열

'Hello World'

### 여러줄 입력

'''
hello
I'm a teacher
'''

food = 'My name is seokhyeon'

print(food)

food = ' My name is seokhyeon.\nYour name is yoko. '
print(food)

food = ' My name is seokhyeon.\tYour name is yoko. '
print(food)

food = ' My name is seokhyeon.\t"Your name is yoko."" '
print(food)

food = ' My name is seokhyeon.\t\'Your name is yoko.\' '
print(food)

### 문자열 연산
head='python'
tail =' is fun!'
print(head+tail)

print(head*10)

print((head+' ')*5)

### 문자열 인덱싱, 슬라이싱
a='Life is too short, you need python'
print(a[2])

print(a[8:11])

a='20010331Rainy'
date=a[:8]
weather=a[8:]
print(date, weather)
print('%s %s' % (date, weather))

# 서식 문자
# %s : 문자열
# %c : 문자 1개
# %d : 정수(integer)
# %f : 실수(float)
# %o : 8진수
# %x : 16진수

a='i am '
b='a boy'
print('%s%s' % (a,b))

# 열칸확보 후 오른쪽 왼쪽 정렬
print('%10s|||%-10d' % ('11111', 52222))

print('i eat %d apples' % 3)
print('i eat {} apples'.format(3))
print('i eat {1} {1} apples'.format(3,5))
print('i eat {} {} apples'.format(3,5))

print('i eat {0:10} apples'.format(3,5))

# 10칸 찍되 소수점 2째자리까지 표현
print('i eat {0:10.2f} apples'.format(3.511))

# 문자열 개수 세기
a='hobby'
print(a.count('b'))
print(len(a))

# 문자열 삽입(문자열에 문자 하나당 ',' 삽입)
a=','
a.join('abcd')

a='hi'
a.upper()

a=' hi '
a.strip()

### 문자열 나누기
a='Life is too short'
a.split(' ')
a.split()

a='Life,is,too,short'
a.split(',')

# 07
a='Life is too short, you need python'
a.index('short')

# 08
q='a:b:c:d'
q.replace(':', '#')

# 09
q='a:b:c:d'
w=q.split(':')
'#'.join(w)

