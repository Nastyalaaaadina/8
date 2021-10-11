def neNol(a):
 if a > 0:
  return 1
 else:
  return 0
try:
 a = int(input('Ведите число: '))
 n = int(input ('Выбирите систему счисления, в которую хотите перевести число: '))
 while n != 2 and n != 8:
  print('Выберете 2-ую или 8-ую систему счисления')
  n = int(input())
 if n == 2:
  x = ''
  while neNol(a) == 1:
   x = str(a % 2) + x
   a = a // 2
   print(x)
 if n == 8:
  y = ''
 while neNol(a) == 1:
  y = str(a % 8) + y
  a = a // 8
  print(y)
except ValueError:
 print('Повторите попытку, вами было введено не число')