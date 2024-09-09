from random import randint

class Minesweeper:
    """Luokka, jonka avulla voidaan pelata miinaharavaa.
    """

    def __init__(self, size, minecount):
        """Luokan konstruktori, joka luo uuden pelin, tai jatkaa peliä annetusta vaiheesta
        
        Args: 
            koko: Miinaharavan pelikentän koko tuplena (n x m)
        """

        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.minecount = minecount
        self.values = self.set_grid()
        self.set_mines()
        self.count_values()
        
    def set_grid(self):
        """Alustaa kentän ruutujen arvot
        
        Returns:
            ruutujen_arvot: kaksiulotteinen taulukko, jossa kaikkien miinojen arvoksi asetettu 0
        """
        
        values = [[0 for i in range(self.cols)] for j in range(self.rows)]
       
        return values

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
        
        for n in range(self.rows):
            for m in range(self.cols):
                if self.values[n][m] == -1:
                    continue
                
                count = 0
                if n > 0 and self.values[n-1][m] == -1:
                    count += 1
                if n > 0 and m < self.cols-1 and self.values[n-1][m+1] == -1:
                    count  += 1
                if m < self.cols-1 and self.values[n][m+1] == -1:
                    count  += 1
                if m < self.cols-1 and n < self.rows-1 and self.values[n+1][m+1] == -1:
                    count  += 1
                if n < self.rows-1 and self.values[n+1][m] == -1:
                    count  += 1
                if n < self.rows-1 and m > 0 and self.values[n+1][m-1] == -1:
                    count  += 1
                if m > 0 and self.values[n][m-1] == -1:
                    count  += 1
                if m > 0 and n > 0 and self.values[n-1][m-1] == -1:
                    count  += 1
                
                self.values[n][m] += count

    def print_grid(self):
        """Tulostaa pelilaudan
        """
        
        for i in range(self.rows):
            print(" " + ((4*self.cols)-1)*"—" + " ")
            line = "|"
            for j in range(self.cols):
                if self.values[i][j] != -1:
                    line += " " + str(self.values[i][j]) + " |"
                else:
                    line += " ? |"
            print(line)
        print(" " + ((4*self.cols)-1)*"—" + " ")