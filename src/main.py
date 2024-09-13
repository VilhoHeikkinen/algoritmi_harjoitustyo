from minesweeper import Minesweeper

if __name__ == "__main__":
    
    ms = Minesweeper((9,9), 10)
    ms.open_square(1,2)
    ms.print_grid()