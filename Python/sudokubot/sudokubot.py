#Sudoku bot work by trying every posible compination until it get it right (minisudoku 6x6)

def find_next_empty(puzzle):
   # finds in table empty place (0) place if there is none left return None,None
   for r in range(6):
      for c in range(6):
         if puzzle[r][c] == -1:
            return r, c
   
   return None,None

def is_valid(puzzle, guess, row, col):
   #checks if whether guess is valid. Return  true if is valid, False otherwise
    row_vals = puzzle[row]
    if guess in row_vals:
       return False
    
    col_vals = [puzzle[i][col] for i in range(6)]
    if guess in col_vals:
        return False
       
    # and then the square
    row_start = (row // 2) * 2
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 2):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
   
   # 1. make guess somewhere in puzzle 
   row, col = find_next_empty(puzzle)

  #2. if table is full, theen it is done
   if row is None:
    return True
   
  # if there is place put number bot guess between 1...6
   for guess in range (1,7):
      # 3. check if guess is valid
      if is_valid(puzzle, guess, row, col):
          puzzle[row][col] = guess
            # 4. then we recursively call our solver!
          if solve_sudoku(puzzle):
              return True
        
        # 5. it not valid or if nothing gets returned true, then we need to backtrack and try a new number
      puzzle[row][col] = -1

   # 6. if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
   return False

if __name__ == '__main__':
    example_board = [
        [-1, 2, 1,   3, 4, -1],
        [-1, 4, -1,   -1, -1, -1],

        [-1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   5, -1, -1],

        [-1, -1, -1,   -1, 3, -1],
        [-1, 3, 2,   4, 1, -1]
    ]

    print(solve_sudoku(example_board))
    print(example_board)
