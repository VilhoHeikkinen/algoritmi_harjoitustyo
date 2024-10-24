from minesweeper.minesweeperapp import MinesweeperApp
from utils.dssp import DoubleSetSinglePoint

if __name__ == "__main__":
    
    ms = MinesweeperApp((16,30), 10, wait_after_print=True, enable_gui=True) # wait_after_print on defaultisti False. Jos valitaan True, niin peli odottaa sekunnin printin jälkeen
    dssp = DoubleSetSinglePoint(ms)
    dssp.doublesetsinglepoint()
    
    
    # ms.open_square(1,2)
    # ms.print_grid()
    # print(ms.get_grid())