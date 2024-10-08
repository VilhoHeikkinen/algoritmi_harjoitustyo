from minesweeper.minesweeperapp import MinesweeperApp
from utils.dssp import DoubleSetSinglePoint

if __name__ == "__main__":
    
    ms = MinesweeperApp((9,9), 10, wait_after_print=True) # wait_after_print on defaultisti False. Jos valitaan True, niin peli odottaa sekunnin printin jälkeen
    dssp = DoubleSetSinglePoint(ms)
    dssp.doublesetsinglepoint()
    
    
    # ms.open_square(1,2)
    # ms.print_grid()
    # print(ms.get_grid())