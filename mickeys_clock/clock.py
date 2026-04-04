import pygame
import datetime

class MickeyClock:
    def __init__(self):
        try:
            self.image = pygame.image.load('images/mickey_hand.png').convert_alpha()
        except FileNotFoundError:
            self.image = pygame.image.load('mickeys_clock/images/mickey_hand.png').convert_alpha()
        
        self.center_pos = (400, 400)
        
        self.mickey_body = pygame.transform.scale(self.image, (600, 600))
        self.hand_img = pygame.transform.scale(self.image, (600, 600))

    def rotate_hand(self, image, angle):
        rotated_image = pygame.transform.rotate(image, -angle)
        new_rect = rotated_image.get_rect(center=self.center_pos)
        return rotated_image, new_rect

    def update(self):
        now = datetime.datetime.now()
        self.sec_angle = now.second * 6
        self.min_angle = now.minute * 6

    def draw(self, screen):
        body_rect = self.mickey_body.get_rect(center=self.center_pos)
        screen.blit(self.mickey_body, body_rect)

        min_img, min_rect = self.rotate_hand(self.hand_img, self.min_angle)
        screen.blit(min_img, min_rect)

        sec_img, sec_rect = self.rotate_hand(self.hand_img, self.sec_angle)
        screen.blit(sec_img, sec_rect)