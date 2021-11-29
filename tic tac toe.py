# welcome message
print("""welcome to tic tac toe!
type the coordinates in this form : 'xy'
for example : 12 
the first coordinate represents the horizontal coordinate and the second represents the vertical one.
enjoy :)""")

# the matrix of the game

row = [[' ','1','2','3'],
         ['1',' ',' ',' '],
         ['2',' ',' ',' '],
         ['3', ' ',' ',' ']]

# the first display of the game table...

display = row[0][0] + '|' + row[0][1] + '|' + row[0][2] + '|' + row[0][3] + '|' + '\n' + row[1][0] + '|' + row[1][1] + '|' + row[1][2] + '|' + row[1][3] + '|' + '\n' + row[2][0] + '|' + row[2][1] + '|' + row[2][2] + '|' + row[2][3] + '|' + '\n' + row[3][0] + '|' + row[3][1] + '|' + row[3][2] + '|' + row[3][3] + '|' + '\n'
print('\n',display)

# there is only 9 possible moves in this game... so i made a loop that itterates 9 times only...

for i in range(0,9):
   # I check whose player's turn by checking the remainder of the order of the turn when we divide by the number of players(which is 2)...if it's 0 then it's player one's turn ,else it's player two's turn...
   if i % 2 == 0:
      print("player one's turn (x)")
      con = True
      while con:
         try:
            sel = input('input the coordinates: ' + '\n')
            if len(sel) == 2:
                sel,sel[0],sel[1] = list(sel),int(sel[0]),int(sel[1])
                if row[sel[0]][sel[1]] == 'x' or row[sel[0]][sel[1]] == 'o':
                    print('this square is full, select an empty square...' + '\n',display)
                else:
                    row[sel[0]][sel[1]] = 'x'
                    con = False
            else:
                print('input the coordinates in the following form: "xy" as x,y are postives integers...' + '\n')
            sel = ''

         except IndexError:
            print('reinput valid coordinates...' + '\n',display)
            sel = ''
   else:
      print("player two's turn (o)")
      con = True
      while con:
         try:
            sel = input('input the coordinates: ' + '\n')
            if len(sel) == 2:
                sel,sel[0],sel[1] = list(sel),int(sel[0]),int(sel[1])
                if row[sel[0]][sel[1]] == 'x' or row[sel[0]][sel[1]] == 'o':
                    print('this square is full, select an empty square...' + '\n' + '\n',display)
                else:
                    row[sel[0]][sel[1]] = 'o'
                    con = False
            else:
                print('input the coordinates in the following form: "xy" as x,y are postives integers...' + '\n' + '\n',display)
            sel = ''
         except IndexError:
            print('reinput valid coordinates...' + '\n' + '\n',display)
            sel = ''
   display = row[0][0] + '|' + row[0][1] + '|' + row[0][2] + '|' + row[0][3] + '|' + '\n' + row[1][0] + '|' + row[1][1] + '|' + row[1][2] + '|' + row[1][3] + '|' + '\n' + row[2][0] + '|' + row[2][1] + '|' + row[2][2] + '|' + row[2][3] + '|' + '\n' + row[3][0] + '|' + row[3][1] + '|' + row[3][2] + '|' + row[3][3] + '|' + '\n'
   print('\n',display)

   # diagonal check
   if row[1][1] == row[2][2] and row[2][2] == row[3][3] and  'x' == row[2][2]:
      print('player one is the winner!')
      exit()
   elif row[1][1] == row[2][2] and row[2][2] == row[3][3] and  'o' == row[2][2]:
      print('player two is the winner!')
      exit()
   elif row[1][3] == row[2][2] and row[2][2] == row[3][1] and  'x' == row[2][2]:
      print('player one is the winner!')
      exit()
   elif row[1][3] == row[2][2] and row[2][2] == row[3][1] and  'o' == row[2][2]:
      print('player two is the winner!')
      exit()

   # rows check
   for i in range(1,4):
      if row[i][1] == row[i][2] and row[i][1] == row[i][3] and 'x' == row[i][1]:
         print('player one is the winner!')
         exit()
      elif row[i][1] == row[i][2] and row[i][1] == row[i][3] and 'o' == row[i][1]:
         print('player two is the winner!')
         exit()
   for i in range(1,4):
      if row[1][i] == row[2][i] and row[1][i] == row[3][i] and 'x' == row[1][i]:
         print('player one is the winner!')
         exit()
      elif row[1][i] == row[2][i] and row[1][i] == row[3][i] and 'o' == row[1][i]:
         print('player two is the winner!')
         exit()
