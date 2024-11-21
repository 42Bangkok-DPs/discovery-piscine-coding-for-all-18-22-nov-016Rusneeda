from is_king_in_check import checkmate
board = [
    [".", ".", ".", ".", "."],
    [".", ".", "Q", ".", "P"],
    [".", ".", ".", "Q", "."],
    [".", ".", ".", "K", "."],
    [".", ".", ".", ".", "."]
]

# ทดสอบ
print(is_king_in_check(board))  # Output: Success