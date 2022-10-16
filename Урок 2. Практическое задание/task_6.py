"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint

def find_answer(quest=randint(0,101), ticker=0):
  if ticker < 10:
    user_answer = int(input('Попробуйте ввести число: '))
    if user_answer == quest:
      print('You win!')
      return
    elif user_answer < quest:
      print('Загаданное число больше')
    else:
      print('Загаданное число меньше')
    ticker += 1
    find_answer(quest, ticker)
  else:
    print(f'You Lose! Find answer is {quest}')
    return  


if __name__ == '__main__':
  find_answer()

  
