import datetime
import pygame
import random
import math

# Classe para o controlador
class Controller(object):
    def update(self, drone):
        pass

# Classe para o sensor
class Sensor(object):
    def __init__(self, value, error=0):
        self.value = value
        self.error = error

    def set(self, value):
        self.value = value + random.gauss(0, self.error)

    def update(self, latest_measurement):
        pass

    def get(self):
        return self.value

# Classe que calcula a diferença de leitura dos sensores
class dSensor(Sensor): 
    def __init__(self, value, error=0):
        Sensor.__init__(self, value, error)
        self.last = value

    def update(self, latest_measurement):
        self.set(latest_measurement - self.last)
        self.last = latest_measurement

# Classe que define os sensores do drone para leitura da velocidade e rotação
class Sensors(object):
    def __init__(self, drone, base_error=0):
        self.drone = drone
        self.x_vel = dSensor(drone.pos[0], base_error)
        self.y_vel = dSensor(drone.pos[1], base_error)
        self.rot = dSensor(drone.rot, base_error)

    def update(self):
        self.x_vel.update(self.drone.pos[0])
        self.y_vel.update(self.drone.pos[1])
        self.rot.update(self.drone.rot)

# Classe que define o objeto drone
class drone(object):
    def __init__(self, pos, world, controller, sensor_interface=Sensors, base_error=0):
        self.controller = controller
        self.world = world
        self.pos = pos
        self.rot = -math.pi / 2
        self.l_thrust = 0
        self.r_thrust = 0
        self.vel = [0, 0]
        self.max_thrust = 100
        self.min_thrust = 0
        self.mass = 1E3
        self.arm_length = 25
        self.sensors = sensor_interface(self, base_error)

    def set_thrust(self, left, right):
        self.l_thrust = max(min(left, self.max_thrust), self.min_thrust)
        self.r_thrust = max(min(right, self.max_thrust), self.min_thrust)

    def total_thrust(self):
        return [math.cos(self.rot) * (self.l_thrust + self.r_thrust),
                math.sin(self.rot) * (self.l_thrust + self.r_thrust)]

    def update(self):
        self.accelerate(self.total_thrust())
        nx, ny = self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]
        if not self.world.check((nx, ny)):
            self.pos[0] = nx
            self.pos[1] = ny
        else:
            self.vel[0] *= 0.8
            self.vel[1] *= -0.5

        net_rot_thrust = (self.l_thrust - self.r_thrust) * 0.001
        ground_rot_thrust = 0.01
        if self.world.check(self.r_thruster()):
            net_rot_thrust -= ground_rot_thrust
        if self.world.check(self.l_thruster()):
            net_rot_thrust += ground_rot_thrust
        self.rot += net_rot_thrust

        self.sensors.update()
        self.controller.update(self)

    # Força no braço direito
    def r_thruster(self):
        cx, cy = self.pos
        cx += math.cos(self.rot + (math.pi / 2)) * self.arm_length
        cy += math.sin(self.rot + (math.pi / 2)) * self.arm_length
        return (cx, cy)

    # Força no braço esquerdo
    def l_thruster(self):
        cx, cy = self.pos
        cx += math.cos(self.rot - (math.pi / 2)) * self.arm_length
        cy += math.sin(self.rot - (math.pi / 2)) * self.arm_length
        return (cx, cy)

    # Altera as velocidades mediante as forças
    def accelerate(self, force):
        self.vel[0] += force[0] / self.mass
        self.vel[1] += force[1] / self.mass

    # Desenha o Drone 
    def draw(self, dest):
        x = int(self.pos[0])
        y = int(self.pos[1])
        lx, ly = self.l_thruster()
        rx, ry = self.r_thruster()
        lx, ly = int(lx), int(ly)
        rx, ry = int(rx), int(ry)
        pygame.draw.line(dest, (255, 255, 255), (lx, ly), (rx, ry))
        pygame.draw.circle(dest, (255, 255, 255), (x, y), 4)

        self.controller.draw(dest)

# Classe para definir o chão
class Ground(object):
    def __init__(self):
        self.depth = 790

    def check(self, pos):
        return pos[1] >= self.depth

    def get_height(self, pos):
        return max(self.depth - pos[1], -1)

    def draw(self, dest):
        pygame.draw.line(dest, (255,255,255), (0, self.depth), (dest.get_size()[0], self.depth), 2)

# Classe para o PID
class PID(object):
    def __init__(self, p, i, d):
        self.params = (p, i, d)
        self.last = 0
        self.integral = 0
        self.output = 0

    # Faz o update com os coeficientes 
    def update(self, error):
        p, i, d = self.params
        self.integral += error
        delta = error - self.last
        self.last = error
        self.output = error * p + self.integral * i + delta * d
        return self.output

    # Calcula o erro de rastreamento
    def update_auto(self, actual, desired=0):
        error = desired - actual
        return self.update(error)

# Classe que define a ação de controle do PID
class AutoController(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.desired_height = 100
        self.desired_x = -100

        self.estimated_x = 0
        self.height_estimate = 0
        self.rotation_estimate = -math.pi / 2

        self.drone = None

        self.height_pid = PID(0.05, 0, 3.5)
        self.x_pid = PID(0.05, 0, 2)

        self.yvel_pid = PID(10000, 0, 0)
        self.xvel_pid = PID(0.2, 0, 0)
        self.rot_pid = PID(50, 0, 0)

    def update(self, drone):
        self.drone = drone

        target_delta = 1
        # Mapeamento das teclas para controle manual do drone
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.desired_x -= target_delta
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.desired_x += target_delta
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.desired_height += target_delta
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.desired_height -= target_delta

        # Coleta informações dos sensores
        sensors = drone.sensors
        self.height_estimate -= sensors.y_vel.get() # velocidade Vertical
        self.rotation_estimate += sensors.rot.get() # rotacao
        self.estimated_x += sensors.x_vel.get() # Velocidade horizontal

        # Calcula o erro para x
        x_error = self.estimated_x - self.desired_x
        desired_xvel = -self.x_pid.update(x_error)
        
        # Calcula o erro para y
        height_error = self.height_estimate - self.desired_height
        desired_yvel = self.height_pid.update(height_error)

        # Calcula o erro para velocidade em x
        yvel_error = sensors.y_vel.get() - desired_yvel
        base_thrust = self.yvel_pid.update(yvel_error)

        # Define minimos e maximos para forças
        thrust_min = drone.max_thrust * 0.1
        thrust_max = drone.max_thrust * 0.8
        base_thrust = min(max(base_thrust, thrust_min), thrust_max)

        # Erro da velocidade x 
        xvel_error = sensors.x_vel.get() - desired_xvel

        # Define minimos e maximos para rotacao
        desired_rot = (-math.pi / 2) - self.xvel_pid.update(xvel_error)
        rot_min = (-math.pi / 2) - (math.pi / 4)
        rot_max = (-math.pi / 2) + (math.pi / 4)
        desired_rot = min(max(desired_rot, rot_min), rot_max)
        rot_error = self.rotation_estimate - desired_rot
        left_thrust = -self.rot_pid.update(rot_error)
        right_thrust = -left_thrust

        l = base_thrust + left_thrust
        r = base_thrust + right_thrust
 
        drone.set_thrust(l, r)

    def draw(self, dest):
        x, y = int(self.drone.pos[0]), int(self.drone.pos[1])
        tx = int(dest.get_size()[0] / 2 + self.desired_x)
        ty = int(self.drone.world.depth - self.desired_height)
        r = 20
        colour = (0, 0, 0)

        pygame.draw.line(dest, colour, (tx-r, ty), (tx+r, ty))
        pygame.draw.line(dest, colour, (tx, ty-r), (tx, ty+r))
