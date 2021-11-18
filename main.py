import math
import threading
import random
import time
import pygame

##########
# Colors #
##########

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


########################
# Simulation variables #
########################

FORREST = []
speed = 0.02
screen_size = (900, 900)
general_probability = 0.53
h = 100
l = 100
size = min([math.ceil(screen_size[0] / l), math.ceil(screen_size[1] / h)])
# burned_cells = 0



#######################
# Animation variables #
#######################

ASHES = 2
FIRE = 1
FRESH = 0
padding_x = 0
padding_y = 0


class Case:
    def __init__(self, value, x,y, modified):
        self.value = value
        self.x = x
        self.y = y
        self.modified = 0
    def __repr__(self):
        return (str ((self.x, self.y)))
    def burn(self):
        if self.value == FRESH:
            self.value = FIRE
        elif self.value == FIRE:
            self.value = ASHES
            global burned_cells
            burned_cells += 1

    def burn_by_probability(self, probability):
        if (self.modified == 0):
            if random.random() <= probability:
                if(self.value  == FRESH):
                    self.burn()
                    self.modified = 1

    def draw(self, screen):
        if self.value == FRESH:
            pygame.draw.rect(screen, GREEN, pygame.Rect((self.y * size)+ math.floor(size/10)+ padding_y, (self.x * size) + math.floor(size /10) + padding_x,
                                                        size - math.floor(size /5), size - math.floor(size /5)) )
        elif self.value == FIRE:
            pygame.draw.rect(screen, RED, pygame.Rect((self.y * size)+math.floor(size /10)  + padding_y, (self.x * size) + math.floor(size /10) +
                                                      padding_x, size - math.floor(size /5), size - math.floor(size /5)))
        else:
            pygame.draw.rect(screen, GREY, pygame.Rect((self.y * size)+math.floor(size/10) + padding_y, (self.x * size) + math.floor(size /10) +
                                                       padding_x, size - math.floor(size /5), size - math.floor(size /5)))

def from_coordinate_to_cell(x, y):
    if (x <= padding_y):
        x = padding_y + 1
    if y <= padding_x :
        y = padding_x + 1
    if x >= padding_y + (size * l) :
        x = padding_y + (size * l) - 1
    if y >= padding_x + (size * h) :
        y = padding_x + (size * h) - 1
    real_x = math.floor (( y - (padding_x) )/ (size ))
    real_y = math.floor( (x - (padding_y) ) /  (size ))

    return (int (real_y),int (real_x))




def draw_forrest( screen):
    screen.fill(WHITE)
    for i in range (len(FORREST)):
        for j in range (len (FORREST[0])):
            FORREST[i][j].draw(screen)
    pygame.display.flip()

def init_forest(hauteur,largeur):
    global FORREST, h, l, size, speed,general_probability,burned_cells, padding_x, padding_y, zoom_out,zoom_in
    FORREST = []
    burned_cells = 0
    cfg_file = open("config.txt",'r')
    cfg_params = cfg_file.readlines()
    h = int(cfg_params[0].split("=")[1])
    l = int(cfg_params[1].split("=")[1])
    speed = float(cfg_params[2].split("=")[1])
    general_probability = float(cfg_params[3].split("=")[1])

    cfg_file.close()


    for x in range(h):
        FORREST.append([])
        for y in range(l):
            case = None
            if(  y == l//2 and x == h//2):
                case = Case(FIRE, x, y, 0)
                print(x,y)
            else:
                case = Case(FRESH, x, y, 0)
            FORREST[-1].append(case)
    pygame.init()
    # size_screen = (900, 900)

    size = min([int(screen_size[0] / l), int(screen_size[1] / h)])

    if (size == int(screen_size[0] / l)):
        padding_y = ((screen_size[0] - size * l)/2)
        padding_x = (screen_size[1] - size * h)/2
    else:
        padding_y = (screen_size[0] - size * l)/2
        padding_x = (screen_size[1] - size * h)/2

    zoom_in = int( max([h, l]) / 2)
    zoom_out = 0


    # size = size_screen[0] //h




def next_step():

    list_burning_cells = []
    for line in FORREST:
        for cell in line:
            # time.sleep(0.5)
            if (cell.value == FIRE):
                burning_cell = Case(cell.value, cell.x, cell.y, 1)
                list_burning_cells.append(burning_cell)
                cell.burn()

    # print(list_burning_cells)

    for cell in list_burning_cells:
                if cell.x == 0:
                    if cell.y == 0:

                            FORREST[cell.x+1][cell.y].burn_by_probability(general_probability)

                            FORREST[cell.x][cell.y+1].burn_by_probability(general_probability)
                    elif cell.y == l-1:

                            FORREST[cell.x + 1][cell.y].burn_by_probability(general_probability)

                            FORREST[cell.x][cell.y - 1].burn_by_probability(general_probability)
                    else:

                            FORREST[cell.x + 1][cell.y].burn_by_probability(general_probability)

                            FORREST[cell.x][cell.y + 1].burn_by_probability(general_probability)

                            FORREST[cell.x][cell.y - 1].burn_by_probability(general_probability)
                elif cell.x == h-1:
                    if cell.y == 0:

                            FORREST[cell.x - 1][cell.y].burn_by_probability(general_probability)

                            FORREST[cell.x][cell.y + 1].burn_by_probability(general_probability)
                    elif cell.y == l-1:
                        FORREST[cell.x - 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x ][cell.y -1].burn_by_probability(general_probability)
                    else:
                        FORREST[cell.x - 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x][cell.y + 1].burn_by_probability(general_probability)
                        FORREST[cell.x][cell.y - 1].burn_by_probability(general_probability)
                else:
                    if cell.y == 0:
                        FORREST[cell.x + 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x - 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x][cell.y + 1].burn_by_probability(general_probability)
                    elif cell.y == l - 1:
                        FORREST[cell.x + 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x - 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x][cell.y - 1].burn_by_probability(general_probability)
                    else:
                        FORREST[cell.x + 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x - 1][cell.y].burn_by_probability(general_probability)
                        FORREST[cell.x][cell.y - 1].burn_by_probability(general_probability)
                        FORREST[cell.x][cell.y + 1].burn_by_probability(general_probability)

    return len (list_burning_cells)




def  start_fire():
    i = 0
    number_burning_cells = next_step()
    ashes = 0
    while (number_burning_cells > 0):
        time.sleep(speed)
        number_burning_cells = next_step()
    for line in FORREST:
        for cell in line:
            if (cell.value == ASHES):
                ashes += 1
    print("number of burned cells = " + str(ashes))
    print(str((ashes/ (l * h)) * 100 ) +"% of the forrest has burned.")



def main():
    init_forest(h,l)
    screen = pygame.display.set_mode(screen_size)
    screen.fill(WHITE)
    draw_forrest(screen)
    done = False
    clock = pygame.time.Clock()


    while (not done):
        draw_forrest(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif pygame.mouse.get_pressed()[0]:
                    x,y = pygame.mouse.get_pos()
                    x1,y1 = from_coordinate_to_cell(x,y)
                    FORREST[y1][x1].value = FIRE
            elif pygame.mouse.get_pressed()[2]:
                    x, y = pygame.mouse.get_pos()
                    x1, y1 = from_coordinate_to_cell(x, y)
                    FORREST[y1][x1].value = ASHES
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    t1 = threading.Thread(target=lambda: start_fire())
                    # list_threads.append(t1)
                    t1.daemon = True
                    t1.start()

                elif event.key == pygame.K_r:
                    init_forest(h, l)

        clock.tick(60)

if __name__ == '__main__':
    main()


