import unittest
from minesweeper.minesweeper import Minesweeper

class TestMinesweeper(unittest.TestCase):
    
    def setUp(self):
        
        self.ms_beginner = Minesweeper((9,9), 10)
        self.ms_intermediate = Minesweeper((16,16), 40)
        self.ms_expert = Minesweeper((16,30), 99)
    
    def test_set_mines_beginner(self):
        
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
        
if __name__ == "__main__":
    unittest.main()