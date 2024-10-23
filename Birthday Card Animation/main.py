
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Birthday Card!!!!!!") # setting a title in pygame

width = 600
height = 600

# step 1 - Loading Image, step 2 - Setting Image : [this is for all images]

# -- loading ...

image = pygame.image.load("backgroundone.jpg") # - must add end extension [ex. .jpg, .png]
image2 = pygame.image.load("backgroundtwo.jpg")
image3 = pygame.image.load("backgroundthree.jpg")

# -- scaling image to make it fit the screen []

image = pygame.transform.scale(image,(width,height))
image2 = pygame.transform.scale(image2,(width,height))
image3 = pygame.transform.scale(image3,(width,height))

while True:
# -- displaying text ___
    font1=pygame.font.SysFont("Times New Roman",50)
    text1=font1.render("Happy Birthday!",True,(0,0,0))
# -- displaying image (^U^)>
    screen.fill("white")
    screen.blit(image,(0,0))
    screen.blit(text1,(150,250))
    
    pygame.display.update()

    time.sleep(2)
    font2 = pygame.font.SysFont("Arial", 35)
    text2 = font2.render("May all your birthday wishes come true :D", True, (0,0,0))
    screen.fill("white")
    screen.blit(image2,(0,0))
    screen.blit(text2, (25,50))
    pygame.display.update()

    time.sleep(2)

    font3 = pygame.font.SysFont("Calibri", 30)
    text3 = font3.render("You are 1 day OLDER than you were yesterday!!", True, (0,0,0))
    screen.fill("white")
    screen.blit(image3,(0,0))
    screen.blit(text3,(15,500))
    pygame.display.update()

    time.sleep(2)
