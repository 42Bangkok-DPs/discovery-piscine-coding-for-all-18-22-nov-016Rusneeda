def checkSquare(board):
    for r in board:
        if len(r) != len(board):
            return False
        
    return True

def check_pawn(piece_pos, king_pos, board):
    piece_row, piece_col = piece_pos
    king_row, king_col = king_pos
    
    # Pawn เดินทแยง 1 ช่องเพื่อกินหมาก (Pawn เดินทแยงได้แค่ในทิศทางการกิน)
    # คำนึงถึงว่าหมากจะเดินทแยงไปทางไหน
    # สมมติว่า Pawn อยู่ในตำแหน่ง (row, col)
    
    if board[piece_row][piece_col] == "P":
        if piece_row - 1 == king_row and (piece_col - 1 == king_col or piece_col + 1 == king_col):
            return True
    
    return False

def checkmate(board):

    board = board.split()

    if not checkSquare(board):
        print("Error : board is not square")
        return 0
    

    
    # ค้นหาตำแหน่งของ King และตัวหมากอื่น
    king_pos = None
    enemy_positions = []
    king_count = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "K":
                king_count = king_count + 1
                king_pos = (row, col)
            elif board[row][col] in "QRBP":
                enemy_positions.append((board[row][col], row, col))

    if king_count > 1:
        print("Error : King more than one")
        return 0

    if not king_pos:
        print("Error : not found King")
        return 0  # หากไม่มี King ให้ถือว่าไม่ถูก check

    # ตรวจสอบว่า King ถูกข่มขู่ (check) หรือไม่
    for piece, row, col in enemy_positions:
        if can_piece_check_king(piece, (row, col), king_pos, board):
            print("Success")
            return 1
    
    print("Fail")
    return 0


def can_piece_check_king(piece, piece_pos, king_pos, board):
    piece_row, piece_col = piece_pos
    king_row, king_col = king_pos
    
    # ตรวจสอบรูปแบบการเดินของแต่ละตัวหมาก
    if piece == "Q":  # Queen: แนวตรง + แนวทแยง
        return check_straight_or_diagonal(piece_pos, king_pos, board)
    elif piece == "R":  # Rook: แนวตรง
        return check_straight(piece_pos, king_pos, board)
    elif piece == "B":  # Bishop: แนวทแยง
        return check_diagonal(piece_pos, king_pos, board)
    elif piece == "P":  # Pawn: เดินทแยงได้เฉพาะการกิน
        return check_pawn(piece_pos, king_pos, board)
    
    return False


# ตัวอย่างฟังก์ชันช่วยเหลือสำหรับตรวจสอบการเดิน:
def check_straight_or_diagonal(piece_pos, king_pos, board):
    return check_straight(piece_pos, king_pos, board) or check_diagonal(piece_pos, king_pos, board)

def check_straight(piece_pos, king_pos, board):
    # ตรวจสอบแนวตรง (แนวตั้ง/แนวนอน) และว่ามีหมากขวางทางหรือไม่
    piece_row, piece_col = piece_pos
    king_row, king_col = king_pos
    
    if piece_row == king_row or piece_col == king_col:  # อยู่ในแถวเดียวกันหรือตรงคอลัมน์เดียวกัน
        return not is_blocked(piece_pos, king_pos, board)
    
    return False

def check_diagonal(piece_pos, king_pos, board):
    # ตรวจสอบแนวทแยง
    piece_row, piece_col = piece_pos
    king_row, king_col = king_pos
    
    if abs(piece_row - king_row) == abs(piece_col - king_col):  # แนวทแยง
        return not is_blocked(piece_pos, king_pos, board)
    
    return False

def is_blocked(start, end, board):
    # ตรวจสอบว่ามีหมากขวางทางระหว่าง start และ end หรือไม่
    start_row, start_col = start
    end_row, end_col = end
    
    step_row = (end_row - start_row) // max(abs(end_row - start_row), 1)
    step_col = (end_col - start_col) // max(abs(end_col - start_col), 1)
    
    current_row, current_col = start_row + step_row, start_col + step_col
    while (current_row, current_col) != (end_row, end_col):
        if board[current_row][current_col] != ".":
            return True
        current_row += step_row
        current_col += step_col
    
    return False