from random import choice

def select_random_square(squares, board):
    """Valitsee satunnaisesti yhden peitetyn ruudun
    
    Args:
        squares (list): merkkaamattomat ruudut
        
    Returns:
        random_square (tuple): satunnaisesti valittu peitetty ruutu
    """
    
    covered = list()
    for sq in squares:
        if board[sq[0]][sq[1]] == -1:
            covered.append(sq)
    random_square = choice(covered)
    return random_square