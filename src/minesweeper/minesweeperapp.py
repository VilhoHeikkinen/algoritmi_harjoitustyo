from minesweeper.minesweeper import Minesweeper
from minesweeper.gui import MinesweeperGUI
from time import sleep

class MinesweeperApp:
    """Luokka, jonka avulla voidaan pelata miinaharavaa
    """
    
    def __init__(self, size, minecount, wait_after_print=False, enable_gui=False, disable_printing=False, mine_locations=None):
        """Luokan konstruktori, joka luo uuden pelin, tai jatkaa peliä annetusta vaiheesta
        
        Args: 
            size: miinaharavan pelikentän koko tuplena (n x m)
            minecount: miinojen määrä kentällä
            wait_after_print: odottaa hetken printin jälkeen
            enable_gui: ottaa graafisen käyttöliittymän käyttöön
            disable_printing: poistaa kentän tulostuksen käytöstä
            mine_locations: lista tupleja, jotka määrääväät pommien paikat kentällä
        """
        
        self.ms = Minesweeper(size, minecount, mine_locations=mine_locations)
        self.gameover = False
        self.win = False
        self.wait_after_print = wait_after_print
        self.disable_printing = disable_printing
        if enable_gui:
            self.gui = MinesweeperGUI(size)
            self.gui.draw_grid(self.ms.values, self.ms.opened, self.ms.marked)
        else:
            self.gui = False
        
    def open_square(self, row, col):
        """Avaa halutun ruudun kentältä

        Args:
            row (int): rivi, jolta ruutu avataan
            col (int): sarake, jolta ruutu avataan
        """
        
        if self.ms.opened[row][col] == 0:
            self.ms.open_square(row, col)
            self.gameover = self.ms.gameover
            if self.disable_printing is False:
                self.print_grid()
            if self.ms.win:
                self.win = True
            
    def mark_square(self, row, col):
        """Merkkaa valitun ruudun

        Args:
            row (int): rivi, jolta ruutu merkataan
            col (int): sarake, jolta ruutu merkataan
        """
        
        if self.ms.opened[row][col] == 0:
            self.ms.mark_square(row, col)
            if self.disable_printing is False:
                self.print_grid()
        else:
            print("Et voi merkata avattua ruutua!")

    def get_grid(self):
        """Palauttaa pelikentän kaksiulotteisena listana
        
        Returns:
            grid: Pelikenttä kaksiulotteisena taulukkona
        """
        
        grid = self.ms.get_grid()
        return grid
    
    def get_dimensions(self):
        """Palauttaa pelikentän mitat
        
        Returns:
            dims: pelikentän mitat
        """
        
        return self.ms.rows, self.ms.cols
    
    def print_grid(self, debug=False):
        """Tulostaa pelilaudan
        """
        if self.disable_printing is True and debug is False:
            return
        if self.gui:
            self.gui.draw_grid(self.ms.values, self.ms.opened, self.ms.marked)
            if self.wait_after_print is True:
                sleep(0.4)
        else:
            for i in range(self.ms.rows):
                print(" " + ((4*self.ms.cols)-1)*"—" + " ")
                line = "|"
                for j in range(self.ms.cols):
                    if self.ms.opened[i][j] == 1:
                        if self.ms.values[i][j] != -1:
                            line += " " + str(self.ms.values[i][j]) + " |"
                        else:
                            line += " * |"
                    elif self.ms.marked[i][j] == 1:
                        line += "=!=|"
                    else:
                        line += "===|"
                print(line)
            print(" " + ((4*self.ms.cols)-1)*"—" + " ")
            if self.wait_after_print is True:
                sleep(0.5)
                
    def handle_outcome(self, win):
        """Käsittelee pelin tuloksen. Ilmoittaa voitosta/häviöstä
        
        Returns:
            newgame (boolean): True, jos uusi peli halutaan aloittaa, False muuten"""
        
        if win:
            if self.gui:
                self.gui.draw_winner()
                return self.gui.idle_screen()
            else:
                print("Voitit")
        else:
            if self.gui:
                return self.gui.idle_screen()
            else:
                print("Hävisit")
