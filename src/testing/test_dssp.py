import unittest
from utils.dssp import DoubleSetSinglePoint
from minesweeper.minesweeperapp import MinesweeperApp

class TestDssp(unittest.TestCase):
    
    def setUp(self):
        
        pass
    
    def test_double_set_singlepoint(self):
        """Testaa DSSP:n toiminta"""
        
        # Testataan, että peli, jonka voi ratkaista ilman arvaamista, päättyy voittoon
        mines = [(0,4),(0,5),(1,3),(2,5),(3,5),(5,4),(5,8),(6,5),(7,2),(8,8)]
        for i in range(100):
            ms = MinesweeperApp((9,9), 10, disable_printing=True, mine_locations=mines)
            dssp = DoubleSetSinglePoint(ms)
            self.assertTrue(dssp.doublesetsinglepoint())
            
        # Testataan, että double_set_singlepoint palauttaa False kun avataan pommi
        mines = [(0,0)]
        ms = MinesweeperApp((2,2), 1, disable_printing=True, mine_locations=mines)
        dssp = DoubleSetSinglePoint(ms)
        self.assertFalse(dssp.doublesetsinglepoint())
        
        # Testataan, että peli arvaa, kun setti S on tyhjä
        mines = [(0,1)]
        while True:
            ms = MinesweeperApp((3,3), 1, disable_printing=True, mine_locations=mines)
            dssp = DoubleSetSinglePoint(ms)
            dssp.doublesetsinglepoint()
            if ms.gameover:
                break
                
    def test_is_afn(self):
        """Testaa toimiiko is_afn"""
        
        mines = [(2,1),(2,2)]
        ms = MinesweeperApp((3,3), 2, disable_printing=True, mine_locations=mines)
        ms.open_square(0,0)
        ms.mark_square(2,1)
        dssp = DoubleSetSinglePoint(ms)

        self.assertTrue(dssp.is_afn((1,0)))
        self.assertFalse(dssp.is_afn((1,2)))
        self.assertFalse(dssp.is_afn((0,0)))
        
        ms.mark_square(2,2)
        self.assertTrue(dssp.is_afn((1,1)))
        
    def test_is_amn(self):
        """Testaa toimiiko is_amn"""
        
        mines = [(2,1),(2,2)]
        ms = MinesweeperApp((3,3), 2, disable_printing=True, mine_locations=mines)
        ms.open_square(0,0)
        ms.mark_square(2,1)
        dssp = DoubleSetSinglePoint(ms)

        self.assertFalse(dssp.is_amn((1,0)))
        self.assertTrue(dssp.is_amn((1,2)))
        self.assertFalse(dssp.is_amn((0,0)))
        
        ms.mark_square(2,2)
        self.assertFalse(dssp.is_amn((1,1)))
        
    def test_unmarked_neighbours(self):
        """Testaa toimiiko unmarked_neighbours"""
        
        mines = [(2,1),(2,2)]
        ms = MinesweeperApp((3,3), 2, disable_printing=True, mine_locations=mines)
        ms.open_square(0,0)
        dssp = DoubleSetSinglePoint(ms)
        
        self.assertEqual(set([(2,1),(2,2)]), set(dssp.unmarked_neighbours((1,2))))
        self.assertEqual(set([(2,1),(2,2),(2,0)]), set(dssp.unmarked_neighbours((1,1))))
        self.assertEqual([], dssp.unmarked_neighbours((0,0)))
        
        ms.mark_square(2,1)
        
        self.assertEqual(set([(2,2)]), set(dssp.unmarked_neighbours((1,2))))
        self.assertEqual(set([(2,2),(2,0)]), set(dssp.unmarked_neighbours((1,1))))
        self.assertEqual([], dssp.unmarked_neighbours((0,0)))
        
    def test_unresolved_squares(self):
        """Testaa toimiiko unresolved_squares"""
        
        mines = [(2,1),(2,2)]
        ms = MinesweeperApp((3,3), 2, disable_printing=True, mine_locations=mines)
        ms.open_square(0,0)
        dssp = DoubleSetSinglePoint(ms)
        
        self.assertEqual(set([(2,1),(2,2),(2,0),(1,0),(1,1),(1,2)]), set(dssp.unresolved_squares((0,0))))
        
        ms.open_square(2,0)
        ms.mark_square(2,1)
        # Resetoidaan unresolved_probed, koska muuten unresolved_squares palauttaisi tyhjän listan
        dssp.unresolved_probed = [[0 for i in range(dssp.boardcols)] for j in range(dssp.boardrows)]
        
        self.assertEqual(set([(2,2),(2,0),(1,0),(1,1),(1,2)]), set(dssp.unresolved_squares((0,0))))
        # Testataan vielä että palautuksena ei tule jo kertaalleen käytyjä ruutuja
        self.assertEqual([], dssp.unresolved_squares((0,0)))

         
if __name__ == "__main__":
    unittest.main()