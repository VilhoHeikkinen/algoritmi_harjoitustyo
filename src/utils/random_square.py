from random import choice

def select_random_square(board):
    """Valitsee satunnaisesti yhden peitetyn ruudun
    
    Args:
        squares (list): merkkaamattomat ruudut
        
    Returns:
        random_square (tuple): satunnaisesti valittu peitetty ruutu
    """
    
    covered = list()
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == -1:
                covered.append((row,col))
    try:
        random_square = choice(covered)
    except IndexError:
        print(covered)
        # print(board)
        return False
    return random_square