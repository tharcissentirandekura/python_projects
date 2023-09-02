def const_board(board):
  print("Current state of the board!\n")
  for i in range(0,9):
    if (i > 0) and (i % 3 == 0):
      print("\n")
    if board[i] == 0:
      print("-",end="  ")
    if board[i] == -1:
      print("0", end = "  ")
    if board[i] ==1:
      print("X", end="  ")
  print("\n")
  return board

def user1_turn(board):
  pos = int(input("Enter X's position between (1,9):"))
  if board[pos - 1] != 0:
    print("here:",board[pos - 1])
    print("wrong move!")
    exit(0)
  board[pos - 1] = -1
def user2_turn(board):
  pos = int(input("Enter X's position between (1,9):"))
  if board[pos - 1] != 0:
    print("wrong move!")
    exit(0)
  board[pos - 1] = 1

def minmax(board, player):
  win_state = analyze_board(board)
  if win_state != 0:
    return win_state * player  
  best_move = -2
  for i in range(0,9):
    if board[i] == 0:
      board[i] = player
      score = -minmax(board, player * -1)  
      board[i] = 0
      best_move = max(best_move, score)
  return best_move

def computer_turn(board, player): 
  best_move = -2
  best_pos = -1
  for i in range(0,9):
    if board[i] == 0:
      board[i] = player
      score = -minmax(board, player * -1)  
      board[i] = 0
      if score > best_move:
        best_move = score
        best_pos = i
  return best_pos


def analyze_board(board):
  current_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
  for i in range(0,8):
    if (board[current_board[i][0]] != 0 and 
        board[current_board[i][0]] == board[current_board[i][1]] and 
        board[current_board[i][1]] == board[current_board[i][2]]):
      return board[current_board[i][0]] # 0 or one has won the game
  return 0 # in the case no body is winning



def main():
  choice = int(input("Enter 1 for single player or 2 for multi player:"))
  board = [0]*9
  if choice ==1:#play as single
    print("Computer:0 Vs you:X")
    player = int(input("enter to play first or second:"))
    for i in range(0,9):
      if analyze_board(board) != 0:
        break
      if i + player % 2 == 0:#computer turn, use a computer function
        computer_turn(board,player)
        user2_turn(board)
        const_board(board)
      else:
        const_board(board)# for the user to see the board
        user1_turn(board)
  else:
    for i in range(0,9):
      if analyze_board(board) != 0:
        break
      if i % 2 == 0:
        const_board(board)# for the user to see the board
        user1_turn(board)
      else:
        const_board(board)# for the user to see the board
        user2_turn(board)



  win_state = analyze_board(board)
  print("here:",win_state)
    # claim the winner of the game!
  if win_state == 0:
    const_board(board)
    print("Draw!")
  if win_state == 1:
    const_board(board)
    print("player O won, X lost!!")
  if win_state == -1:
    const_board(board)
    print("Player X won, O lost!!")
main()




