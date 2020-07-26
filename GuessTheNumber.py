'''Game : Guess the number between 1 to 20

User to input any number between 1 to 20 and
if the number is equal to the number generated
by computer then user wins. If he does not input
any number or consumes tries then he loses
and quits the program.
'''
#Below is the code of the program
import sys, random #random module to generate random number
print('Game to guess the number from 1 to 20')
tries = int(input("please enter number of tries : ") or 0)
CompNum = random.randint(1, 20)#randint(<start>, <end>) generates random number in given range
GuessNum = 0
cnt = 1 #counter for user tries
if tries > 0:
      while GuessNum != CompNum and cnt <= tries:
            cnt += 1
            GuessNum = int(input("Try number 1 to 20 to play or 0 to quit: ") or 0)
            if GuessNum < 0 or GuessNum > 20:
                  print('Sorry, out of range 1-20')
            elif GuessNum == 0:
                  print('You looser, quitting!')
                  sys.exit()
else:
      print('Tries must be a positive number!')
      sys.exit()
if GuessNum == CompNum:
      print('Congrats, you win')
else:
      print('You tried your best, keep spirit up!')
print('Thanks for playing')
