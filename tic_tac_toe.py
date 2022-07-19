board=['-','-','-','-','-','-','-','-','-']
def dis():
  print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
  print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
  print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
def check(board):
    p1="x"
    p2="o"
    if board[0]==board[1]==board[2]==p1 or board[0]==board[1]==board[2]==p2:return True
    elif board[3]==board[4]==board[5]==p1 or board[3]==board[4]==board[5]==p2 :return True
    elif  board[6] == board[7] == board[8] ==p1 or board[6] == board[7] == board[8] ==p2 :return True
    elif  board[0] == board[3] == board[6]== p1 or board[0] == board[3] == board[6]== p2 :return True
    elif   board[0] == board[3] == board[6]==p1 or  board[0] == board[3] == board[6]==p2:return True
    elif   board[1] == board[4] == board[7]==p1 or board[1] == board[4] == board[7]==p2 :return True
    elif   board[2] == board[5] == board[8] ==p1 or board[2] == board[5] == board[8] ==p2 :return True
    elif board[0] == board[4] == board[8]==p1 or board[0] == board[4] == board[8]==p2:return True
    elif board[2] == board[4] == board[6]==p1 or board[2] == board[4] == board[6]==p2  :return True
    else: return False
def inp(board):
    x= int(input('enter position '))
    if board[x-1]!='-':
        print("already exist")
    else:
        return x
player1=input ("enter first player name")
player2=input ("enter second player name")
dis()
for i in range(9):
    if i%2==0:
        x=inp(board)
        board[x-1]='x'
        dis()
        if check(board):
          print('player {} win'.format(player1))
          break
    else:
        x = inp(board)
        board[x - 1] = 'o'
        dis()
        if check(board):
          print('player {} win'.format(player2))
          break
print("over")