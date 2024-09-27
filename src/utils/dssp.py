from minesweeper.minesweeperapp import MinesweeperApp
from utils.firstmove import firstmove
from utils.random_square import select_random_square
import time


class DoubleSetSinglePoint:
    """Luokka, jonka avulla voidaan ajaa DSSP-algoritmi annetulle pelille
    """
    
    def __init__(self, game):
        """Luokan konstruktori, jossa alustetaan algoritmi
        
        Args: 
            game (class Minesweeper): ratkaistava peli
        """
        
        self.game = game
        self.boardrows, self.boardcols = game.get_dimensions()
        self.probed = [[0 for i in range(self.boardcols)] for j in range(self.boardrows)]
        
    def doublesetsinglepoint(self):
        """Ajaa DSSP-algoritmin
        """
            
        # print(game.get_grid())
        # game.print_grid()
        opener = firstmove()
        s = set()
        s.add(opener)
        q = set()
        while self.game.gameover is False:
            if len(s) == 0:
                x = select_random_square(self.game.get_grid())
            while len(s) > 0:
                x = s.pop()
                self.game.open_square(x[0],x[1])
                if self.game.gameover:
                    self.game.print_grid()
                    return
                if self.isAFN(x) is True:
                    for nb in self.unmarked_neighbours(x):
                        s.add(nb)
                else:
                    q.add(x)
            for sq in q:
                if self.isAMN(sq):
                    for nb in self.unmarked_neighbours(sq):
                        self.game.mark_square(nb[0], nb[1])
                    q.remove(sq)
            for sq in q:
                if self.isAFN(sq):
                    for nb in self.unmarked_neighbours(sq):
                        s.add(nb)
                    q.remove(sq)

    def isAFN(self, x):
        """Tutkii, ovatko ruudun viereiset, ei-merkityt ruudut tyhjiä. Jos merkittyjä ruutuja on 
           yhtä paljon kuin tutkittavan ruudun arvo on, niin palauttaa True.
        
        Args:
            x (tuple): tutkittava ruutu
            
        Returns:
            (boolean): onko ruutu AFN (all free neighbours)
        """

        row = x[0]
        col = x[1]
        board = self.game.get_grid()
        xvalue = board[row][col]
        moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        count = 0
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if new_row >= 0 and new_row <= self.boardrows-1 and new_col >= 0 and new_col <= self.boardcols-1:
                if board[new_row][new_col] == -2:
                    count += 1
        return xvalue == count
    
    def isAMN(self, x):
        """Tutkii, ovatko ruudun viereiset, ei-merkityt ruudut pommeja. Jos avaamattomia ja merkittyjä ruutuja on yhtä paljon
           kuin tutkittavan ruudun arvo on, niin palauttaa True.

        Args:
            x (tuple): tutkittava ruutu
            
        Returns:
            (boolean): onko ruutu AMN (all mine/mark neighbours)
        """
        
        row = x[0]
        col = x[1]
        board = self.game.get_grid()
        xvalue = board[row][col]
        moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        count = 0
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if new_row >= 0 and new_row <= self.boardrows-1 and new_col >= 0 and new_col <= self.boardcols-1:
                if board[new_row][new_col] == -2 or board[new_row][new_col] == -1:
                    count += 1
                    
        return xvalue == count
    
    def unmarked_neighbours(self, x):
        """Palauttaa listan merkkaamattomista naapureista

        Args:
            x (tuple): ruutu, jonka merkkaamattomat naapurit palautetaan
            
        Returns:
            neighbours (list): lista, joka sisältää merkkaamattomat naapurit
        """
        
        row = x[0]
        col = x[1]
        self.probed[row][col] == 1
        board = self.game.get_grid()
        moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        neighbours = list()
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if new_row >= 0 and new_row <= self.boardrows-1 and new_col >= 0 and new_col <= self.boardcols-1:
                if board[new_row][new_col] != -2 and self.probed[new_row][new_col] == 0:
                    neighbours.append((new_row, new_col))
        return neighbours