import unittest
from minesweeper.minesweeper import Minesweeper

class TestMinesweeper(unittest.TestCase):
    
    def setUp(self):
        
        self.ms_beginner = Minesweeper((9,9), 10)
        self.ms_intermediate = Minesweeper((16,16), 40)
        self.ms_expert = Minesweeper((16,30), 99)
    
    def test_set_mines_on_first_open(self):
        """Testaa, että miinat asetetaan ensimmäisellä avauksella
        """
        
        ms = Minesweeper((3,3), 1)
        ms.open_square(0,0)
        count = 0
        for r in range(ms.rows):
            for c in range(ms.cols):
                if ms.values[r][c] == -1:
                    count += 1
        
        self.assertEqual(1, count)
        
    def test_too_many_mines(self):
        """Testataan, että tulee virhe, kun annetaan liikaa miinoja
        """
        
        with self.assertRaises(ValueError):
            Minesweeper((1,1), 2)
    
    def test_set_mines_beginner(self):
        """Testaa miinojen määrän oikeellisuus beginner-tasolla
        """
        
        self.ms_beginner.set_mines((0,0))
        values = self.ms_beginner.values
        print(values)
        count = 0
        for r in range(self.ms_beginner.rows):
            for c in range(self.ms_beginner.cols):
                if values[r][c] == -1:
                    count += 1
                    
        self.assertEqual(10, count)
        
    def test_set_mines_intermediate(self):
        """Testaa miinojen määrän oikeellisuus intermediate-tasolla
        """
        
        self.ms_intermediate.set_mines((0,0))
        values = self.ms_intermediate.values
        print(values)
        count = 0
        for r in range(self.ms_intermediate.rows):
            for c in range(self.ms_intermediate.cols):
                if values[r][c] == -1:
                    count += 1
                    
        self.assertEqual(40, count)
        
    def test_set_mines_expert(self):
        """Testaa miinojen määrän oikeellisuus expert-tasolla
        """
        
        self.ms_expert.set_mines((0,0))
        values = self.ms_expert.values
        print(values)
        count = 0
        for r in range(self.ms_expert.rows):
            for c in range(self.ms_expert.cols):
                if values[r][c] == -1:
                    count += 1
                    
        self.assertEqual(99, count)
        
    def test_count_values(self):
        """Testaa että ruutujen numerot lasketaan oikein
        """
        
        mine_locations = [(0,3),(1,3),(2,5),(3,0),(5,6),(5,8),(6,6),(6,8),(7,0),(8,8)]
        ms = Minesweeper((9,9), 10, mine_locations=mine_locations)
        
        expected = [[0,0,2,-1,2,0,0,0,0],
                    [0,0,2,-1,3,1,1,0,0],
                    [1,1,1,1,2,-1,1,0,0],
                    [-1,1,0,0,1,1,1,0,0],
                    [1,1,0,0,0,1,1,2,1],
                    [0,0,0,0,0,2,-1,4,-1],
                    [1,1,0,0,0,2,-1,4,-1],
                    [-1,1,0,0,0,1,1,3,2],
                    [1,1,0,0,0,0,0,1,-1]]
        
        self.assertEqual(ms.values, expected)
    
    def test_open_square(self):
        """Testaa että tyhjän ruudun avaus avaa viereisiä ruutuja rekursiivisesti oikein
        """
        
        mine_locations = [(0,3),(1,3),(2,5),(3,0),(5,6),(5,8),(6,6),(6,8),(7,0),(8,8)]
        ms = Minesweeper((9,9), 10, mine_locations=mine_locations)
        ms.open_square(5,0)
        
        expected = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,1,1,1,1,0,0,0,0],
                    [0,1,1,1,1,1,0,0,0],
                    [1,1,1,1,1,1,0,0,0],
                    [1,1,1,1,1,1,0,0,0],
                    [1,1,1,1,1,1,0,0,0],
                    [0,1,1,1,1,1,1,1,0],
                    [0,1,1,1,1,1,1,1,0]]
        
        self.assertEqual(ms.opened, expected)
        
        # Testataan, että peli häviää jos avaa miinan
        ms.open_square(0,3)
        self.assertTrue(ms.gameover)
        
if __name__ == "__main__":
    unittest.main()