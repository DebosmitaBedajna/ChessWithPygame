import pygame 

pygame.init()
WIDTH= 900
HEIGHT=900
screen= pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Bishop\'sPlayground(Testing)')
font= pygame.font.Font('freesansbold.ttf', 20)
big_font= pygame.font.Font('freesansbold.ttf', 50)
timer= pygame.time.Clock()
fps= 60

#game variables and images setting up
colour=(112, 128, 144)
white_pieces=['rook','knight','bishop','king','queen','bishop','knight','rook',
              'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

white_locations=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                 (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

black_pieces=['rook','knight','bishop','king','queen','bishop','knight','rook',
              'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

black_locations=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                 (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

captured_pieces_white=[]
captured_pieces_black=[]

#The turn variable keeps a track: 0->Whites turn, no selection, 1->Whites turn, piece selection, 2-> Black's turn, no selection, 3->Black's turn, piece selection.
#This is to make sure what phase of game we are on, which move is the last-what legal move is being played.
turn=0
#which piece currently selected, this is found out based on the index in the list
#initialised as a large number so it does not fall under the indices of any of the lists.
selection=100
valid_moves=[]

#load in the images for the pieces


#main game loop
run= True
while run:
    timer.tick(fps)
    screen.fill(colour)
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        
    pygame.display.flip()
pygame.quit()