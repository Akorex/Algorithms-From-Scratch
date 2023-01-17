class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"{self._name}, {self._score}"


class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order"""

    def __init__(self, capacity=10):
        """Initialize a scoreboard with given capacity
        
        All enteries are initially None
        """
        self._board = [None] * capacity
        self._n = 0 # counter for scores

    def __getitem__(self, index):
        """Return entry at given index"""
        return self._board[index]
    
    def __str__(self):
        """Return string representation of the high score list"""
        return '\n'.join(str(self._board[i]) for i in range(self._n))

    def add(self, entry, score):
        """Consider adding score to list of high scores
        Adds score if board is not full or score is higher than last entry
        """

        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n -1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


# implementing insert sort algorithm
def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order"""
    for k in range(1, len(A)):
        curr = A[k] # current element to be inserted
        j = k  # find correct index j for current
        while j > 0 and A[j-1] > curr:
            A[j] = A[j - 1]
            j -= 1
        A[j] = curr
g = GameEntry('Bob', 25)
print(str(g))


class TicTacToe:
    """Management of a TicTacToe game (does not do strategy)"""

    def __init__(self):
        """Start a new game"""
        self._board = [[' ']* 3 for j in range(3)] # creates the x & o grid
        self._player = 'X'

    def mark(self, i, j):
        """Put an X or O mark at position (i, j) for the next player's turn """
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        """Check whether the board configuration is a win for the given player"""
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
        mark == board[1][0] == board[1][1] == board[1][2] or # row 1
        mark == board[2][0] == board[2][1] == board[2][2] or # row 2
        mark == board[0][0] == board[1][0] == board[2][0] or # column 0
        mark == board[0][1] == board[1][1] == board[2][1] or # column 1
        mark == board[0][2] == board[1][2] == board[2][2] or # column 2
        mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
        mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        """Return mark of winning player or None to indicate a tie"""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        """Return string representation of current game board"""
        rows = ['|'.join(self._board[r] for r in range(3))]
        return 'n------\n'.join(rows)
