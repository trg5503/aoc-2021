# NOTE: *somewhere* in this code, horizontal and vertical are being flipped
#       which is causing the board to be represented rotated by 90 degrees
#       I have no clue where this is but I don't really care to look because
#       it doesn't really break any functionality or anything
#       The solution is also *incredibly* inefficient but I really don't care
#       about that one either

input = [x.strip() for x in open('input.txt').readlines()]

class Line:
  def __init__(self, data: str):
    # yes I'm a professional programmer and 100% know what I'm doing
    self.points = [(int(x), int(y)) for x, y in [x.split(',') for x in data.split(' -> ')]]
  
  def is_at_point(self, x: int, y: int):
    # algorithm who???
    x1, y1 = self.points[0]
    x2, y2 = self.points[1]
    # determine which direction the line is pointing - this will *definitely* not work for part 2
    if x1 == x2:
      return x == x1 and y >= min(y1, y2) and y <= max(y1, y2)
    elif y1 == y2:
      return y == y1 and x >= min(x1, x2) and x <= max(x1, x2)
    else:
      low_x, high_x = min(x1, x2), max(x1, x2)
      low_y, high_y = min(y1, y2), max(y1, y2)
      if all([
        low_x <= x <= high_x, # ensure x is within rough range
        low_y <= y <= high_y, # ensure y is within rough range
        (y - y1) == ((y2 - y1) / (x2 - x1)) * (x - x1) # check point on line
      ]):
        return True
    return False

lines = [Line(x) for x in input]

def vis_lines(lines: list, size: int):
  virtual_board = [[0 for x in range(size)] for x in range(size)]
  for line in lines:
    for x in range(size):
      for y in range(size):
        if line.is_at_point(x, y):
          virtual_board[x][y] += 1
  # print('\n'.join([''.join([f'{"." if x == 0 else x}' for x in l]) for l in virtual_board]))
  return virtual_board

board = vis_lines(lines, 1000)
res = 0
for line in board:
  for col in line:
    if col >= 2:
      res += 1
print(res)