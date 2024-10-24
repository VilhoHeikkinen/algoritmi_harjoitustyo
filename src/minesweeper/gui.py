import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1' 

class MinesweeperGUI:
    """Luokka, jonka avulla voidaan piirtää miinaharavakenttä 
       graafisesti
    """
    
    def __init__(self, size):
        """Luokan konstruktori, joka luo uuden ruudun
        
        Args:
            size: miinaharavan pelikentän koko tuplena (n x m)
        """
        
        self.rows = size[0]
        self.cols = size[1]
        self.square_size = 50 # Ruutujen koko 50x50 px
        self.imgs = dict()
        self.get_images()
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.screen_width = self.cols*self.square_size
        self.screen_height = self.rows*self.square_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
    def get_images(self):
        """Tallentaa pelin ruutujen kuvat dictionaryyn"""
        
        img_location = os.getcwd() + "/minesweeper/images/"
        for base, dirs, files in os.walk(img_location):
            for file in files:
                name = file.split(".")[0] # Otetaan tiedoston nimi ilman .png -päätettä
                self.imgs[name] = pygame.transform.scale(pygame.image.load(img_location + file),
                                                         (self.square_size, self.square_size))
        
    def draw_grid(self, values, opened, marked):
        """Piirtää pelilaudan ruudulle

        Args:
            values (list): kaksiulotteinen taulukko, jossa pelilaudan ruutujen arvot
            opened (list): kaksiulotteinen taulukko, jossa merkitty avatut ruudut
            marked (list): kaksiulotteinen taulukko, jossa merkitty merkatut/liputetut ruudut
        """
        
        for row in range(self.rows):
            for col in range(self.cols):
                if opened[row][col] == 1:
                    if values[row][col] == -1:
                        img = self.imgs["bomba"]
                    else:
                        img = self.imgs[str(values[row][col])]
                elif marked[row][col] == 1:
                    img = self.imgs["flag"]
                else:
                    img = self.imgs["not_opened"]
                self.screen.blit(img, (col*self.square_size, row*self.square_size))
                pygame.display.flip()
                
    def draw_winner(self):
        """Ilmoittaa voitosta ruudulla"""
        
        img = pygame.transform.scale(self.imgs["voitto"], (100, 100))
        pos = ((self.screen_width//2) - 50, (self.screen_height//2) - 50)
        self.screen.blit(img, pos)
        pygame.display.flip()
        
    def idle_screen(self):
        """Aloittaa loopin, jotta ruutu pysyisi näkyvillä
        
        Returns:
            newgame (boolean): True, jos uusi peli halutaan aloittaa, False muuten"""
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        newgame = True
                        return newgame
            pygame.time.Clock().tick(30)
            
        