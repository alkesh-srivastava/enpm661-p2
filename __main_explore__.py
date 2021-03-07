import pygame
import maze
import matplotlib.pyplot as plt
WIDTH, HEIGHT = 500, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project 2 - Testudo on a Hunt!")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128,128,128)
print("Please enter the amount of frames you want to render per second: \n(e.g. 60, I'll recommend anything over 1000)")
_input_fps = int(input())
FPS = _input_fps
TESTUDO = pygame.image.load('images/testudo.png')
TESTUDO_RESIZE = pygame.transform.scale(TESTUDO, (10, 10))
BACKGROUND = pygame.image.load('images/Path_1_1.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (401, 301))
x_offset = 49
y_offset = 300
y_upper_offset = 50
global initial_testudo


def draw_window(rect):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (50, 50))
    WIN.blit(TESTUDO_RESIZE, (rect.x, rect.y))
    pygame.draw.circle(WIN, GREEN, [x_offset + goal_x, (y_offset - goal_y) + y_upper_offset], 10)
    pygame.draw.rect(WIN, BLACK, (50, 50, 400, 300), 3)



def main():
    player = pygame.Rect(x_offset, y_offset + y_upper_offset, 0, 0)

    clock = pygame.time.Clock()
    run = True
    counter = 0
    while run:
        try:

            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if counter == 0:
                player.x = x_offset + exploration[counter][0]
                player.y = y_offset -exploration[counter][1] + y_upper_offset

            if counter > 1:
                player.x = x_offset + exploration[counter][0]
                player.y = y_offset - exploration[counter][1] + y_upper_offset


            pygame.display.update()
            draw_window(player)
            counter = counter + 1
            if counter > counter_stop:
                pygame.time.wait(0)

        except:
            run = False
            pygame.quit()

    pygame.quit()


if __name__ == '__main__':
    print("Input Start Position for Testudo :\nX Co-ordinate :")
    testudo_x = int(input())
    if testudo_x > 400 or testudo_x < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()
    print("Y Co-ordinate :")
    testudo_y = int(input())
    if testudo_y > 300 or testudo_x < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()
    print("Input Goal Position for Testudo :\nX Co-ordinate :")
    goal_x = int(input())
    if goal_x > 400 or goal_x < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()
    print("Y Co-ordinate :")
    goal_y = int(input())

    if goal_y > 300 or goal_y < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()

    puzzle = [[''] * 400] * 300
    try:
        exploration = maze.explored_path(puzzle, (testudo_x, testudo_y), (goal_x, goal_y))
        counter_stop = len(exploration)
        testudo_pos_x = x_offset + testudo_x
        testudo_pos_y = (y_offset - testudo_y) + y_upper_offset
        initial_testudo = (testudo_pos_x, testudo_pos_y)
        print("Testudo explored the following path before making a final decision:\n",str(exploration))
        main()
        x_a = list()
        y_a = list()
        x_b = list()
        y_b = list()
        x_c = list()
        y_c = list()
        x_d = list()
        y_d = list()
        x_e = list()
        y_e = list()
        x_f = list()
        y_f = list()
        x_g = list()
        y_g = list()
        x_h = list()
        y_h = list()
        explore_x = list()
        explore_y = list()
        exploration_list = exploration
        for x in exploration_list:
            explore_x.append(x[0])
            explore_y.append(x[1])
        for x in range(0, 400):
            for y in range(0, 300):
                if ((x - 90) ** 2 + (y - 70) ** 2) <= (35 ** 2):
                    x_a.append(x)
                    y_a.append(y)
        for x in range(0, 400):
            for y in range(0, 300):
                if (y >= 0.7 * x + 74.4) and \
                        (y >= -1.42 * x + 176.16) and \
                        (y <= -1.42 * x + 436.82) and \
                        (y <= 0.7 * x + 97.18):
                    x_b.append(x)
                    y_b.append(y)
        for x in range(0, 400):
            for y in range(0, 300):
                if ((x - 246) ** 2) / (60 ** 2) + (y - 145) ** 2 / (30 ** 2) <= 1:
                    x_c.append(x)
                    y_c.append(y)

        for x in range(0, 328 + int(75 / 1.414)):
            for y in range(0, 300):
                if (
                        (y >= x - 265) and
                        (y >= 391 - x) and
                        # (y <= x - 210)  and
                        (y <= x - 265 + 60 * 1.414) and
                        (y <= (x - 328) * (-0.36397023426) + 145.07)

                ):
                    x_d.append(x)
                    y_d.append(y)
        for x in range(347, 328 + int(75 / 1.414)):
            for y in range(0, 172):
                if (y > (x - 328) * (-0.36397023426) + 145.07313811473279 and y < x - 210):
                    x_e.append(x)
                    y_e.append(y)

        for x in range(200, 210):
            for y in range(240, 270):
                x_f.append(x)
                y_f.append(y)

        for x in range(200, 230):
            for y in range(230, 240):
                x_g.append(x)
                y_g.append(y)

        for x in range(200, 230):
            for y in range(270, 280):
                x_h.append(x)
                y_h.append(y)

        plt.plot(explore_x, explore_y, '#008080')
        plt.plot(x_a, y_a, '#615FB6')
        plt.plot(x_b, y_b, '#615FB6')
        plt.plot(x_c, y_c, '#615FB6')
        plt.plot(x_d, y_d, '#615FB6')
        plt.plot(x_e, y_e, '#615FB6')
        plt.plot(x_f, y_f, '#615FB6')
        plt.plot(x_g, y_g, '#615FB6')
        plt.plot(x_h, y_h, '#615FB6')

        plt.show()


    except:
            print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
            raise SystemExit()
