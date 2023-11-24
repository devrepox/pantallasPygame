from interfaces.intPantallas import Pantallas
from pantallas import pantalla1,secundaria
import pygame

class Main:
    def __init__(self):
        self.status="login"
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.clock = pygame.time.Clock()
        self.running=True
        self.pantalla:Pantallas=pantalla1.menu(self)
        self.run()

    def cambio(self,newPantalla):
        temp=self.pantalla
        if newPantalla=="Register":
            self.pantalla=secundaria.register(self)
        elif newPantalla=="main":
            self.pantalla=pantalla1.menu(self)
        del temp

    def run(self):
        while self.running:
            self.pantalla.runner()
            self.clock.tick(60)
        pygame.quit()

Main()