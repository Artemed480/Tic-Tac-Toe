field = [["-"] * 3 for i in range(3)]

def hello():
   print("        |Крестики нолики|")
   print("       -------------------")
   print("        Формат ввода: x y ")
   print("          x - строка  ")
   print("          y - стобец ")

def board():
   print()
   print(f'             0 1 2')
   print(f'           0 {field[0][0]} {field[0][1]} {field[0][2]}')
   print(f'           1 {field[1][0]} {field[1][1]} {field[1][2]}')
   print(f'           2 {field[2][0]} {field[2][1]} {field[2][2]}')
   print()

def move():
   while True:
      go = input("         Ваш ход: ").split()
      if len(go) != 2:
         print("         Введите 2 координаты! ")
         continue
      x, y = go
      if not x.isdigit() or not y.isdigit():
         print("         Введите числа! ")
         continue
      x, y = int(x), int(y)
      if not(0 <= x <= 2) or not(0 <= y <= 2):
         print("         Координаты вне диапазона! ")
         continue
      if field[x][y] != "-":
         print("         Клетка занята! ")
         continue
      return x, y

def win():
   win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
   for comb in win_comb:
      opt = []
      for i in comb:
         opt.append(field[i[0]][i[1]])
         if opt == ['X', 'X', 'X']:
            print("         ----------")
            print("         Выиграл X!")
            print("         ----------")
            return True
         if opt == ['0', '0', '0']:
            print("         ----------")
            print("         Выиграл 0!")
            print("         ----------")
            return True
   return False

hello()
count = 0
while True:
   count += 1
   board()
   if count % 2 == 0:
      print("         Ходит нолик!")
   else:
      print("         Ходит крестик!")
   x, y = move()
   if count % 2 == 0:
      field[x][y] = "0"
   else:
      field[x][y] = "X"
   if win():
      break
   if count == 9:
      break
