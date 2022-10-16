"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

from sys import exit

def calc(list_of_symbols=list()):
  if not list_of_symbols:
    list_of_symbols.append(input('Введите операцию (+, -, *, / или 0 для выхода): '))
    calc(list_of_symbols)
  elif len(list_of_symbols) == 1:
    if list_of_symbols[0] == '0':
      exit()
    elif list_of_symbols[0] in ['+', '-', '/', '*']:
      list_of_symbols.append(input('Введите первое число: '))
      calc(list_of_symbols)
    else:
      list_of_symbols[0] = input(f'Вместо нужного символа Вы ввели "{list_of_symbols[0]}". Исправьтесь: ')
      calc(list_of_symbols)
  elif len(list_of_symbols) == 2:
    if list_of_symbols[1].isdigit():
      list_of_symbols.append(input('Введите второе число: '))
      calc(list_of_symbols)
    else:
      list_of_symbols[1] = input(f'Вместо числа Вы ввели "{list_of_symbols[1]}". Исправьтесь: ')
      calc(list_of_symbols)
  else:
    if list_of_symbols[2].isdigit():
      if list_of_symbols[0] != '/':
        result = int(list_of_symbols[1])*int(list_of_symbols[2]) if list_of_symbols[0] == '*' else int(list_of_symbols[1])+int(list_of_symbols[2]) if list_of_symbols[0] == '+' else int(list_of_symbols[1])-int(list_of_symbols[2])
        print(f'Результат: {result}')
      else:
        if int(list_of_symbols[2]) != 0:
          result = int(list_of_symbols[1])/int(list_of_symbols[2])
          print(f'Результат: {result}')
        else:
          print('На ноль делить нельзя')
      list_of_symbols.clear()
      calc(list_of_symbols)
    else:
      list_of_symbols[2] = input(f'Вместо числа Вы ввели "{list_of_symbols[2]}". Исправьтесь: ')
      calc(list_of_symbols)
      
      
if __name__ == '__main__':
  calc()
