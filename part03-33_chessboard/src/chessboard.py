# Write your solution here
def oddChessboard(length):
    size = ((length**2) // 2) + 1
    board = "10" * size
    for i in range(length):
        print(board[0:length])
        board = board[length:]


def evenChessboard(length):
    size = length // 2
    row = "10" * size
    if length % 2 != 0:
        row += "1"
    for i in range(length):
        print(row)
        row = row[::-1]


def chessboard(length):
    if length % 2 == 0:
        evenChessboard(length)
    else:
        oddChessboard(length)
# Testing the function
if __name__ == "__main__":
    chessboard(3)
