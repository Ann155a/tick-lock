seed = get_time_seed()
msg = "GUESSWHAT"
encrypted = encrypt_message(msg, seed)
board = message_to_board(encrypted)

print(f"Encrypted: {encrypted}")
print_board(board)
