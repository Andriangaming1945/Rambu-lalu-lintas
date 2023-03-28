import pygame
import button
import datetime
Waktu = datetime.datetime.now()

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")
Main_menu = Waktu


#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40) 

#define colours
TEXT_COL = (0, 0, 255)

#load button images
resume_img = pygame.image.load("button_resume.png").convert_alpha()


print("\nTime minutes you've been playing this game = ",Waktu) 

quit_img = pygame.image.load("button_quit.png").convert_alpha()



#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if (screen):
        print("Resume")
  
  else:
    draw_text("Press SPACE to start", font, TEXT_COL, 160, 250)
    draw_text("Press X for back", font, TEXT_COL, 160, 160)
    

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE: import prototype_game
      game_paused = True
    if event.type == pygame.QUIT: 
     run = False
    if event.type == pygame.QUIT:
      game_paused()

  pygame.display.update()

# inisialisasi Pygame dan mixer
pygame.init()
pygame.mixer.init()

# mengatur ukuran layar
# menambahkan background music
 # -1 artinya musik akan diputar secara berulang-ulang

# menjalankan game loop
while True:
    # mendeteksi event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # keluar dari game loop
            pygame.quit()
            quit()


