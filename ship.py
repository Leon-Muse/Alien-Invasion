import pygame

class Ship:
    #THis is a class to manage the ship

    def __init__(self,ai_game):
        #Initilaize the ship and set its srtartin position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.get_rect()
        
        #load the ship image and get its rect
        self.image = pygame.image.load('/Users/omarmontoya/Alien-Invasion/images/rocket-147466_640.bmp')
        self.rect = self.image.get_rect()

        #movement flag
        self.moving_right = False

        #start each new ship at the bottom cetner of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        if self.moving_right:
            self.rect.x += 1
    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image,self.rect)