from minesweeper.minesweeper import Minesweeper
from time import sleep

class MinesweeperApp:
    """Luokka, jonka avulla voidaan pelata miinaharavaa
    """
    
    def __init__(self, size, minecount, wait_after_print=False):
        """Luokan konstruktori, joka luo uuden pelin, tai jatkaa peliä annetusta vaiheesta
        
        Args: 
            size: miinaharavan pelikentän koko tuplena (n x m)
            minecount: miinojen määrä kentällä
        """
        
        self.ms = Minesweeper(size, minecount)
        self.gameover = False
        self.win = False
        self.wait_after_print = wait_after_print
        
    def new_game(self):
        """Aloittaa uuden interaktiivisen pelin
        """
        
        self.print_grid()
        while True:
            row, col = input("Syötä koordinaatit (r,s): ").split()
            
            self.open_square(int(row), int(col))
            self.print_grid()
            
            if self.ms.gameover is True:
                break
        
    def open_square(self, row, col):
        """Avaa halutun ruudun kentältä

        Args:
            row (int): rivi, jolta ruutu avataan
            col (int): sarake, jolta ruutu avataan
        """
        
        if self.ms.opened[row][col] == 0:
            self.ms.open_square(row, col)
            self.gameover = self.ms.gameover
            self.print_grid()
            if self.wait_after_print is True:
                sleep(1)
            if self.ms.win:
                self.win = True
                print("voittaja")
            
    def mark_square(self, row, col):
        """Merkkaa valitun ruudun

        Args:
            row (int): rivi, jolta ruutu merkataan
            col (int): sarake, jolta ruutu merkataan
        """
        
        self.ms.mark_square(row, col)
        self.print_grid()

    def get_grid(self):
        """Palauttaa pelikentän kaksiulotteisena listana
        
        Returns:
            grid: Pelikenttä kaksiulotteisena taulukkona
        """
        
        grid = self.ms.get_grid()
        return grid
    
    def print_grid(self):
        """Tulostaa pelilaudan
        """
        
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
        
    def get_dimensions(self):
        """Palauttaa pelikentän mitat
        
        Returns:
            dims: pelikentän mitat
        """
        
        return self.ms.rows, self.ms.cols