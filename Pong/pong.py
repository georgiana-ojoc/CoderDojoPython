import pygame
from random import randint

pygame.init()
font = pygame.font.Font(None, 70)
black = (0, 0, 0)
white = (255, 255, 255)
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()


class Paddle:
    def __init__(self, left_top_x, left_top_y, width, height, color):
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.width = width
        self.height = height
        self.color = color
        self.shape = pygame.Rect(self.left_top_x, self.left_top_y, self.width, self.height)
        self.object = pygame.draw.rect(screen, self.color, self.shape)
        self.score = 0

    def draw(self):
        self.object = pygame.draw.rect(screen, self.color, self.shape)

    def move(self, pixels):
        self.left_top_y += pixels
        if self.left_top_y < 0:
            self.left_top_y = 0
        elif self.left_top_y > screen_height - self.height:
            self.left_top_y = screen_height - self.height
        self.shape = pygame.Rect(self.left_top_x, self.left_top_y, self.width, self.height)


class Ball:
    def __init__(self, center_x, center_y, radius, color):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.pixels_x = randint(4, 8)
        self.pixels_y = randint(-8, 8)
        self.object = pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)

    def draw(self):
        self.object = pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)

    def move(self):
        self.center_x += self.pixels_x
        self.center_y += self.pixels_y

    def bounce(self):
        self.pixels_x *= -1
        self.pixels_y = randint(-8, 8)


def main():
    left_paddle = Paddle(20, 200, 10, 100, white)
    right_paddle = Paddle(670, 200, 10, 100, white)
    ball = Ball(350, 250, 10, white)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move(-5)
        elif keys[pygame.K_s]:
            left_paddle.move(5)
        elif keys[pygame.K_UP]:
            right_paddle.move(-5)
        elif keys[pygame.K_DOWN]:
            right_paddle.move(5)

        if pygame.Rect.colliderect(ball.object, left_paddle.object) or \
                pygame.Rect.colliderect(ball.object, right_paddle.object):
            ball.bounce()
        if ball.center_x <= ball.radius:
            right_paddle.score += 1
            ball.pixels_x *= -1
        if ball.center_x >= screen_width - ball.radius:
            left_paddle.score += 1
            ball.pixels_x *= -1
        if ball.center_y <= ball.radius or ball.center_y >= screen_height - ball.radius:
            ball.pixels_y *= -1
        ball.move()

        screen.fill(black)
        left_paddle.draw()
        right_paddle.draw()
        ball.draw()
        pygame.draw.line(screen, white, [349, 0], [349, 500], 6)
        text = font.render(str(left_paddle.score), True, white)
        screen.blit(text, (289, 10))
        text = font.render(str(right_paddle.score), True, white)
        screen.blit(text, (385, 10))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
