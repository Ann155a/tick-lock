from datetime import datetime

def get_time_seed():
    now = datetime.now()
    return (now.hour * 60 + now.minute) % 256  

def encrypt_message(msg, seed):
    encrypted = []
    for i, char in enumerate(msg):
        encrypted_char = chr((ord(char) + seed + i) % 256)
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

def message_to_board(encrypted):
    board = [['.' for _ in range(8)] for _ in range(8)]
    bits = ''.join(f'{ord(c):08b}' for c in encrypted)
    for i in range(8):
        for j in range(8):
            board[i][j] = 'P' if bits[i*8 + j] == '1' else '.'
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

