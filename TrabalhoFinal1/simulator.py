# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.gridspec as gridspec
import pygame
import datetime
import math
# import random


from s_classes import *

def main():

    # Definição das especificações do plot
    # configuração do plot do output
    # x = 0
    # y = 0
    # plt.ion()

    # fig, ax = plt.subplots(figsize=(10, 8))
    # line, = ax.plot(x, y)
    # ax.set_title('Resposta da Posição Horizontal')
    # ax.set_ylabel('Posição')
    # ax.set_xlabel('Tempo [frame]')
    
    # Inicia o pygame
    pygame.init()
    xl = 1200
    yl = 800
    # Define o tamanho da tela
    screen = pygame.display.set_mode((xl, yl))

    # Define quantidades de loops e frames por segundo
    lps = 100.0
    fps = 60.0

    # Define variáveis para periodo de calculo e periodo de frame
    calc_period = datetime.timedelta(seconds=1.0 / lps)
    next_calc = datetime.datetime.now()
    draw_period = datetime.timedelta(seconds=1.0 / fps)
    next_draw = datetime.datetime.now()

    gravity = 9.81

    # Cria objetos para controlador, ambiente de simulação e drone
    controller = AutoController()
    world = Ground()
    Drone = drone([600, world.depth], world, controller, base_error=0.001)

    # define fonte como default para plot de dados na tela
    font = pygame.font.Font(None, 30)

    count = 0
    running = True
    # inicia o loop
    while running:
        # Lida com eventos de quit e clique do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # para o click do mouse pega a posição de x e y define como posição desejada
                controller.desired_height = world.depth - event.pos[1]
                controller.desired_x = event.pos[0] - (screen.get_size()[0] / 2)

        now = datetime.datetime.now()

        # Refaz o calculo para a posição
        if now >= next_calc:
            next_calc += calc_period

            Drone.vel[1] += 9.91 / lps
            Drone.update()
            # print(Drone.vel)
            # print(Drone.pos)
            # print(Drone.rot*180/math.pi)
            # print(Drone.controller.height_pid.output)
            # print(Drone.r_thrust)
 
        # Replota tudo na tela
        if now >= next_draw:
            next_draw += draw_period

            text1 = f'''Velocidade: {Drone.vel[0]:.3f}, {-Drone.vel[1]:.3f} [m/s]'''
            output1 = font.render(text1, True, (255, 255, 255))
            text2 = f'''Posição: {Drone.pos[0]:.3f}, {(yl - Drone.pos[1]):.3f} [m]'''
            output2 = font.render(text2, True, (255, 255, 255))
            text4 = f'''Angulação: {Drone.rot*180/math.pi*(-1):.3f} [graus]'''
            output4 = font.render(text4, True, (255, 255, 255))

            screen.fill((0,0,0))
            world.draw(screen)
            Drone.draw(screen)
            screen.blit(output1,(10 , 10))
            screen.blit(output2,(10 , 35))
            screen.blit(output4,(10 , 60))

            # new_y = Drone.pos[0]
            # line.set_xdata(count)
            # line.set_ydata(new_y)
            # fig.canvas.draw()
            # fig.canvas.flush_events()
            # count += 1

            pygame.display.flip()
            
    pygame.quit()


if __name__ == "__main__":
    main()