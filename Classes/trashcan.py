import pygame
class Trashcan:
    def __init__(self,number,top_left_x,top_y,top_width,height,image_path) -> None:
        self.id = number
        
        self.top_left_x = top_left_x
        self.top_rigth_x = top_width+top_left_x
        self.top_y = top_y
        
        
        self.bot_left_x = top_left_x + top_width/5
        self.bot_right_x = self.bot_left_x + 3*top_width/5
        self.bot_y = top_y+height

        self.img = pygame.image.load(image_path)
        self.img = pygame.transform.scale(self.img,(2*top_width/3,2*height/3))
        self.img_rect = self.img.get_rect()
        self.img_rect.center = (top_width/2+top_left_x,top_y+height/2)


    def draw(self, surface) -> None:
        pygame.draw.polygon(surface, (0,80,0), ((self.top_left_x,self.top_y),(self.top_rigth_x,self.top_y),(self.bot_right_x,self.bot_y),(self.bot_left_x,self.bot_y)))
        surface.blit(self.img,self.img_rect)
