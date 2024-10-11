from object import Player
from object import Judge

if __name__ == '__main__':
    judge = Judge()
    playerA = Player('山本')
    playerB = Player('鈴木')
    judge.start_janken(playerA,playerB)