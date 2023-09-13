#Import del for brugerdefinerede klasser
from Classes.memocard import Memo
from Classes.trashcan import Trashcan

#Import del for pip pakker
import pygame


#Pygame setup
pygame.init()

screen_size = (screen_width, screen_height) = (1080,810)

main_window = pygame.display.set_mode(screen_size)


affald_piktogrammer = [
    #En liste med alle piktogrammerne
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


spande = []
spand_størrelse = ss = 150
i=0
while i < len(affald_piktogrammer):
    if i < 3:
        spande.append(Trashcan(i,((i%3+2)*screen_width/6)-(ss/2),50,ss,ss,affald_piktogrammer[i]))
    elif i < 6:
        spande.append(Trashcan(i,((i%3+2)*screen_width/6)-(ss/2),50+(ss+10),ss,ss,affald_piktogrammer[i])) 
    elif i < 9:
        spande.append(Trashcan(i,((i%3+2)*screen_width/6)-(ss/2),50+(ss+10)*2,ss,ss,affald_piktogrammer[i]))
    i+=1


skrald = [
    [r"Assets\Skrald\plastik_pose.png",7]
]

memo = Memo(100,100,100,100,skrald[0][0],skrald[0][1])

def redraw_screen(surface):
    """
    redraw_screen er den funktion hvor alt der skal være på skærmen bliver tegnet.
    Den tager en surface, som er en specifik pygame type, som input parameter.
    """
    surface.blit(pygame.image.load(r"Assets\ipad_frame.png"),pygame.Rect(0,0,1080,810))
    for spand in spande:
        spand.draw(surface)
    memo.draw(surface)
    pygame.display.flip()


def main(surface):
    """
    main er den funktion hvor alt koden kører i.
    Pygame har brug for et uendeligt loop mens programmet kører.
    main tager også en surface som input parameter.
    """
    running = True
    pressed = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    exit()
        if memo.is_pressed():
            pressed = True
            mouse_pos = pygame.mouse.get_pos()
            memo.x = mouse_pos[0]
            memo.y = mouse_pos[1]
            memo.rect = pygame.Rect(memo.x-memo.width/2, memo.y-memo.height/2, memo.width, memo.height)
        else:
            if pressed:
                for spand in spande:
                    if memo.is_colliding(spand.img_rect):
                        if memo.id == spand.id:
                            print("Yeah")
                            memo.x = 100
                            memo.y = 100
                            memo.rect = pygame.Rect(memo.x-memo.width/2, memo.y-memo.height/2, memo.width, memo.height)

        redraw_screen(surface)
main(main_window)