from typing import List as l

input = [x.strip() for x in open('input.txt').readlines()]

class BingoBoard():
  def __init__(self, board: l[l[int]]):
    self.matrix = board

  def string_to_matrix(self, board: str) -> l[l[int]]:
    matrix = []
    rows = board.splitlines()
    for row in rows:
      matrix.append([int(col) for col in row.split()])
    return matrix

  def check_board(self, nums: l[int]):
    # check cols
    if any([all([self.matrix[x][i] in nums for i in range(5)]) for x in range(5)]):
      return True
    # check rows
    if any([all([self.matrix[i][x] in nums for i in range(5)]) for x in range(5)]):
      return True
    return False

class BingoGame:
  def __init__(self, rng: l[int], boards: l[BingoBoard]):
    self.rng = rng
    self.nums = []
    self.boards = boards
  
  def add_board(self, board: BingoBoard):
    self.boards.append(board)

  def advance_nums(self):
    self.nums.append(self.rng.pop(0))

  def check_boards(self):
    for board in self.boards:
      if board.check_board(self.nums):
        return board
    return None

game = BingoGame([int(x) for x in input[0].split(',')], [])

raw_boards = []
this_board = []
for line in input[2:]:
  if line == '':
    raw_boards.append(this_board)
    this_board = []
    continue
  this_board.append([int(col) for col in line.split()])
# fix to include final board in list
# could probably be more elegantly fixed but whatever
raw_boards.append(this_board)

print(f'There are {len(raw_boards)} boards.')
for board in raw_boards:
  board2 = BingoBoard(board)
  game.add_board(board2)

while True:
  game.advance_nums()
  winning = game.check_boards()
  if winning:
    sum_of_unmarked = sum([x for row in winning.matrix for x in row if x not in game.nums])
    most_recent_num = game.nums[-1]
    print(winning.matrix)
    print(game.nums)
    print(f'{sum_of_unmarked=} * {most_recent_num=} = {sum_of_unmarked * most_recent_num}')
    break