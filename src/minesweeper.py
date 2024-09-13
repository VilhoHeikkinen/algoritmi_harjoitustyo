from random import randint

class Minesweeper:
    """Luokka, jonka avulla voidaan pelata miinaharavaa.
    """

    def __init__(self, size, minecount):
        """Luokan konstruktori, joka luo uuden pelin, tai jatkaa peliä annetusta vaiheesta
        
        Args: 
            size: miinaharavan pelikentän koko tuplena (n x m)
            minecount: miinojen määrä kentällä
        """

        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.minecount = minecount
        self.values, self.opened = self.set_grid()
        self.set_mines()
        self.count_values()
        
    def set_grid(self):
        """Alustaa kentän ruutujen arvot
        
        Returns:
            values: kaksiulotteinen taulukko, jossa kaikkien miinojen arvoksi asetettu 0
            opened: kaksiulotteinen taulukko, jossa merkittynä avatut ruudut (0 = ei avattu, 1 = avattu)
        """
        
        values = [[0 for i in range(self.cols)] for j in range(self.rows)]
        opened = [[0 for i in range(self.cols)] for j in range(self.rows)]
       
        return values, opened

    def set_mines(self):
        """Asettaa kentälle miinat
        """
      
        count = 0
        while count < self.minecount:
            # Arvotaan satunnainen luku, josta saadaan uudelle
            # miinalle koordinaatit
            num = randint(0, self.rows*self.cols - 1)
            mine_r = num % self.rows
            mine_s = num // self.cols
            
            
            # print(mine_r, mine_s)
            if self.values[mine_r][mine_s] != -1:
                self.values[mine_r][mine_s] = -1
                count += 1
                
    def count_values(self):
        """Laskee jokaisen miinattoman ruudun arvon
        """
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.values[row][col] == -1:
                    continue
                
                count = 0
                # if n > 0 and self.values[n-1][m] == -1:
                #     count += 1
                # if n > 0 and m < self.cols-1 and self.values[n-1][m+1] == -1:
                #     count  += 1
                # if m < self.cols-1 and self.values[n][m+1] == -1:
                #     count  += 1
                # if m < self.cols-1 and n < self.rows-1 and self.values[n+1][m+1] == -1:
                #     count  += 1
                # if n < self.rows-1 and self.values[n+1][m] == -1:
                #     count  += 1
                # if n < self.rows-1 and m > 0 and self.values[n+1][m-1] == -1:
                #     count  += 1
                # if m > 0 and self.values[n][m-1] == -1:
                #     count  += 1
                # if m > 0 and n > 0 and self.values[n-1][m-1] == -1:
                #     count  += 1
                
                moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
                for move in moves:
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if new_row >= 0 and new_row <= self.rows-1 and new_col >= 0 and new_col <= self.cols-1:
                        if self.values[new_row][new_col] == -1:
                            count += 1
                
                self.values[row][col] += count
    
    def open_square(self, row, col):
        """Avaa ruutuja laudalta rekursiivisesti. Jos avattu ruutu on arvoltaan 0 (eli vieressä ei pommia),
           niin avataan myös viereiset ruudut.
        
        Args:
            row: rivi, jolta ruutu avataan
            col: sarake, jolta ruutu avataan
        """
        
        
        self.opened[row][col] = 1
        if self.values[row][col] == 0:
            # if row > 0 and self.values[row-1][col] != -1:
            #     if self.opened[row-1][col] != 1:
            #         self.open_square(row-1, col)
            # if row > 0 and col < self.cols-1 and self.values[row-1][col+1] != -1:
            #     if self.opened[row-1][col+1] != 1:
            #         self.open_square(row-1, col+1)
            # if col < self.cols-1 and self.values[row][col+1] != -1:
            #     if self.opened[row][col+1] != 1:
            #         self.open_square(row, col+1)
            # if col < self.cols-1 and row < self.rows-1 and self.values[row+1][col+1] != -1:
            #     if self.opened[row+1][col+1] != 1:
            #         self.open_square(row+1, col+1)
            # if row < self.rows-1 and self.values[row+1][col] != -1:
            #     if self.opened[row+1][col] != 1:
            #         self.open_square(row+1, col)
            # if row < self.rows-1 and col > 0 and self.values[row+1][col-1] != -1:
            #     if self.opened[row+1][col-1] != 1:
            #         self.open_square(row+1, col-1)
            # if col > 0 and self.values[row][col-1] != -1:
            #     if self.opened[row][col-1] != 1:
            #         self.open_square(row, col-1)
            # if col > 0 and row > 0 and self.values[row-1][col-1] != -1:
            #     if self.opened[row-1][col-1] != 1:
            #         self.open_square(row-1, col-1)
                    
            moves = [(-1,0), (0,1), (1,0), (0,-1)]
            for move in moves:
                new_row = row + move[0]
                new_col = col + move[1]
                if new_row >= 0 and new_row <= self.rows-1 and new_col >= 0 and new_col <= self.cols-1:
                    if self.opened[new_row][new_col] != 1:
                        self.open_square(new_row, new_col)
        

    def print_grid(self):
        """Tulostaa pelilaudan
        """
        
        for i in range(self.rows):
            print(" " + ((4*self.cols)-1)*"—" + " ")
            line = "|"
            for j in range(self.cols):
                if self.opened[i][j] == 1:
                    if self.values[i][j] != -1:
                        line += " " + str(self.values[i][j]) + " |"
                    else:
                        line += " * |"
                else:
                    line += "===|"
            print(line)
        print(" " + ((4*self.cols)-1)*"—" + " ")