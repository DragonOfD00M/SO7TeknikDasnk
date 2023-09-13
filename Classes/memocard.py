import pygame
pygame.init()
class Memo:
    def __init__(self, x, y, width, height, image_path, id) -> None:
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.img = pygame.image.load(image_path)
        self.img = pygame.transform.scale(self.img,(self.width,self.height))
        self.id = id

    def draw(self,surface) -> None:
        pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(self.img,self.rect)
    
    def is_pressed(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed(3)[0]
        if self.rect.collidepoint(mouse_pos) and mouse_press == True:
            return True
        else:
            return False

    def is_colliding(self, rect) -> bool:
        if self.rect.colliderect(rect):
            return True
        else:
            return False