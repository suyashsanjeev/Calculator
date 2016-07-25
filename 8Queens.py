ref = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h']
board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append(False)

def underAttack(x, y, b):
    if b[x][y]:
        return b
    i = x
    while i < 8:
        i+=1
print(board)
