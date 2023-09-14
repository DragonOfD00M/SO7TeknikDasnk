import pygame
class Trashcan:
    def __init__(self,number: int, top_left_x: int,top_y: int,top_width: int,height: int,image_path: int) -> None:
        self.id = number
        
        #Definere top venstre og højre hjørne af trapetsen
        self.top_left_x = top_left_x
        self.top_rigth_x = top_width+top_left_x
        self.top_y = top_y
        
        #Definere bund venstre og højre hjørne af trapetsen
        self.bot_left_x = top_left_x + top_width/5
        self.bot_right_x = self.bot_left_x + 3*top_width/5
        self.bot_y = top_y+height

        #Laver billedet af affaldspiktogrammet og placerer det i midten af trapetsen
        self.img = pygame.image.load(image_path)
        self.img = pygame.transform.scale(self.img,(2*top_width/3,2*height/3))
        self.img_rect = self.img.get_rect()
        self.img_rect.center = (top_width/2+top_left_x,top_y+height/2)


    def draw(self, surface: pygame.Surface) -> None:
        #Tegner polygonen og billedet på kanvas
        pygame.draw.polygon(surface, (0,80,0), ((self.top_left_x,self.top_y),(self.top_rigth_x,self.top_y),(self.bot_right_x,self.bot_y),(self.bot_left_x,self.bot_y)))
        surface.blit(self.img,self.img_rect)
