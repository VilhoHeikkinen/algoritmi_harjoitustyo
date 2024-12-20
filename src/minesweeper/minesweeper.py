from random import randint

class Minesweeper:
    """Luokka, joka toteuttaa miinaharavan toiminnallisuuden
    """

    def __init__(self, size, minecount, mine_locations=None):
        """Luokan konstruktori, joka luo uuden pelin, tai jatkaa peliä annetusta vaiheesta
        
        Args: 
            size (tuple): miinaharavan pelikentän koko tuplena (n x m)
            minecount (int): miinojen määrä kentällä
            mine_locations (list): lista tupleja, jotka määrääväät pommien paikat kentällä
        """

        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.minecount = minecount
        if self.minecount >= self.rows*self.cols:
            raise ValueError("Annoit liian suuren määrän miinoja!")
        self.values, self.opened, self.marked = self.set_grid()
        if mine_locations is not None:
            self.set_values_for_input_mines(mine_locations)
            self.count_values()
        self.opened_count = 0
        self.to_open_count = (self.rows*self.cols) - minecount
        # self.set_mines()
        # self.count_values()
        if not mine_locations:
            self.set_mine_locations = True
        else:
            self.set_mine_locations = False
        self.gameover = False
        self.win = False
        
    def set_grid(self):
        """Alustaa kentän ruutujen arvot
        
        Returns:
            values: kaksiulotteinen taulukko, jossa kaikkien miinojen arvoksi asetettu 0
            opened: kaksiulotteinen taulukko, jossa merkittynä avatut ruudut (0 = ei avattu, 1 = avattu)
            marked: kaksiulotteinen taulukko, jossa merkittynä merkityt ruudut (0 = ei merkitty, 1 = merkitty)
        """
        
        values = [[0 for i in range(self.cols)] for j in range(self.rows)]
        opened = [[0 for i in range(self.cols)] for j in range(self.rows)]
        marked = [[0 for i in range(self.cols)] for j in range(self.rows)]
       
        return values, opened, marked
    
    def set_values_for_input_mines(self, mines):
        """Alustaa kentän ruutujen arvot annetulle pelikentälle

        Args:
            mines (list): lista pommien koordinaateista tupleina
        """

        for mine in mines:
            self.values[mine[0]][mine[1]] = -1

    def set_mines(self, square):
        """Asettaa kentälle miinat
        
        Args:
            square (tuple): ensimmäisen avauksen koordinaatit
        """

        count = 0
        while count < self.minecount:
            # Arvotaan satunnainen luku, josta saadaan uudelle
            # miinalle koordinaatit
            mine_r = randint(0, self.rows-1)
            mine_c = randint(0, self.cols-1)
            
            if self.values[mine_r][mine_c] != -1 and (mine_r, mine_c) != square:
                self.values[mine_r][mine_c] = -1
                count += 1
                
    def count_values(self):
        """Laskee jokaisen miinattoman ruudun arvon
        """
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.values[row][col] == -1:
                    continue
                
                count = 0
                moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
                for move in moves:
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if new_row >= 0 and new_row <= self.rows-1 and new_col >= 0 and new_col <= self.cols-1:
                        if self.values[new_row][new_col] == -1:
                            count += 1
                
                self.values[row][col] += count
    
    def open_square(self, row, col):
        """Avaa ruutuja kentältä rekursiivisesti. Jos avattu ruutu on arvoltaan 0 (eli vieressä ei pommia),
           niin avataan myös viereiset ruudut.
        
        Args:
            row: rivi, jolta ruutu avataan
            col: sarake, jolta ruutu avataan
        """
        
        if self.set_mine_locations is True:
            self.set_mines((row, col))
            self.count_values()
            self.set_mine_locations = False
        
        self.opened[row][col] = 1
        self.opened_count += 1
        
        if self.values[row][col] == -1:
            self.gameover = True
            return
        
        if self.opened_count == self.to_open_count:
            self.win = True
            return
        
        if self.values[row][col] == 0:
            moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
            for move in moves:
                new_row = row + move[0]
                new_col = col + move[1]
                if new_row >= 0 and new_row <= self.rows-1 and new_col >= 0 and new_col <= self.cols-1:
                    if self.opened[new_row][new_col] != 1:
                        self.open_square(new_row, new_col)
                        
    def mark_square(self, row, col):
        """Merkkaa valitun ruudun

        Args:
            row (int): rivi, jolta ruutu merkataan
            col (int): sarake, jolta ruutu merkataan
        """
        
        self.marked[row][col] = 1
                        
    def get_grid(self):
        """Palauttaa pelikentän taulukkona
        
        Returns:
            grid: Pelikenttä kaksiulotteisena taulukkona
        """

        grid = list()
        for row in range(self.rows):
            new_row = list()
            for col in range(self.cols):
                if self.opened[row][col] == 1:
                    new_row.append(self.values[row][col])
                elif self.marked[row][col] == 1:
                    new_row.append(-2)
                else:
                    new_row.append(-1)
            grid.append(new_row)
        return grid
        