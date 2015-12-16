# import the relevant libraries
import time
import pygame
import pygame.camera
from pygame.locals import *
# this is where one sets how long the script
# sleeps for, between frames.
sleeptime__in_seconds = 0.05
# initialise the display window
screen = pygame.display.set_mode(FULLSCREEN)
pygame.init()
pygame.camera.init()
# set up a camera object
cam = pygame.camera.Camera("/dev/video0",(640,480))
# start the camera
cam.start()

while 1:

    # sleep between every frame
    time.sleep( sleeptime__in_seconds )
    # fetch the camera image
    image = cam.get_image()
    # blank out the screen
    screen.fill([0,0,0])
    # copy the camera image to the screen
    screen.blit( image, ( 100, 0 ) )
    # update the screen to show the latest screen image
    pygame.display.update()

"""import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
print(camlist)

if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))

class Capture(object):
    def __init__(self):
        self.size = (640,480)
        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)
        
        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check 
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # blit it to the display surface.  simple!
        self.display.blit(self.snapshot, (0,0))
        pygame.display.flip()

    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False

            self.get_and_flip()"""
