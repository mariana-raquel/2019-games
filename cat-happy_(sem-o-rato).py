import pygame
pygame.init()
screen = pygame.display.set_mode([640, 640])
pygame.display.set_caption("Cat Happy")

x = -10 # x do personagem
y = 352 # y do personagem
x1 = 150 # x da moeda1
y1 = 420 # y da moeda1
x2 = 350 # x da moeda2
y2 = 420 # y da moeda2
x3 = 550 # x da moeda3
y3 = 380 # y da moeda3
x4 = 90 # x da moeda4
y4 = 380 # y da moeda4
x5 = 300 # x da moeda5
y5 = 300 # y da moeda5
x6 = 550 # x da moeda6
y6 = 380 # y da moeda6
x7 = 310 # x do baú
y7 = 235 # y do baú

def mostrar_personagem(screen, x,y):
    image1 = pygame.image.load("Happy de frente.png")
    screen.blit(image1, (x, y))
    pygame.display.flip()

def mostrar_personagem2(screen, x,y):
    image2 = pygame.image.load("Happy com o peixe.png")
    screen.blit(image2, (x, y))
    pygame.display.flip()

def mostrar_rato(screen, x8, y8):
    rato = pygame.image.load("Ratâo.png")
    screen.blit(rato, (x8, y8))
    pygame.display.flip()

def mostrar_moeda1_c1(screen, x1,y1):
    image = pygame.image.load("moedinha.png")
    screen.blit(image, (x1, y1))
    pygame.display.flip()

def mostrar_moeda2_c1(screen, x2,y2):
    image = pygame.image.load("moedinha.png")
    screen.blit(image, (x2, y2))
    pygame.display.flip()

def mostrar_moeda3_c1(screen, x3,y3):
    image = pygame.image.load("moedinha.png")
    screen.blit(image, (x3, y3))
    pygame.display.flip()

fundo3 = pygame.image.load("Cenario3.png")
screen.blit(fundo3, (0,0))
mostrar_personagem(screen, x, y)

fundo2 = pygame.image.load("Cenario2.png")
screen.blit(fundo2, (0,0))
mostrar_personagem(screen, x, y)
mostrar_moeda1_c1(screen, x4, y4)
mostrar_moeda2_c1(screen, x5, y5)
mostrar_moeda3_c1(screen, x6, y6)

fundo1 = pygame.image.load("Cenario1.png")
screen.blit(fundo1, (0,0))
mostrar_personagem(screen, x, y)
mostrar_moeda1_c1(screen, x1, y1)
mostrar_moeda2_c1(screen, x2, y2)
mostrar_moeda3_c1(screen, x3, y3)

explicações = pygame.image.load("Explicações.png")
screen.blit(explicações, (0,0))

continuar = True

while continuar:
    pygame.display.flip()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        continuar = False
    if 323 > x:
      if (event.type == pygame.KEYUP and event.key == pygame.K_UP):
          screen.blit(fundo1, (0, 0))
          y = y - 40
          mostrar_personagem(screen, x, y)
          y = y + 40
          x = x + 75
          screen.blit(fundo1, (0, 0))
          mostrar_personagem(screen, x, y)
          if x <= 80:
              mostrar_moeda1_c1(screen, x1, y1)
          if x <= 280:
              mostrar_moeda2_c1(screen, x2, y2)
          if x <= 480:
              mostrar_moeda3_c1(screen, x3, y3)
      pressionado = pygame.key.get_pressed()
      if pressionado[pygame.K_RIGHT]:
            screen.blit(fundo1, (0, 0))
            x = x + 3
            mostrar_personagem(screen, x, y)
            if x <= 80:
                mostrar_moeda1_c1(screen, x1, y1)
            if x <= 280:
                mostrar_moeda2_c1(screen, x2, y2)
            if x <= 480:
                mostrar_moeda3_c1(screen, x3, y3)
      elif pressionado[pygame.K_LEFT]:
            screen.blit(fundo1, (0, 0))
            x = x - 3
            mostrar_personagem(screen, x, y)
            if x <= 80:
                mostrar_moeda1_c1(screen, x1, y1)
            if x <= 280:
                mostrar_moeda2_c1(screen, x2, y2)
            if x <= 480:
                mostrar_moeda3_c1(screen, x3, y3)
    if y >= 332:
        if (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
            screen.blit(fundo1, (0, 0))
            x = x + 57
            y = y - 20
            mostrar_personagem(screen, x, y)
            if x <= 80:
                mostrar_moeda1_c1(screen, x1, y1)
            if x <= 280:
                mostrar_moeda2_c1(screen, x2, y2)
            if x <= 480:
                mostrar_moeda3_c1(screen, x3, y3)
    if 325 < x and y == 352:
        pressionado = pygame.key.get_pressed()
        if pressionado[pygame.K_RIGHT]:
            screen.blit(fundo1, (0, 0))
            x = x + 3
            mostrar_personagem(screen, x, y)
            if x <= 80:
                mostrar_moeda1_c1(screen, x1, y1)
            if x <= 280:
                mostrar_moeda2_c1(screen, x2, y2)
            if x <= 480:
                mostrar_moeda3_c1(screen, x3, y3)
        elif pressionado[pygame.K_LEFT]:
            screen.blit(fundo1, (0, 0))
            x = x - 3
            mostrar_personagem(screen, x, y)
            if x <= 80:
                mostrar_moeda1_c1(screen, x1, y1)
            if x <= 280:
                mostrar_moeda2_c1(screen, x2, y2)
            if x <= 480:
                mostrar_moeda3_c1(screen, x3, y3)
    elif y == 312 :
        pressionado = pygame.key.get_pressed()
        if pressionado[pygame.K_RIGHT]:
            screen.blit(fundo1, (0, 0))
            x = x + 3
            mostrar_personagem(screen, x, y)
            if x <= 80:
                mostrar_moeda1_c1(screen, x1, y1)
            if x <= 280:
                mostrar_moeda2_c1(screen, x2, y2)
            if x <= 480:
                mostrar_moeda3_c1(screen, x3, y3)
        elif pressionado[pygame.K_LEFT]:
            screen.blit(fundo1, (0, 0))
            x = x - 3
            mostrar_personagem(screen, x, y)
            if x <= 80:
                mostrar_moeda1_c1(screen, x1, y1)
            if x <= 280:
                mostrar_moeda2_c1(screen, x2, y2)
            if x <= 480:
                mostrar_moeda3_c1(screen, x3, y3)
    if 580 < x:
        def mostrar_moeda1_c2(screen, x4, y4):
            image = pygame.image.load("moedinha.png")
            screen.blit(image, (x4, y4))
            pygame.display.flip()

        def mostrar_moeda2_c2(screen, x5, y5):
            image = pygame.image.load("moedinha.png")
            screen.blit(image, (x5, y5))
            pygame.display.flip()

        def mostrar_moeda3_c2(screen, x6, y6):
            image = pygame.image.load("moedinha.png")
            screen.blit(image, (x6, y6))
            pygame.display.flip()
        continuar = True
        x = -60
        y = 317
        mostrar_personagem(screen, x, y)
        screen.blit(fundo2, (0, 0))
        while continuar:
            pygame.display.flip()
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                continuar = False
            if -17 > x:
                pressionado = pygame.key.get_pressed()
                if pressionado[pygame.K_RIGHT]:
                    screen.blit(fundo2, (0, 0))
                    x = x + 3
                    mostrar_personagem(screen, x, y)
                    if x <= 80:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 280:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 480:
                        mostrar_moeda3_c2(screen, x6, y6)
                elif pressionado[pygame.K_LEFT]:
                    screen.blit(fundo2, (0, 0))
                    x = x - 3
                    mostrar_personagem(screen, x, y)
                    if x <= 80:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 280:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 480:
                        mostrar_moeda3_c2(screen, x6, y6)
            if y >= 252:
                if (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
                    screen.blit(fundo2, (0, 0))
                    x = x + 57
                    y = y - 20
                    mostrar_personagem(screen, x, y)
                    if x <= 40:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 240:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 440:
                        mostrar_moeda3_c2(screen, x6, y6)
            elif y <= 252 and x < 310:
                pressionado = pygame.key.get_pressed()
                if pressionado[pygame.K_RIGHT]:
                    screen.blit(fundo2, (0, 0))
                    x = x + 3
                    mostrar_personagem(screen, x, y)
                    if x <= 40:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 240:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 440:
                        mostrar_moeda3_c2(screen, x6, y6)
                elif pressionado[pygame.K_LEFT]:
                    screen.blit(fundo2, (0, 0))
                    x = x - 3
                    mostrar_personagem(screen, x, y)
                    if x <= 40:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 240:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 440:
                        mostrar_moeda3_c2(screen, x6, y6)
            if x >=  310:
                if (event.type == pygame.KEYUP and event.key == pygame.K_DOWN):
                    screen.blit(fundo2, (0, 0))
                    x = x + 70
                    y = y + 20
                    mostrar_personagem(screen, x, y)
                    if x <= 40:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 240:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 440:
                        mostrar_moeda3_c2(screen, x6, y6)
            if x > 500:
                pressionado = pygame.key.get_pressed()
                if pressionado[pygame.K_RIGHT]:
                    screen.blit(fundo2, (0, 0))
                    x = x + 3
                    mostrar_personagem(screen, x, y)
                    if x <= 40:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 240:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 440:
                        mostrar_moeda3_c2(screen, x6, y6)
                elif pressionado[pygame.K_LEFT]:
                    screen.blit(fundo2, (0, 0))
                    x = x - 3
                    mostrar_personagem(screen, x, y)
                    if x <= 40:
                        mostrar_moeda1_c2(screen, x4, y4)
                    if x <= 240:
                        mostrar_moeda2_c2(screen, x5, y5)
                    if x <= 440:
                        mostrar_moeda3_c2(screen, x6, y6)
            if 580 < x:
                def mostrar_baú(screen, x7, y7):
                    image = pygame.image.load("Baú - 270x270.png")
                    screen.blit(image, (x7, y7))
                    pygame.display.flip()
                continuar = True
                x = -60
                y = 317
                mostrar_personagem(screen, x, y)
                screen.blit(fundo3, (0, 0))
                while continuar:
                    pygame.display.flip()
                    event = pygame.event.poll()
                    if event.type == pygame.QUIT:
                        continuar = False
                    pressionado = pygame.key.get_pressed()
                    if pressionado[pygame.K_RIGHT]:
                        screen.blit(fundo3, (0, 0))
                        mostrar_baú(screen, x7, y7)
                        x = x + 3
                        mostrar_personagem(screen, x, y)
                        if x >= 400:
                            mostrar_personagem2(screen, x, 317)
                    elif pressionado[pygame.K_LEFT]:
                        screen.blit(fundo3, (0, 0))
                        mostrar_baú(screen, x7, y7)
                        x = x - 3
                        mostrar_personagem(screen, x, y)
                        if x >= 400:
                            mostrar_personagem2(screen, x, 317)
