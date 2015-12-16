#! /usr/bin/env python
"""Deathstar takes a camera feed from a USB camera (using pygame) and spits it out onto
a 480 x 320 monitor which is attached to a helmet, showing the cameras path through a 
rotating felt Death Star

This code borrows heavily from pygame.cam example and also includes other example code
"""


# import the relevant libraries
import time
import pygame
import pygame.camera
from pygame.locals import *
# this is where one sets how long the script
# sleeps for, between frames.
sleeptime__in_seconds = 0.05
# initialise the display window
screen = pygame.display.set_mode((480, 320),FULLSCREEN)
pygame.init()
pygame.camera.init()
# set up a camera object
cam = pygame.camera.Camera("/dev/video0",(320,240))
# start the camera
cam.start()

try:
    while 1:

    # sleep between every frame
        time.sleep( sleeptime__in_seconds )
    # fetch the camera image
        image = cam.get_image()
    # blank out the screen
        screen.fill([0,0,0])
    # copy the camera image to the screen
        screen.blit( image, ( 0, 20 ) )
    # update the screen to show the latest screen image
        pygame.display.update()

        events = pygame.event.get()
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                # close the camera safely
                cam.stop()
                pygame.quit()
