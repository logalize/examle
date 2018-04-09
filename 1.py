#weekly task's
#math
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c)/2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)

#comparing
# a = int(input())
# if a <= 12 and a > -15 or a < 17 and a > 14 or a >= 19:
#     print(True)
# else:
#     print(False)

#calculator
# a = float(input())
# b = float(input())
# c = str(input())

# if c == '/' and b > 0:
#     print(a / b)
# elif c == '/' and b == 0:
#     print("Деление на 0!")

# if c == 'div' and b > 0:
#     print(a // b)
# elif c == 'div' and b == 0:
#     print("Деление на 0!")

# if c == 'mod' and b > 0:
#     print(a % b)
# elif c == 'mod' and b == 0:
#     print("Деление на 0!")

# if c == 'pow':
#     print(a ** b)

# if c == '+':
#     print(a + b)

# if c == '-':
#     print(a - b)

# if c == '*':
#     print(a * b)

#square
# pi = 3.14
# obj = str(input())
# if obj == 'треугольник':
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = float((a + b + c)/2)
#     S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
#     print(S)
# elif obj == 'прямоугольник':
#     a = float(input())
#     b = float(input())
#     S = float(a * b)
#     print(S)
# elif obj == 'круг':
#     r = float(input())
#     S = float(pi * (r**2))
#     print(S)

#maximum
# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c:
#     maxi = a
# elif b >= a and b >= c:
#     maxi = b
# elif c >= a and c >= b:
#     maxi = c

# if a <= b and a <= c:
#     mini = a
# elif b <= c and b <= a:
#     mini = b
# elif c <= b and c <= a:
#     mini = c

# if a <= b and a >= c or a <= c and a >= b:
#     mid = a
# elif b <= c and b >= a or b <=a and b >=c:
#     mid = b
# elif c <= a and c >= b or c <= b and c >= a:
#     mid = c

# print(maxi)
# print(mini)
# print(mid)


# # human count
# a = int(input())
# str1 = 'программист'
# str2 = 'программиста'
# str3 = 'программистов'
# b = list(str(a))

# if len(b) == 1 and int(b[0]) == 1:
#     print(str(a) + ' ' + str1)
# elif len(b) == 1 and 2 <= int(b[0]) <= 4:
#     print(str(a) + ' ' + str2)
# elif len(b) == 1 and int(b[0]) == 0 or len(b) == 1 and 5 <= int(b[0]) <= 9:
#     print(str(a) + ' ' + str3)

# if len(b) == 2 and int(b[1]) == 1 and a > 20:
#     print(str(a) + ' ' + str1)
# elif len(b) == 2 and 2 <= int(b[1]) <= 4 and a > 20:
#     print(str(a) + ' ' + str2)
# elif len(b) == 2 and int(b[1]) == 0 or len(b) == 2 and 5 <= int(b[1]) <= 9 or 11 <= a <= 14:
#     print(str(a) + ' ' + str3)

# if len(b) == 3 and int(b[2]) == 1 and int(b[1]) != int(b[2]):
#     print(str(a) + ' ' + str1)
# elif len(b) == 3 and 2 <= int(b[2]) <= 4 and ((b[1]) + (b[2])) != '12' and ((b[1]) + (b[2])) != '13' and ((b[1]) + (b[2])) != '14':
#     print(str(a) + ' ' + str2)
# elif len(b) == 3 and int(b[2]) == 0 or len(b) == 3 and 0 <= int(b[1]) <= 9 and 0 <= int(b[2]) <= 9 or a == 1000:
#     print(str(a) + ' ' + str3)

#ticket
# a = str(input())
# b = list(a)
# s1 = int(a[0]) + int(a[1]) + int(a[2])
# s2 = int(a[3]) + int(a[4]) + int(a[5])
# if s1 == s2:
#     print('Счастливый')
# else: print('Обычный')

# while sum
# s = 0
# i = 1
# while i > 0:
#   n = int(input())
#   if n == 0:
#     i = 0
#   else:
#     s += n
# print(s)

#while pie
# a = int(input())
# b = int(input())
# i = 2
# if a == 1 and b == 1:
#     print(int(1))
# else:
#     while i != 0:
#         if int(i % a) or int(i % b) != 0:
#             i += 1
#         else:
#             break
#     print(i)

# a = int(input())
# b = int(input())
# m = a*b
# while a != 0 and b != 0:
#     if a > b:
#         a %= b
#     else:
#         b %= a
# print(m // (a+b))

#while digit's
# i = 0
# while i >= 0:
#   i = int(input())
#   if i < 10:
#     continue
#   elif i > 100:
#     break
#   else:
#     print(i)

#for table
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print('', end='\t')
# for i in range(c, d+1):
#     print(i, end='\t')
# print()
# for j in range(a, b+1):
#     print(j, end = '\t')
#     for k in range(c, d+1):
#         print(j * k, end = '\t')
#     print()

#for arithmetic
# a = int(input())
# b = int(input())
# s = 0
# c = 0
# for i in range(a, b+1):
#     if i % 3 == 0:
#         s += i
#         c += 1
# print(s / c)

#GC
# st = str(input())
# st1 = st.upper()
# l = len(st1)
# c1 = st1.count('C')
# c2 = st1.count('G')
# su = (((c1 + c2) / l) * 100)
# print(su)

#Slice

#from Andrey V
# string = input(str())
# out = ''
# c =1
# t = string[0]

# for i in range(1, len(string)):
#     if t == string[i]:
#         c = c + 1
#         continue
#     out = out + t + str(c)
#     t = string[i]
#     c =1
# out = out + t + str(c)
# print(out)

#My
# l = input(str())
# i = 1
# j = 0
# s = 1
# tmp = ''
# if len(l) == 1:
#     tmp += l[len(l) - 1] + str(s)
#     print(tmp)    
#     exit()

# for a in range(len(l)):
#     while l[j] == l[i]:
#         s += 1
#         i += 1
#         if i >= len(l):
#             tmp += l[i-1] + str(s)
#             print(tmp)
#             exit()           
#     tmp += l[i-1] + str(s)
#     j += s
#     i += 1
#     if i >= len(l):
#         s = 1
#         tmp += l[i-1] + str(s)
#         print(tmp)
#         break
#     s = 1

# split and summ
# s = 0
# l = input(str())
# l1 = l.split(' ')
# for i in l1:
#     s += int(i)
# print(s)

#repeat
# l = input(str())
# b = l.split(' ')
# tmp = []
# tmp2 = ''
# for i in b:
#     if b.count(i) > 1:
#         if i in tmp:
#             continue
#         else:
#             tmp.append(i)
# for k in tmp:
#     tmp2 += k + ' '
# print(tmp2)

#sum two neighbors
# l = input(str())
# l1 = l.split(' ')
# index = 0
# s = ''
# dl = int(len(l1))

# for i in l1:
#     if int(len(l1) == 1):
#         s = l1[0]
#         print(str(s))
#         exit()
#     if int(len(l1) == 2):
#         s += str((int(l1[1]) + int(l1[1]))) + ' '
#         s += str((int(l1[0]) + int(l1[0])))
#         print(str(s))
#         exit()
#     if index == int(dl - 1):
#         s += str(((int(l1[index - 1]) + int(l1[0])))) + ' '
#         break
#     if index == 0:
#        s += str((int(l1[dl - 1]) + int(l1[index + 1]))) + ' '
#        index += 1
#        continue
#     s += str((int(l1[index - 1]) + int(l1[index + 1]))) + ' '
#     index += 1
#     continue
# print(s)

# sum of squares
# k = True
# s = 0
# sk = 0
# m = []
# while k == True:
#     l = input(str())
#     m.append(l)
#
#     for i in m:
#         s += int(i)
#         sk += int(i) ** 2
#     if s == 0:
#         k = False
#         print(sk)
#         break
#     else:
#         s = 0
#         sk = 0
#         continue
#
#sequence
# l = input()
# l1 = int(l)
# m = []
# dl = len(range(int(l)))
#
# for i in range(1, l1 + 1):
#     for k in range(i):
#         if len(m) > dl - 1:
#             break
#         else:
#             m.append(i)
# print(' '.join(map(str, m)))

#position
# l = input().split()
# k = input()
# j = 0
# tmp = []
# for i in l:
#     if str(k) == i:
#         tmp.append(j)
#         j += 1
#     else:
#         j += 1
#         continue
#
# if len(tmp) != 0:
#     print(' '.join(map(str, tmp)))

#f(x)
# def f(x):
#     if x <= -2:
#         x = 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         x = -( x / 2)
#     else:
#         x = (x - 2) ** 2 + 1
#     return x

#modify_list(l)
# def modify_list(lst):
#     tmp = []
#     for i in lst:
#         if i % 2 != 0:
#             tmp.append(i)
#     for n in tmp:
#         lst.remove(n)
#     tmp.clear()
#     for k in lst:
#         tmp.append(k // 2)
#     lst.clear()
#     lst.extend(tmp)
#     return lst

# def update_dictionary(d, key, value):
#
#     if key in d:
#         d[key].append(value)
#
#     if key not in d and 2 * key in d:
#         d[2 * key].append(value)
#
#     if key not in d and 2 * key not in d:
#         d[2 * key] = list()
#         d[2 * key].append(value)
#
# d = {}
# update_dictionary(d, 1, -1)
# print(d)
#
# update_dictionary(d, 2, -2)
# print(d)
#
# update_dictionary(d, 1, -3)
# print(d)

# Count duplicates of worbs
# sumline = []
# sumlinetemp = {}
# with open('input.txt') as inf:
#     for line in inf:
#         sumline += line.strip().lower().split()
#     for element in sumline:
#         if sumline.count(element) in sumlinetemp and element < str(sumlinetemp[sumline.count(element)]):
#             continue
#         else:
#             sumlinetemp[sumline.count(element)] = list()
#             sumlinetemp[sumline.count(element)].append(element)
# # print(sumline)
# print((str(sumlinetemp[max(sumlinetemp)])) + ' ' + str(max(sumlinetemp)))

# average score(mark)
# summ = 0
# ball = 0
# tmp = ''
# math = 0
# phis = 0
# rus = 0
# k = 0
# with open('input.txt') as inf:
#     for line in inf:
#         line = line.strip().split(';')
#         for i in range(1, len(line)):
#             summ += int(line[i])
#             if i == 1:
#                 math+=int(line[i])
#             elif i == 2:
#                 phis += int(line[i])
#             else:
#                 rus += int(line[i])
#         ball = summ/i
#         k += 1
#         print(ball)
#         summ = 0
#         ball = 0
# math = math/k
# phis = phis/k
# rus = rus/k
# print(math, phis, rus)

#module math
# from math import pi
# R = float(input())
# print((2 * pi)*R)

#module sys
# from sys import argv
# for i in range(1, len(argv)):
#     print(argv[i], end = ' ')

#external module requests
# import requests
# count = 0
# getfile = 'https://stepic.org/media/attachments/course67/3.6.2/314.txt'
# f = requests.get(getfile)
# f = f.text.strip()
# f = f.splitlines()
# for lines in f:
#     count += 1
# print(count)

# external module requests-2
# import requests
# getpath = 'https://stepic.org/media/attachments/course67/3.6.3/'
# getfile = '699991.txt'
# geturl = getpath + getfile
# i = 1
# while i:
#     geturl = getpath + getfile
#     f = requests.get(geturl)
#     getfile = f.text.strip()
#     if 'We' in f:
#         print(f.text.strip())
#         i = 0
#         exit()
#     else:
#         print(getfile)


#footbal count games
# games = input()
# game = {}
# j = 0
# commands = {}
#
# for i in range(1, int(games) + 1):
#     game[i] = (input().split(';'))
# #print(game)
#
#
# for i in game:
#
#     if game[i][j+1] > game[i][j+3]:
#         command = game[i][j]
#         if command in commands:
#             print()
#         else:
#             commands[command] = [0 for x in range(5)]
#         commands[command][4] += 3
#         commands[command][3] += 0
#         commands[command][2] += 0
#         commands[command][1] += 1
#         commands[command][0] += 1
#
#         command = game[i][j + 2]
#         if command in commands:
#             print()
#         else:
#             commands[command] = [0 for x in range(5)]
#
#         commands[command][4] += 0
#         commands[command][3] += 1
#         commands[command][2] += 0
#         commands[command][1] += 0
#         commands[command][0] += 1
#
#     if game[i][j + 1] < game[i][j + 3]:
#         command = game[i][j + 2]
#         if command in commands:
#             print()
#         else:
#             commands[command] = [0 for x in range(5)]
#         commands[command][4] += 3
#         commands[command][3] += 0
#         commands[command][2] += 0
#         commands[command][1] += 1
#         commands[command][0] += 1
#
#         command = game[i][j]
#         if command in commands:
#             print()
#         else:
#             commands[command] = [0 for x in range(5)]
#
#         commands[command][4] += 0
#         commands[command][3] += 1
#         commands[command][2] += 0
#         commands[command][1] += 0
#         commands[command][0] += 1
#
#
#     if game[i][j+1] == game[i][j+3]:
#         command = game[i][j]
#         if command in commands:
#             print()
#         else:
#             commands[command] = [0 for x in range(5)]
#         commands[command][4] += 1
#         commands[command][3] += 0
#         commands[command][2] += 1
#         commands[command][1] += 0
#         commands[command][0] += 1
#
#         command = game[i][j + 2]
#         if command in commands:
#             print()
#         else:
#             commands[command] = [0 for x in range(5)]
#         commands[command][4] += 1
#         commands[command][3] += 0
#         commands[command][2] += 1
#         commands[command][1] += 0
#         commands[command][0] += 1
#
# for key, value in commands.items():
#     print(key, end=': ')
#     for item in value:
#         print(item, end = ' ')
#     print()


#code encode
# seqin = input()
# code = input()
# seqout = input()
# seqout_enc = input()
# # print(list(seqin))
# # print(list(code))
# code_dict = dict(zip(code, seqin))
# encode_dict = dict(zip(seqin, code))
#
# for i in seqout:
#     print(encode_dict[i], end = '')
# print()
# for i in seqout_enc:
#     print(code_dict[i], end = '')


#dictionary system
# count_words = range(int(input()))
# # input_words = [ 'a', 'bb', 'cCc' ]
# input_words = ( input().lower() for x in count_words )
# dict_words = dict(zip(input_words, count_words))
# count_words = range(int(input()))
# input_wordsin = ' '.join((input().lower()) for x in count_words)
# #line1 = ['a', 'bb', 'aab', 'aba', 'ccc']
# #line2 = ['c', 'bb', 'aaa']
# mn = { n for n in input_wordsin.split() if n not in dict_words }
# # print(mn)
# for i in mn:
#   print(''.join(i))

# search coordinate point
# move_count = range(int(input()))
# move_dict = {}
# tmp = []
# x = 0
# y = 0
# for i in move_count:
#     tmp.append(input().split())
#     if tmp[i][0] in move_dict:
#         move_dict[tmp[i][0]] += int(tmp[i][1])
#     else:
#         move_dict[tmp[i][0]] = int(tmp[i][1])
# # m1 = 'север 10'
# # m2 = 'запад 20'
# # m3 = 'юг 30'
# # m3 = 'восток 40'
# # m4 = 'восток 40'
# for key in move_dict:
#     if key == 'запад':
#         x -= int(move_dict[key])
#     elif key == 'восток':
#         x += int(move_dict[key])
#     elif key == 'юг':
#         y -= int(move_dict[key])
#     elif key == 'север':
#         y += int(move_dict[key])
# # print(tmp)
# # print(move_dict)
# print(x,y)

#lenght of school students
# sumline = []
# classdict = {}
# cline = 0
# tmp = []
# with open('classin.txt') as inf:
#     for line in inf:
#         sumline = line.split()
#         # cline += 1
#         if int(sumline[0]) not in classdict:
#             classdict[int(sumline[0])] = list()
#             classdict[int(sumline[0])].append(int(sumline[2]))
#         else:
#             classdict[int(sumline[0])].append(int(sumline[2]))
#
#
# for i in range(1, int(max(classdict))):
#     if int(i) not in classdict:
#         classdict[int(i)] = '-'
#     else:
#         continue
#
# keylist = classdict.keys()
# # print(sorted(keylist))
# for key in sorted(keylist):
#     if '-' not in classdict[key]:
#         print(key, (sum(classdict[key]))/len(classdict[key]))
#     else:
#         print(str(key) + ' ' + '-')


# sum matrix
# m = []
# k = 0
# tmp = []
# t = 0
# while k != 'end':
#     for k in input().split():
#         if k != 'end':
#             m.append(k)
#         else:
#             break
#     if t == 0:
#         lk = len(m)
#         t += 1
#     else:
#         continue
# print(lk)
# print(m)

# z = []
# zz = [['9', '5', '3'], ['0', '7', '-1'], ['-5', '2', '9']]
# zzz = []
# i = 0
# # while i != 'end':
# #     i = input()
# #     if i != 'end':
# #         z.append(i)
# #     else:
# #         break
# # [ zz.append(i.split()) for i in z ]
# # print(len(zz[0]))
# print(zz)
# for i in range(len(zz)):
#     for j in range(len(zz[0])):
        # print(zz[i][j], end = '\n')
#         if i == 0 and j == 0:
#             zzz.append(int(zz[i][len(zz[0]) -1 ]) + int(zz[len(zz[0]) - 1][j]) + int(zz[i][j + 1]) + int(zz[i + 1][j]))
# print(zzz)
# print(len(zz[0]) -1)
# print(int(zz[0][len(zz[0]) -1 ]), int(zz[len(zz[0]) - 1][0]), int(zz[0][0 + 1]), int(zz[0 + 1][0]))



























