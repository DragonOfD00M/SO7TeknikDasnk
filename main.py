#Import del for brugerdefinerede klasser
from Classes.trashcard import Trash
from Classes.trashcan import Trashcan

#Import del for pip pakker
import pygame
import time
import math
import random

#Pygame setup
pygame.init()
font = pygame.font.Font(r"c:\WINDOWS\Fonts\INKFREE.TTF",60)
screen_size = (screen_width, screen_height) = (1080,810)
main_window = pygame.display.set_mode(screen_size)


#Setup af globale variabler og lister
score = 0 #Spillerens score
file = open(r"Highscore.txt","r")
highscore = file.read()
highscore = int(highscore)
file.close()

    
affald_piktogrammer = [ #En liste med alle piktogrammerne
    r"Assets\Affaldssortering piktogrammer\Farligt Affald.png",
    r"Assets\Affaldssortering piktogrammer\Glas.png",
    r"Assets\Affaldssortering piktogrammer\Mad- og Drikkekartoner.png",
    r"Assets\Affaldssortering piktogrammer\Mad.png",
    r"Assets\Affaldssortering piktogrammer\Metal.png",
    r"Assets\Affaldssortering piktogrammer\Pap.png",
    r"Assets\Affaldssortering piktogrammer\Papir.png",
    r"Assets\Affaldssortering piktogrammer\Plast.png",
    r"Assets\Affaldssortering piktogrammer\Restaffald.png"
]

#Følgende loop fylder listen spande, med det brugerdefinerede object Trashcan.
#Der bliver lavet 3 rækker med 3 spande i hver
spande = []
spand_størrelse = 150
i=0
while i < len(affald_piktogrammer):
    if i < 3:
        spande.append(Trashcan(i,((i%3+2)*screen_width/6)-(spand_størrelse/2),50,spand_størrelse,spand_størrelse,affald_piktogrammer[i]))
    elif i < 6:
        spande.append(Trashcan(i,((i%3+2)*screen_width/6)-(spand_størrelse/2),50+(spand_størrelse+10),spand_størrelse,spand_størrelse,affald_piktogrammer[i])) 
    elif i < 9:
        spande.append(Trashcan(i,((i%3+2)*screen_width/6)-(spand_størrelse/2),50+(spand_størrelse+10)*2,spand_størrelse,spand_størrelse,affald_piktogrammer[i]))
    i+=1


skrald_stykke = [ 
    #En liste der indeholder en masse lister. Den indre liste indeholder fil pathen til et billede af skrald og et indexnummer baseret
    #på hvilken skraldespand det skal i.
    #Farligt Affald
    [r"Assets\Skrald\batteri.png",0],
    [r"Assets\Skrald\spary_dåse.png",0],
    #Glas
    [r"Assets\Skrald\drikke_glas.png",1],
    [r"Assets\Skrald\marmelade.png",1],
    #Madaffald
    [r"Assets\Skrald\æble.png",3],
    [r"Assets\Skrald\banan.png",3],
    [r"Assets\Skrald\pizza_slice.png",3],
    #Metal
    [r"Assets\Skrald\tuborg.png",4],
    [r"Assets\Skrald\gaffel.png",4],
    #Plastik
    [r"Assets\Skrald\plastik_pose_1.png",7],
    [r"Assets\Skrald\plastik_pose_2.png",7],
    [r"Assets\Skrald\plastik_flaske.png",7],
    #Restaffald
    [r"Assets\Skrald\chips.png",8],
    [r"Assets\Skrald\pizza_box.png",8]
]

random_index = random.randint(0,len(skrald_stykke)-1) 
skrald = Trash(screen_width/2-50,screen_height-150,100,100,skrald_stykke[random_index][0],skrald_stykke[random_index][1]) #Her laves selve skraldet som skal sorteres

clock = (5,0)

previous_time = 0

def timer(clock: tuple[int,int]) -> str:
    global previous_time
    if previous_time == 0:
        previous_time = math.floor(time.time())
    if math.floor(time.time()) == previous_time+1:
        if clock[1] == 0:
            clock = clock = (clock[0]-1,59)
        else:
            clock = (clock[0],clock[1]-1)
        previous_time = 0
    return f"{clock[0]}:{clock[1]}",clock



def redraw_screen(surface: pygame.Surface):
    global clock
    """
    redraw_screen er den funktion hvor alt der skal være på skærmen bliver tegnet.
    Den tager en surface, som er en specifik pygame type, som input parameter.
    """
    
    #Herunder defineres teksten der fremviser scoren
    score_text = font.render(f"Score: {score}",True,(0,0,0)) #Teksten er Score: efterfuglt af scoren og den er sort
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (screen_width-score_text_rect.width/2-55,50+score_text_rect.height)
    
    
    #Herunder defineres teksten der fremviser highscoren
    highscore_text = font.render(f"Highscore: {highscore}", True, (0,0,0)) #Teksten er Highscore: efterfuglt af highscoren og den er sort
    highscore_text_rect = highscore_text.get_rect()
    highscore_text_rect.center = (screen_width-highscore_text_rect.width/2-55,screen_height-highscore_text_rect.height-50)

    #Herunder defineres teksten der fremviser timeren
    clock_string, clock = timer(clock) #Kører brugerdefineret funktion timer
    clock_text = font.render(clock_string,True,(0,0,0)) #Teksten er sort og er formaten mm:ss
    clock_text_rect = clock_text.get_rect()
    clock_text_rect.center = (50+clock_text_rect.width,50+clock_text_rect.height)

    #Baggrunden tegnes
    surface.blit(pygame.transform.scale(pygame.image.load(r"Assets\background.png"),(980,710)),pygame.Rect(50,50,980,710))

    #Alle spandene tegnes
    for spand in spande:
        spand.draw(surface)

    #Skraldet tegnes
    skrald.draw(surface)

    #Teksten skrives på skærmen
    surface.blit(score_text,score_text_rect)
    surface.blit(highscore_text,highscore_text_rect)
    surface.blit(clock_text,clock_text_rect)
    
    #Der bliver lagt en ipad frame på
    surface.blit(pygame.image.load(r"Assets\ipad_frame.png"),pygame.Rect(0,0,1080,810))
    
    pygame.display.flip()


def main(surface: pygame.Surface):
    """
    main er den funktion hvor alt koden kører i.
    Pygame har brug for et uendeligt loop mens programmet kører.
    main tager også en surface som input parameter.
    """
    global score
    running = True
    pressed = False
    while running:
        for event in pygame.event.get(): #en standard del til pygame
            if event.type == pygame.QUIT: #Hvis du prøver at lukke vinduet
                running = False

            if event.type == pygame.KEYUP: #Hvis en knap bliver sluppet
                if event.key == pygame.K_ESCAPE: #Er knappen escape?
                    running = False

        if clock == (0,0): #Hvis tiden er løbet ud
            running = False

        if skrald.is_pressed(): #Trykker du på skraldet
            pressed = True
            mouse_pos = pygame.mouse.get_pos() #Find musens position
            #Herunder ændres skraldets koordinater til musens position
            skrald.x = mouse_pos[0]
            skrald.y = mouse_pos[1]
            skrald.rect = pygame.Rect(skrald.x-skrald.width/2, skrald.y-skrald.height/2, skrald.width, skrald.height)
        else:
            if pressed: #Er skraldet blevet sluppet
                for spand in spande: #Tjek alle skraldespande for følgende
                    if skrald.is_colliding(spand.img_rect): #Rør skraldet og skraldespanden
                        if skrald.id == spand.id: #Er det den rigige skraldespand
                            score+=1
                        else:
                            score-=1
                        #Herunder rykkes skraldet tilbage til startpositionen
                        random_index = random.randint(0,len(skrald_stykke)-1) 
                        skrald.x = screen_width/2-50
                        skrald.y = screen_height-150
                        skrald.rect = pygame.Rect(skrald.x, skrald.y, skrald.width, skrald.height)
                        #Billedet og skraldets id laves om til et nyt tilfældigt et.
                        skrald.replace_image(skrald_stykke[random_index][0],skrald_stykke[random_index][1])
        redraw_screen(surface)
    if score > highscore: #Er din score større en highscoren
        #Gem scoren i en fil
        file = open(r"Highscore.txt","w")
        file.write(f"{score}")
        file.close()
    
main(main_window)