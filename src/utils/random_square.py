from random import randint

def select_random_square(squares):
    """Valitsee satunnaisesti yhden peitetyn ruudun
    
    Args:
        squares (list): merkkaamattomat ruudut
    """
    
    return squares[randint(len(squares))]