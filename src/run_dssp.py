import argparse
from minesweeper.minesweeperapp import MinesweeperApp
from utils.dssp import DoubleSetSinglePoint

class Parameters:
    """Luokka, johon säilytetään annetut parametrit"""
    
    def __init__(self, args):
        
        self.args = args
        self.difficulty = args.difficulty
        self.disable_gui = args.disable_gui

def run_dssp(difficulty, disable_gui=False, running_stats=False):
    
    if difficulty == "b":
        size = (9,9)
        mines = 10
    elif difficulty == "i":
        size = (16,16)
        mines = 40
    elif difficulty == "e":
        size = (16,30)
        mines = 99
        
    if running_stats:
        ms = MinesweeperApp(size, mines, wait_after_print=False, enable_gui=False, disable_printing=True) # wait_after_print on defaultisti False. Jos valitaan True, niin peli odottaa sekunnin printin jälkeen
        dssp = DoubleSetSinglePoint(ms)
        win = dssp.doublesetsinglepoint()
        return win
        
    if disable_gui is True:
        enable_gui = False
    else:
        enable_gui = True

    ms = MinesweeperApp(size, mines, wait_after_print=True, enable_gui=enable_gui) # wait_after_print on defaultisti False. Jos valitaan True, niin peli odottaa sekunnin printin jälkeen
    dssp = DoubleSetSinglePoint(ms)
    win = dssp.doublesetsinglepoint()
    
    newgame = ms.handle_outcome(win)
    if newgame:
        run_dssp(difficulty=difficulty)
    
def parse_cmdline_args():

    parser = argparse.ArgumentParser()

    #
    # Basic input
    #
    group_input = parser.add_argument_group("Basic input stuff")

    group_input.add_argument("--difficulty",
                             dest="difficulty",
                             help="The difficulty of the minesweeper game (b = beginner, i = intermediate, e = expert)",
                             default="b")
    
    group_input.add_argument("--disable-gui",
                             action="store_true",
                             dest="disable_gui",
                             help="Disable pygame GUI and output the game to terminal",
                             default=False)

    print(parser.parse_args())

    return parser.parse_args()

def main():
    
    args = parse_cmdline_args()
    P = Parameters(args)
    
    run_dssp(P.difficulty, P.disable_gui)
    
if __name__ == "__main__":
    main()