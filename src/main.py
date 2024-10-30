from minesweeper.minesweeperapp import MinesweeperApp
from utils.dssp import DoubleSetSinglePoint

if __name__ == "__main__":
    
    # ms = MinesweeperApp((16,30), 10, wait_after_print=True, enable_gui=True) # wait_after_print on defaultisti False. Jos valitaan True, niin peli odottaa sekunnin printin jälkeen
    # dssp = DoubleSetSinglePoint(ms)
    # dssp.doublesetsinglepoint()
    
    
    # ms.open_square(1,2)
    # ms.print_grid()
    # print(ms.get_grid())
    
    mines = [(2,1),(2,2)]
    ms = MinesweeperApp((3,3), 2, disable_printing=False, mine_locations=mines)
    ms.open_square(0,0)
    ms.mark_square(2,1)
    dssp = DoubleSetSinglePoint(ms)
    print(dssp.is_afn((1,0)))
    print(dssp.is_afn((1,2)))
    print(dssp.is_afn((0,0)))
    
    ms.mark_square(2,2)
    print(dssp.is_afn((1,1)))
    print(dssp.is_afn((1,2)))