import pygame
import random
pygame.init()
screen = pygame.display.set_mode([805, 805])
pygame.display.set_caption("Snake")
going = True
dead = True
down = False
up = False
left = False
right = False
score = 0
highscore = 0
start = False
apples = 1
apple = []
speed = 6
movesnake = True
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
GREY = (125, 125, 125)
RED = (255, 0, 0)
PURPLE = (120, 81, 169)
YELLOW = (255, 255, 0)
style = "Classic"
font = pygame.font.SysFont("Times", 60)
smallfont = pygame.font.SysFont("Times", 15)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
while going:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and down == False or event.key == pygame.K_UP and down == False:
                up = True
                right = False
                left = False
            elif event.key == pygame.K_a and right == False or event.key == pygame.K_LEFT and right == False:
                left = True
                down = False
                up = False
            elif event.key == pygame.K_s and up == False or event.key == pygame.K_DOWN and up == False:
                down = True
                right = False
                left = False
            elif event.key == pygame.K_d and left == False or event.key == pygame.K_RIGHT and left == False:
                right = True
                down = False
                up = False
            #menu keys
            if event.key == pygame.K_1 and start == False:
                apples = 1
            if event.key == pygame.K_3 and start == False:
                apples = 3
            if event.key == pygame.K_5 and start == False:
                apples = 5
            if event.key == pygame.K_4 and start == False:
                speed = 4
            if event.key == pygame.K_6 and start == False:
                speed = 6
            if event.key == pygame.K_8 and start == False:
                speed = 8
            if event.key == pygame.K_c and start == False:
                style = "Classic"
            if event.key == pygame.K_p and start == False:
                style = "Poison"
            if event.key == pygame.K_r and start == False:
                style = "Ripe"
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
    screen.fill(WHITE)
    #Backend for snake
    if start == True:
        if dead == True:
            apple = []
            snake = [[random.randrange(0, 9), random.randrange(0, 9)]]
            for m in range(apples):
                apple.append([random.randrange(0, 9), random.randrange(0, 9), random.randrange(1, 9)])
            dead = False
            up = False
            down = False
            left = False
            right = False
            score = 0
            if style == "Poison":
                papple = []
                papple = [random.randrange(0, 9), random.randrange(0, 9)]
        if style == "Ripe":
            for a in range(len(apple)):
                apple[a][2] += 1
                if apple[a][0] == snake[0][0] and apple[a][1] == snake[0][1]:
                    if apple[a][2] < 10:
                        snake.append([snake[0][0], snake[0][1]])
                        score += 1
                        apple[a] = [random.randrange(0, 9), random.randrange(0, 9), 1]
                    elif apple[a][2] >= 10 and apple[a][2] < 40:
                        snake.append([snake[0][0], snake[0][1]])
                        snake.append([snake[0][0], snake[0][1]])
                        score += 2
                        apple[a] = [random.randrange(0, 9), random.randrange(0, 9), 1]
                    elif apple[a][2] >= 40 and len(snake) > 2:
                        for s in range(len(snake)):
                            if s > 0:
                                snake[s][0] = snake[s - len(snake) + 1][0]
                                snake[s][1] = snake[s - len(snake) + 1][1]
                        movesnake = False
                        snake.pop()
                        score -= 1
                        apple[a] = [random.randrange(0, 9), random.randrange(0, 9), 1]
                    elif apple[a][2] >= 40 and len(snake) < 2:
                        snake.append([snake[0][0], snake[0][1]])
                        score -= 1
                        apple[a] = [random.randrange(0, 9), random.randrange(0, 9), 1]
        if movesnake:
            for s in range(len(snake)):
                if s > 0:
                    snake[s][0] = snake[s - len(snake) + 1][0]
                    snake[s][1] = snake[s - len(snake) + 1][1]
        else:
            movesnake = True
        #Snake collision with apple
        for a in range(len(apple)):
            if snake[0][0] == apple[a][0] and snake[0][1] == apple[a][1] and style != "Ripe":
                score += 1
                snake.append([snake[0][0], snake[0][1]])
                while snake[0][0] == apple[a][0] and snake[0][1] == apple[a][1]:
                    apple[a] = [random.randrange(0, 9), random.randrange(0, 9), 0]
                if style == "Poison":
                    papple = [random.randrange(0, 9), random.randrange(0, 9)]
                    while snake[0][0] == papple[0] and snake[0][1] == papple[1]:
                        papple = [random.randrange(0, 9), random.randrange(0, 9)]
        for s in range(len(snake)):
            if s > 0:
                if style == "Poison":
                    if snake[s][0] == papple[0] and snake[s][1] == papple[1]:
                        while snake[s][0] == papple[0] and snake[s][1] == papple[1]:
                            papple = [random.randrange(0, 9), random.randrange(0, 9)]
                for a in range(len(apple)):
                    if snake[s][0] == apple[a][0] and snake[s][1] == apple[a][1]:
                        while snake[s][0] == apple[a][0] and snake[s][1] == apple[a][1]:
                            apple[a] = [random.randrange(0, 9), random.randrange(0, 9), 0]
                                      
        #Snake Movement
        if up:
            snake[0][1] -= 1
        if down:
            snake[0][1] += 1
        if left:
            snake[0][0] -= 1
        if right:
            snake[0][0] += 1
        if snake[0][0] > 9 or snake[0][1] > 9 or snake[0][0] < 0 or snake[0][1] < 0:
            dead = True
            start = False
        #Backend for grid
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        #Add snake position and apple position to grid if not dead
        if dead == False:
            for s in range(len(snake)):
                if s > 0:
                    grid[snake[s][0]][snake[s][1]] = 1
            if grid[snake[0][0]][snake[0][1]] == 1:
                dead = True
                start = False
            else:
                grid[snake[0][0]][snake[0][1]] = 3
            for a in range(len(apple)):
                if grid[apple[a][0]][apple[a][1]] == 2:
                    while grid[apple[a][0]][apple[a][1]] == 2:
                        apple[a] = [random.randrange(0, 9), random.randrange(0, 9), 0]
                else:
                    grid[apple[a][0]][apple[a][1]] = 2
            if style == "Poison":
                if grid[papple[0]][papple[1]] == 3:
                    dead = True
                    start = False
                else:
                    grid[papple[0]][papple[1]] = 4
            if style == "Ripe":
                for a in range(len(apple) - 1):
                    if apple[a][2] <= 15:
                        grid[apple[a][0]][apple[a][1]] = 5
                    elif apple[a][2] > 15 and apple[a][2] <= 40:
                        grid[apple[a][0]][apple[a][1]] = 2
                    elif apple[a][2] > 40:
                        grid[apple[a][0]][apple[a][1]] = 4
        #Decode grid
        for x in range(10):
            for y in range(10):
                if grid[y][x] == 0:
                    pygame.draw.rect(screen, GREY, (5 + (y * (5 + 75)), (5 + x * (5 + 75)), 75, 75))
                elif grid[y][x] == 1:
                    pygame.draw.rect(screen, DARKGREEN, (5 + (y * (5 + 75)), (5 + x * (5 + 75)), 75, 75))
                elif grid[y][x] == 2:
                    pygame.draw.rect(screen, RED, (5 + (y * (5 + 75)), (5 + x * (5 + 75)), 75, 75))
                elif grid[y][x] == 3:
                    pygame.draw.rect(screen, GREEN, (5 + (y * (5 + 75)), (5 + x * (5 + 75)), 75, 75))
                elif grid[y][x] == 4:
                    pygame.draw.rect(screen, PURPLE, (5 + (y * (5 + 75)), (5 + x * (5 + 75)), 75, 75))
                elif grid[y][x] == 5:
                    pygame.draw.rect(screen, YELLOW, (5 + (y * (5 + 75)), (5 + x * (5 + 75)), 75, 75))
        #Draw Score
    if score > highscore:
        highscore = score
    elif start == False:
        screen.fill(WHITE)
        start_string = "Click anywhere to start"
        strt = font.render(start_string, True, (0, 0, 0))
        strt_rect = strt.get_rect()
        strt_rect.centerx = screen.get_rect().centerx
        strt_rect.centery = screen.get_rect().centery
        screen.blit(strt, strt_rect)
        
        mode_string = "Settings Codes: 1, 3, 5 to change the number of apples; 4, 6, 8 to change the speed; c, p, r to change the mode"
        mde = smallfont.render(mode_string, True, (0, 0, 0))
        mde_rect = mde.get_rect()
        mde_rect.centerx = screen.get_rect().centerx
        mde_rect.y = screen.get_rect().centery + 40
        screen.blit(mde, mde_rect)
        
        md_string = "Apples: " + str(apples)
        md = font.render(md_string, True, (0, 0, 0))
        md_rect = md.get_rect()
        md_rect.x = 40
        md_rect.y = 80
        screen.blit(md, md_rect)

        spd_string = "Speed: " + str(speed)
        spd = font.render(spd_string, True, (0, 0, 0))
        spd_rect = spd.get_rect()
        spd_rect.x = 40
        spd_rect.y = 140
        screen.blit(spd, spd_rect)

        style_string = "Mode: " + str(style)
        styl = font.render(style_string, True, (0, 0, 0))
        styl_rect = styl.get_rect()
        styl_rect.x = 40
        styl_rect.y = 200
        screen.blit(styl, styl_rect)
        
    draw_string = "Score: " + str(score) + " High Score: " + str(highscore)
    text = font.render(draw_string, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 40
    text_rect.y = 20
    screen.blit(text, text_rect)
    pygame.display.update()
pygame.quit()
