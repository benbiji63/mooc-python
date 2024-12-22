# Write your solution here
def squared(string, length):
    size = ((length**2) // 2) + 1
    board = string * size
    for i in range(length):
        print(board[0:length])
        board = board[length:]