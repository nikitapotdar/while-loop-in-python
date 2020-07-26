'''Program to demonstrate While Loop

User has to input a positive number until which
program will print all the even numbers
starting the range from 0
'''
import sys
print('Program to print even numbers in positive range')
cnt = 0
lim = int(input('input positive number to set range : ') or 0)
if lim < 0:
      print('negative range is not allowed')
      sys.exit()
while cnt <= lim:
      if cnt%2 == 0:
            print(cnt, 'is an even number')
      cnt += 1
print('All even numbers up to', lim)
            
