import pygame
from settings import *
from point import Point, draw_point, draw_line
from sys import exit



pygame.init()

def main() -> None:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bezier Curves")
    clock = pygame.time.Clock()
    
    p1 = Point(50, 50, BLUE)
    p2 = Point(100, 150, GREEN)
    p3 = Point(400, 200, BLUE)
    selected = None

    points = [p1, p2, p3]
    curve_points = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exit Succesfully")
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, point in enumerate(points):
                        if point.rect.collidepoint(event.pos):
                            selected = num
                            print(f"Selected Point: {selected}")


            elif event.type == pygame.MOUSEMOTION:
                if selected != None:
                    points[selected].x += event.rel[0]
                    points[selected].y += event.rel[1]
                    curve_points = []
                    for i in range(1, 10):
                        t = i / 10
                        pb = B(p1, p2, p3, t)
                        curve_points.append(pb)



        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and selected != None:
                    print(f"Released Point: {selected}")
                    selected = None


        screen.fill(BLACK)
        
        draw_screen(screen, points, curve_points)
        pygame.display.update()
        clock.tick(FPS)
        

def draw_screen(screen, points, curve_points):
   # for i in range(1, len(points)):
    #    draw_line(screen, points[i - 1], points[i], BLUE)

    for i in range(len(points)):
        points[i].rect = draw_point(screen, points[i])

    for i in range(len(curve_points)):
        curve_points[i].rect = draw_point(screen, curve_points[i])

    
def B(p1, p2, p3, t=0.5) -> Point:
    xp = 0
    yp = 0
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y

    xp = x2 + (1-t)**2 * (x1 - x2) + t**2 * (x3 - x2)
    yp = y2 + (1-t)**2 * (y1 - y2) + t**2 * (y3 - y2)
    
    return Point(xp, yp, RED)

if __name__ == "__main__":
    main()
