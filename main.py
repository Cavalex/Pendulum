import pygame
import random
import math
from pygame import time

from pygame.constants import AUDIO_ALLOW_CHANNELS_CHANGE

WIDTH = 1400
HEIGHT = 800

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum")
gravity = 1
damping = 0.995
pendulumAngle = math.pi/3
centerX = WIDTH / 2
centerY = (HEIGHT / 5) * 2
pendulumOuterRadius = 40
pendulumInnerRadius = 30
pendulumLineLength = 250
BACKGROUND_COLOR = (180,180,180)
OUTER_RADIUS_COLOR = (0,0,0)
INNER_RADIUS_COLOR = (80, 80, 80)
LINE_COLOR = (0,0,0)

class Pendulum:
    def __init__(self, angle, centerX, centerY, outerRadius, innerRadius, lineLength):
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.angle = angle
        self.lineLength = lineLength
        self.centerX = centerX
        self.centerY = centerY
        self.x = self.lineLength * math.sin(angle) + self.centerX
        self.y = self.lineLength * math.cos(angle) + self.centerY
        self.lineCenter = [self.centerX, self.centerY]
        self.lineLength = lineLength
        self.acceleration = 0
        self.velocity = 0

    def drawLine(self):
                         #surface, color, start_pos, end_pos
        pygame.draw.line(screen, LINE_COLOR, self.lineCenter, (self.x, self.y))

    def drawPendulum(self):
                           #surface, color, center, radius
        pygame.draw.circle(screen, OUTER_RADIUS_COLOR , (self.x, self.y), self.outerRadius)
        pygame.draw.circle(screen, INNER_RADIUS_COLOR , (self.x, self.y), self.innerRadius) # must come after the other

    def update(self):

        # https://www.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-oscillations/a/trig-and-forces-the-pendulum
        self.acceleration = (-1 * gravity / self.lineLength) * math.sin(self.angle) # http://www.myphysicslab.com/pendulum1.html
        self.velocity += self.acceleration
        self.velocity *= damping
        self.angle += self.velocity

        # updating the ball position
        self.x = self.lineLength * math.sin(self.angle) + centerX
        self.y = self.lineLength * math.cos(self.angle) + centerY

def main():

    velocity = 1 # 1 if the program is running, -1 if it's not
    running = True

    p = Pendulum(pendulumAngle, centerX, centerY, pendulumOuterRadius, pendulumInnerRadius, pendulumLineLength)

    # the main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    velocity = -velocity

        # update the pendulum path with time
        if velocity == 1:
            p.update()

        # Draw pendulums
        screen.fill(BACKGROUND_COLOR)
        p.drawLine()
        p.drawPendulum()

        #update the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


