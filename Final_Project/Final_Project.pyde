add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)


class Platform:
    def __init__(self, x, y, w, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = 100
        self.img = loadImage(path + "/" + img + ".png")
        self.status = 1
        self.fallcounter = 0
        self.shaker = [-10, 0, 0, 10, 10, 0, 0, -10]*2
        
    def show_platform(self):
        if self.status == 1:
            image(self.img, self.x, self.y, self.w, self.h)
        elifs self.status == 2:
            y = self.shaker.pop()
            x = self.shaker.pop()
            image(self.img, self.x + x, self.y + y, self.w, self.h)
            if len(self.shaker) == 0:
                self.fall()
                self.status = 3
                
    def fall(self):
        self.y += 10
        self.fallcounter += 1
        if self.fallcounter = 12:
            self.status = 4


class Buttons:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "/" + img + ".png")
    
    def showButton(self):
        image(self.img, self.x, self.y, self.w, self.h)
        if mouseX in range(self.x, self.w) and mouseY in range(self.y, self.h):
            noFill()
            stroke(255)
            strokeWeight(10)
            rect(self.x - 10, self.y - 10, self.w + 20, self.h + 20)

class Screen:
    def __init__(self, bg, buttons, sound):
        self.bg = loadImage(path + "/" + bg + ".png")
        self.buttons = buttons
        self.sound = player.loadFile(path + "/sounds/" + sound + ".mp3")
        self.sound_on = True
    
    def runScreen(self):
        image(self.bg, 0, 0, game.w, game.h)
        for button in self.buttons:
            button.showButton()
        # something for the sounds
            
    def clickButton(button):
        global game
        if button = home:
            game.screen = home_screen
        elif button = instructions:
            game.screen = instructions_screen
        elif button = play:
            game.screen = game_screen
        elif button = pause:
            game.screen = pause_screen
        elif button = restart:
            restart()
        elif button = ok:
            game.screen = game_screen
        elif button = sound:
            if self.sound_on:
                self.sound_on = False
            else:
                self.sound_on = True
    
class Hero:
    def __init__(self):
        
    def show(self):

    def move(self):
                      
class Game:
    def __init__(self):
    
    def display(self):
            
def restart():
    global game
    game = Game()
    game.screen = play

pause = Button(, , , , )
play = Button(, , , , )
home = Button(, , , , )
instructions = Button(, , , , )
sound = Button(, , , , )
restart = Button(, , , , )
ok = Button(, , , , )


home_screen = Screen("bg1", [play, instructions, sound], "bgmusic1")
instructions_screen = Screen("bg2", [home], "bgmusic1")
game_screen = Screen("bg3", [pause], "bgmusic2")
pause_screen = Screen("bg4", [home, instructions, restart, sound, ok], "bgmusic2")
                     


                   
    
def keyPressed():

def keyReleased():
    
def mouseClicked():
    for button in game.screen.buttons:
        if mouseX in range(button.x, button.w) and mouseY in range(button.y, button.h):
            game.screen.clickButton(button)
            break
        
def setup():
    fullScreen()
    background(255)
    
def draw():