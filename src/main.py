from minesweeper.minesweeperapp import MinesweeperApp
from utils.dssp import DoubleSetSinglePoint

if __name__ == "__main__":
    
    ms = MinesweeperApp((9,9), 10)
    dssp = DoubleSetSinglePoint(ms)
    dssp.doublesetsinglepoint()
    
    
    # ms.open_square(1,2)
    # ms.print_grid()
    # print(ms.get_grid())