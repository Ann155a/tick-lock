# tick-lock
This repository is my take on the `Code Challenge #2` of StackOverflow.

`tick-lock` is a time-based encryption system that traps a message in the moment it was created. 
It uses a time-derived seed to encrypt a message and encodes the result visually in a chessboard.

## 🔐 How It Works
- The time (HH:MM) is converted into a seed.
- Each character in the message is shifted using this seed.
- The encrypted message is converted into binary and encoded on a chessboard.
- Pawns (`P`) = binary 1, empty squares (`.`) = binary 0.


## 🔄 Decryption
To decrypt, you need the board and the original time.


