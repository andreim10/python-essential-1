#final project of python-essential-1
def display_board(board):
   for row in range(3):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    free_fields=[]
    for r in range(3):
        for g in range(3):
            if board[r][c] not in ['O', 'X']:
                free_fields.append((r, c))
    return free_fields


def make_list_of_free_fields(board):
   free_fields=make_list_of_free_fields(board)
   while True:
       try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Error: Please enter a number between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if (row, col) in free_fields:
                board[row][col] = 'O'
                break
            else:
                print("That square is already taken! Try another one.")
      except ValueError:
            print("Invalid input. Please enter an integer.")

def victory_for(board, sign):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == sign:
            return True
            
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == sign:
            return True
            
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
        
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        random_index = randrange(len(free_fields))
        row, col = free_fields[random_index]
        board[row][col] = 'X'

def play_game():
    
    board = [[3 * r + c + 1 for c in range(3)] for r in range(3)]
    board[1][1] = 'X'
    display_board(board)
    while True:
        
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("Congratulations! You won!")
            break
            
       
        if len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            break
            
        
        print("Computer is making its move...")
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("The computer wins! Better luck next time.")
            break
            
        
        if len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            break
if __name__ == "__main__":
    play_game()


if __name__ == "__main__":
    play_game()
