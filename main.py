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
#Black Images
#Queen
bq= pygame.image.load('/assets/images/bQ.png')
bq=pygame.image.scale(bq,(80,80))
bq_small=pygame.image.scale(bq,(65,65))
#King
bk= pygame.image.load('/assets/images/bK.png')
bk=pygame.image.scale(bk,(80,80))
bk_small=pygame.image.scale(bk,(65,65))
#Rook
br= pygame.image.load('/assets/images/bR.png')
br=pygame.image.scale(br,(80,80))
br_small=pygame.image.scale(br,(65,65))
#Knight
bn= pygame.image.load('/assets/images/bN.png')
bn=pygame.image.scale(bn,(80,80))
bn_small=pygame.image.scale(bn,(65,65))
#Pawn
bp= pygame.image.load('/assets/images/bP.png')
bp=pygame.image.scale(bp,(60,60))
bp_small=pygame.image.scale(bp,(45,45))
#Bishop
bb= pygame.image.load('/assets/images/bB.png')
bb=pygame.image.scale(bb,(80,80))
bb_small=pygame.image.scale(bb,(65,65))

#White Images
#Queen
wq= pygame.image.load('/assets/images/wQ.png')
wq=pygame.image.scale(wq,(80,80))
wq_small=pygame.image.scale(wq,(65,65))
#King
wk= pygame.image.load('/assets/images/wK.png')
wk=pygame.image.scale(wk,(80,80))
wk_small=pygame.image.scale(wk,(65,65))
#Rook
wr= pygame.image.load('/assets/images/wR.png')
wr=pygame.image.scale(wr,(80,80))
wr_small=pygame.image.scale(wr,(65,65))
#Knight
wn= pygame.image.load('/assets/images/wN.png')
wn=pygame.image.scale(wn,(80,80))
wn_small=pygame.image.scale(wn,(65,65))
#Pawn
wp= pygame.image.load('/assets/images/wP.png')
wp=pygame.image.scale(wp,(60,60))
wp_small=pygame.image.scale(wp,(45,45))
#Bishop
wb= pygame.image.load('/assets/images/wB.png')
wb=pygame.image.scale(wb,(80,80))
wb_small=pygame.image.scale(wb,(65,65))


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