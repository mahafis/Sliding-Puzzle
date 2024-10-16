import os
import random

path = os.getcwd() # get the current working directory of the folder this file is stored in
NUM_ROWS = 4
NUM_COLS = 4
RESOLUTION = 800
TILE_WIDTH = RESOLUTION/NUM_COLS
TILE_HEIGHT = RESOLUTION/NUM_ROWS

class Tile:
    
    def __init__(self, row, col):
        self.r = row
        self.c = col
        self.v = row * NUM_COLS + col
        self.img = loadImage(path + "/images/" + str(self.v) + ".png")

    def swap(self, other):
        tmp_v = self.v
        self.v = other.v
        other.v = tmp_v
        
        tmp_img = self.img
        self.img = other.img
        other.img = tmp_img

    def display(self):
        if self.v != 15:
            image(self.img, self.c * TILE_WIDTH, self.r * TILE_HEIGHT)
            noFill()
            stroke(0)
            strokeWeight(5)
            rect(self.c * TILE_WIDTH, self.r * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)

class Puzzle(list):
    
    def __init__(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r, c))

    def show_tiles(self):
        for tile in self:
            tile.display()
    
    def get_empty_tile(self):
        for tile in self:
            if tile.v == 15:
                return tile
            
    def get_tile(self, r, c):
        for tile in self:
            if tile.r == r and tile.c == c:
                return tile
        return None
    
    def move(self, dir):
        empty_tile = self.get_empty_tile()
        if dir == RIGHT:
            neighbor_tile = self.get_tile(empty_tile.r, empty_tile.c - 1)
        if dir == LEFT:
            neighbor_tile = self.get_tile(empty_tile.r, empty_tile.c + 1)
        if dir == UP:
            neighbor_tile = self.get_tile(empty_tile.r + 1, empty_tile.c)
        if dir == DOWN:
            neighbor_tile = self.get_tile(empty_tile.r - 1, empty_tile.c)
            
        if neighbor_tile != None:
            empty_tile.swap(neighbor_tile)
            
    def shuffle(self, moves=100):
        for _ in range(moves):
            empty_tile = self.get_empty_tile()
            neighbors = []

            # Check for possible moves and add neighbor tiles to the list
            if empty_tile.r > 0:  # Can move down
                neighbors.append(self.get_tile(empty_tile.r - 1, empty_tile.c))
            if empty_tile.r < NUM_ROWS - 1:  # Can move up
                neighbors.append(self.get_tile(empty_tile.r + 1, empty_tile.c))
            if empty_tile.c > 0:  # Can move right
                neighbors.append(self.get_tile(empty_tile.r, empty_tile.c - 1))
            if empty_tile.c < NUM_COLS - 1:  # Can move left
                neighbors.append(self.get_tile(empty_tile.r, empty_tile.c + 1))

            # Randomly select a neighbor to swap with the empty tile
            neighbor = random.choice(neighbors)
            empty_tile.swap(neighbor)
            
            
            
    
def setup():
    size(RESOLUTION, RESOLUTION)
    background(0,0,0)

def draw():
    background(0,0,0)
    puzzle.show_tiles()

def keyPressed():
    if keyCode in [UP, DOWN, RIGHT, LEFT]:
        puzzle.move(keyCode)
        
puzzle = Puzzle()
puzzle.shuffle()











    
    
