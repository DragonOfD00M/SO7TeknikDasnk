import pygame
pygame.init()
class Trash:
    def __init__(self, x: int, y: int, width: int, height: int, image_path: str, id: int) -> None:
        
        #Gemmer parametrene som i klassen
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
        #Loader billedet af skrald og gør det den ordenlige størrelse
        self.img = pygame.image.load(image_path)
        self.img = pygame.transform.scale(self.img,(self.width,self.height))
        self.id = id

    def draw(self,surface: pygame.Surface) -> None:
        #Tegner billedet på kanvas
        surface.blit(self.img,self.rect)
    
    def replace_image(self, image_path: str, id: int) -> None:
        #Bytter om på værdierne for klassens billede
        self.img = pygame.image.load(image_path)
        self.img = pygame.transform.scale(self.img,(self.width,self.height))
        self.id = id

    def is_pressed(self) -> bool:
        #Tjekker om der er trykket på skraldet

        mouse_pos = pygame.mouse.get_pos() #Finder musens position
        mouse_press = pygame.mouse.get_pressed(3)[0] #Bolsk værdi om m1 er trykket ned
        
        #Herunder: Er mousen oven på billedet og er m1 trykket ned
        if self.rect.collidepoint(mouse_pos) and mouse_press == True:
            return True
        else:
            return False

    def is_colliding(self, rect: pygame.Rect) -> bool:
        #Tjekker om en input parameter rect rør ved skraldet
        if self.rect.colliderect(rect):
            return True
        else:
            return False