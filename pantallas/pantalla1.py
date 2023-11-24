import pygame
from interfaces.intPantallas import Pantallas
from componentes import button

class menu(Pantallas):
    def __init__(self,manager):
        self.controlador=manager
        self.pantalla=manager.screen
        
    def runner(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.controlador.running = False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_2:
                         print("tecla 2")
                         self.change("Register")
                     
        self.pantalla.fill("purple")
        pygame.display.flip()
    
    def change(self,newPantalla):
         self.controlador.cambio(newPantalla)