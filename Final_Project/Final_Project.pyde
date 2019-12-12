add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)
difficulty = 1
character = "harold"
music = True
sound_fx = True
SCREEN_W = 1150
SCREEN_H = 800

class Platform:
    def __init__(self, x, y, w, h, img, floor):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.floor = floor
        self.img = loadImage(path + "/assets/images/platforms/" + img)
        if floor >= 400:
            self.tile_img = loadImage(path + "/assets/images/tiles/4.png")
        else:
            self.tile_img = loadImage(path + "/assets/images/tiles/" + str(self.floor//100 + 1) + ".png")
            # tiles for displaying floor number
        
    def showPlatform(self):
        image(self.img, self.x, self.y + game.y_shift, self.w, self.h)
        if self.floor % 10 == 0 and self.floor != 0:
            image(self.tile_img, self.x + self.w/2 - 35, self.y + 20 + game.y_shift, 70, 50)
            fill(255)
            textSize(20)
            text(self.floor, self.x + self.w/2 - 15, self.y + 50 + game.y_shift)
            #tile displayed every 10 platforms


class Button:
    def __init__(self, x, y, w, h, img = "transparent"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "/assets/images/buttons/" + img + ".png")
        self.on = False
        # some buttons are highlighted to indicate the current setting (options screen)
        
        
    def showButton(self):
        image(self.img, self.x, self.y, self.w, self.h)
        if self.on:
            noFill()
            stroke(0, 255, 0)
            strokeWeight(4)
            rect(self.x - 4, self.y - 4, self.w + 8, self.h + 8)
            # highlighting buttons that indicate the current setting
        elif mouseX in range(self.x, self.x + self.w) and mouseY in range(self.y, self.y + self.h):
            noFill()
            stroke(255)
            strokeWeight(4)
            rect(self.x - 4, self.y - 4, self.w + 8, self.h + 8)
            # rectangle around button to indicate that the mouse is over it
        

class Screen:
    def __init__(self, bg, buttons):
        self.bg = loadImage(path + "/assets/images/backgrounds/" + bg)
        self.buttons = buttons
        self.press_sound = player.loadFile(path + "/assets/audio/press.wav")
        # sound played when button is pressed
        
    def runScreen(self):
        # displaying buttons and screen background
        image(self.bg, 0, 0, game.w + 150, game.h)
        if game.screen == game_screen and not game.dead:
            for button in self.buttons:
                if button != play_again and button != main:
                    button.showButton()
        else:
            for button in self.buttons:
                button.showButton()
            
    def clickButton(self, button):
        # this function carries out the action that the button is supposed to do
        global game, difficulty, character, music, sound_fx, background_sound
        if button == instructions:
            game.screen = instructions_screen
        elif button == play:
            game.screen = game_screen
        elif button == back:
            game.screen = home_screen
        elif button == main:
            game = Game(1000, 800)
        elif button == play_again:
            restart()
        elif button == options:
            game.screen = options_screen
        elif button == on1:
            on1.on = True 
            off1.on = False
            game.music = True
            music = True
            if not background_sound.isPlaying():
                background_sound.rewind()
                background_sound.play()
            # playing music
        elif button == off1:
            on1.on = False 
            off1.on = True
            game.music = False
            music = False
            if background_sound.isPlaying():
                background_sound.pause()
            # stopping music
        elif button == on2:
            on2.on = True 
            off2.on = False
            sound_fx = True
            game.sound_fx = True
            # playing sound effects
        elif button == off2:
            on2.on = False 
            off2.on = True
            sound_fx = False
            game.sound_fx = False
            # stopping sound effects
        elif button == character1:
            character1.on = True
            character2.on = False
            character = "harold"
            game = Game(1000, 800)
            game.screen = options_screen
            # changing character
        elif button == character2:
            character2.on = True
            character1.on = False
            character = "Disco Dave"
            game = Game(1000, 800)
            game.screen = options_screen
            # changing character
        elif button == rookie:
            rookie.on = True
            amateur.on = False
            pro.on = False
            legend.on = False
            difficulty = 1
            game = Game(1000, 800)
            game.screen = options_screen
        elif button == amateur:
            rookie.on = False
            amateur.on = True
            pro.on = False
            legend.on = False
            difficulty = 1.25
            game = Game(1000, 800)
            game.screen = options_screen
        elif button == pro:
            rookie.on = False
            amateur.on = False
            pro.on = True
            legend.on = False
            difficulty = 1.5
            game = Game(1000, 800)
            game.screen = options_screen
        elif button == legend:
            rookie.on = False
            amateur.on = False
            pro.on = False
            legend.on = True
            difficulty = 2
            game = Game(1000, 800)
            game.screen = options_screen
            # changing difficulty
        elif button == leader:
            game.screen = leaderboard_screen
            
        if game.sound_fx:
            self.press_sound.rewind()
            self.press_sound.play()
            # playing the press sound if sound effects are turned on 
        
        
# class Confetti:
#     def __init__(self, x, y, vy, img, vx = 0):
#         self.x = x
#         self.y = y
#         self.vx = vx
#         self.vy = vy
#         self.img = loadImage(path + "/assets/images/confetti/" + img + ".png")
#         self.alive = True
    
#     def update(self):
#         self.vy += 0.4
#         if self.y + game.y_shift >= game.h :
#             self.alive = False
#         self.x += self.vx
#         self.y += self.vy
    
#     def showConfetti(self):
#         image(self.img, self.x, self.y + game.y_shift, 15, 15)
#         self.update()

# I would have added confetti to the game, but it slows it down significantly. Uncmomment this and lines 387 - 390 and lines 515-519
class PowerUp:
    def __init__(self, x, y, img, slices, img_w, img_h):
        self.x = x
        self.y = y
        self.img = loadImage(path + "/assets/sprites/powerups/" + img + ".png")
        self.type = img
        self.slices = slices
        self.frame = 1
        self.img_w = img_w
        self.img_h = img_h
        self.on = True
        
    def showPowerUp(self):
        # displaying powerup
        self.hitHero()
        if self.type == "spring":
            image(self.img, self.x, self.y + game.y_shift - self.img_h, self.img_w*2, self.img_h*2, self.frame * self.img_w, self.img_h, (self.frame +1) * self.img_w, 0)
            # spring image is flipped to create the illusion that it is going up and down with its base sticking to the platform 
        else:
            image(self.img, self.x, self.y + game.y_shift - self.img_h, self.img_w, self.img_h, self.frame * self.img_w, 0, (self.frame +1) * self.img_w,  self.img_h)
        if frameCount%5 == 0:
            self.frame = (self.frame + 1) % self.slices
    
    def hitHero(self):
        global game
        # checking if harold hits the powerup and boosting him accordingly
        if (game.harold.y + game.harold.r) in range(self.y - self.img_h*2, self.y) and game.harold.x in range(self.x, self.x + self.img_w*2):
            if self.type == "spring":
                game.harold.vy = - 300
                # big jump when player jumps on spring
            elif self.type == "multiplier":
                game.score_multiplier *= 2
                # score doubles when player takes powerup
            self.on = False
            # remove powerup if player uses it


class Hero:
    def __init__(self, x, y, r, g, img_w, img_h, slices, name):
        self.alive = True
        self.status = ""
        self.i_slices = slices[0]
        self.w_slices = slices[1]
        self.s_slices = slices[2]
        # slices for each movement type 
        self.idle = loadImage(path + "/assets/sprites/" + name + "/idle-" + name + ".png")
        self.walking = loadImage(path + "/assets/sprites/" + name + "/walking-" + name + ".png")
        self.jumping = loadImage(path + "/assets/sprites/" + name + "/jumping-" + name + ".png")
        self.jumping2 = loadImage(path + "/assets/sprites/" + name + "/jumping2-" + name + ".png")
        self.falling = loadImage(path + "/assets/sprites/" + name + "/falling-" + name + ".png")
        self.spinning = loadImage(path + "/assets/sprites/" + name + "/spinning-" + name + ".png")
        # loading images for the hero 
        self.frame_i = 0
        self.frame_w = 0
        self.frame_s = 0
        self.direction = ""
        self.img_w = img_w
        self.img_h = img_h
        self.x = x
        self.y = y
        self.r = r
        self.vy = 0
        self.vx = 0
        self.g = g
        self.key_handler = {LEFT: False, RIGHT:False, UP:False}
        self.jump_boost = 1
        self.jump_sound = player.loadFile(path + "/assets/audio/jump.wav")
        self.jump2_sound = player.loadFile(path + "/assets/audio/jump2.wav")
        self.spin_sound = player.loadFile(path + "/assets/audio/spin.wav")
        self.die_sound = player.loadFile(path + "/assets/audio/die.wav")
        # sound effects
        
    def gravity(self):
        if self.y + self.r == self.g:
            self.vy = 0
        else:
            self.vy += 6
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y + self.r)
        # adds to the vertical velocity if player is above the ground
        if self.hitPlatform() == game.platforms[0]:
            self.g = game.g
        else:
            self.g = self.hitPlatform().y
        # checks which platform the player is standing on and makes it the ground
            
    def hitPlatform(self):
        for i in range(1, len(game.platforms)):
            if self.y + self.r <= game.platforms[-i].y and self.x >= game.platforms[-i].x and self.x - self.r/2 <= game.platforms[-i].x + game.platforms[-i].w:
                return game.platforms[-i]
        return game.platforms[0]
        # function that returns the platform the player is currently on

    def update(self):
        self.gravity()
        if self.key_handler[LEFT]:
            if self.direction == RIGHT:
                self.vx = -self.vx 
            if self.vx > -40:
                self.vx -= 2
            self.direction = LEFT
        elif self.key_handler[RIGHT]:
            if self.direction == LEFT:
                self.vx = - self.vx
            if self.vx < 40:
                self.vx += 2
            self.direction = RIGHT
        else:
            self.vx = 0
        # moves to the left or right depending on the key pressed with max horizontal speed 40 pixels/frame

            
        self.jump_boost = abs(self.vx)//20
        # gives the player a boost depending on his horizontal velocity
        if self.jump_boost == 0:
            self.jump_boost = 1
        if self.key_handler[UP] and self.distance() == 0 and self.vy >=0:
            if game.sound_fx:
                if self.status != "boost":
                    if -0.5 < self.vx < 0.5:
                        self.jump_sound.rewind()
                        self.jump_sound.play()
                        # sound effects
                    else:
                        self.jump2_sound.rewind()
                        self.jump2_sound.play()
                        # sound effects
                else:
                    self.spin_sound.rewind()
                    self.spin_sound.play()
                    # sound effects
            self.vy = -45 * self.jump_boost
            # jump speed
        if self.x - self.r < 75:
            self.x = self.r + 75
        elif self.x >= game.w + self.r:
            self.x = game.w + self.r
        # stops player from going through wall

        self.y += self.vy
        self.x += self.vx
        if self.y <= 0:
            if game.y_shift +self.y <= 100:
                game.y_shift -= self.vy - 2*game.difficulty
            else:
                if self.vy > 0:
                    game.y_shift += 2*game.difficulty
                else:
                    game.y_shift -= self.vy//3 - 2*game.difficulty
            # moves the screen downwards to give illusion of floors falling. speed of falling depends on the difficulty
        if frameCount % 5 == 0:
            if -0.5 < self.vx < 0.5:
                self.frame_i = (self.frame_i + 1) % self.i_slices
            elif -0.5 > self.vx or self.vx > 0.5:
                self.frame_w = (self.frame_w + 1) % self.w_slices
            # animations for walking and standing
        if self.vy < - 65 and game.floor[0] > 5:
            if not self.spin_sound.isPlaying() and game.sound_fx:
                self.spin_sound.rewind()
                self.spin_sound.play()
                # sound effects
            self.status = "boost"
        elif self.vy > 20 or self.vy == 0:
            self.status = ""
            if self.spin_sound.isPlaying():
                self.spin_sound.pause()
        self.frame_s = (self.frame_s + 1) % self.s_slices
        # animation for spinning

        if self.y + game.y_shift >= game.h:
            if game.sound_fx and not self.die_sound.isPlaying():
                self.die_sound.rewind()
                self.die_sound.play()
                # sound effects
            self.alive = False
            # player dies iff he falls off screen
            
    def distance(self):
         return (self.y + self.r - self.g)   
        
    def show(self):
        global game
        self.update()
        if self.status == "boost":
            game.floor[1] += 0.4
            # game.confetti.append(Confetti(self.x + random.randint(-5, 5), self.y, 10, random.choice(game.conf), random.randint(-10, 10)))
            # game.confetti.append(Confetti(self.x + random.randint(-5, 5), self.y, 10, random.choice(game.conf), random.randint(-10, 10)))
            # game.confetti.append(Confetti(self.x + random.randint(-5, 5), self.y, 10, random.choice(game.conf), random.randint(-10, 10)))
            # game.confetti.append(Confetti(self.x + random.randint(-5, 5), self.y, 10, random.choice(game.conf), random.randint(-10, 10)))
            image(self.spinning, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["spin"] * 1.5, self.img_h["spin"] * 1.5, self.frame_s * self.img_w["spin"], 0, (self.frame_s +1) * self.img_w["spin"], self.img_h["spin"])
        else:
            if -0.5 < self.vx < 0.5 and self.vy < 0:
                image(self.jumping, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["jump"] * 1.5, self.img_h["jump"] * 1.5)
            elif self.vx > 0.5 and self.vy < 0:
                image(self.jumping2, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["jump2"] * 1.5, self.img_h["jump2"] * 1.5)
            elif self.vx < -0.5 and self.vy < 0:
                image(self.jumping2, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["jump2"] * 1.5, self.img_h["jump2"] * 1.5, self.img_w["jump2"], 0, 0, self.img_h["jump2"])
            elif self.vx > 0.5 and self.vy > 0:
                image(self.falling, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["fall"] * 1.5, self.img_h["fall"] * 1.5)
            elif self.vy > 0:
                image(self.falling, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["fall"] * 1.5, self.img_h["fall"] * 1.5, self.img_w["fall"], 0, 0, self.img_h["fall"])
            elif -0.5 < self.vx < 0.5 and self.vy == 0:
                image(self.idle, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["idle"] * 1.5, self.img_h["idle"] * 1.5, self.frame_i * self.img_w["idle"], 0, (self.frame_i +1) * self.img_w["idle"], self.img_h["idle"])
            elif self.vx >= 0.5:
                image(self.walking, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["walking"] * 1.5, self.img_h["walking"] * 1.5, self.frame_w * self.img_w["walking"], 0, (self.frame_w +1) * self.img_w["walking"], self.img_h["walking"])
            elif self.vx <= -0.5:
                image(self.walking, self.x - self.r, self.y -self.r +  game.y_shift, self.img_w["walking"] * 1.5, self.img_h["walking"] * 1.5, (self.frame_w +1) * self.img_w["walking"], 0, self.frame_w * self.img_w["walking"], self.img_h["walking"])
            # displaying chaaracter
                         
class Game:
    def __init__(self, w, h):
        global character, difficulty, sound_fx, music
        self.sound_fx = sound_fx
        self.music = music
        self.difficulty = difficulty
        self.character = character
        self.confetti = []
        self.tile = loadImage(path + "/assets/images/tile.jpg")
        self.conf = ["pink", "blue", "yellow", "red"]
        self.w = w
        self.h = h
        self.high_score_img = loadImage(path + "/assets/images/highscore.png")
        self.score = 0
        self.floor = [0, 0]
        self.screen = home_screen
        self.g = self.h - 120
        self.y_shift = 0
        self.score_multiplier = 10
        self.platforms = []
        self.powerups = []
        self.name = ''
        self.red = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.dead = False
        self.go_img = loadImage(path + "/assets/images/backgrounds/game-over.png")
        for i in range(3):
            self.platforms.append(Platform(75 + (self.w * i)/3, self.g, self.w/3, 50, "platform1.png", 0))
        for i in range(2, 100):
            w = random.randint(300, 400)//self.difficulty
            x = random.randint(75, self.w - w)
            platform = Platform(x, self.h - 120*i, w, 50, "platform1.png", i)
            self.platforms.append(platform)
            self.temp = 120 * i 
        for i in range(3):
            self.platforms.append(Platform(75 + (self.w * i)/3, self.g - self.temp, self.w/3, 50, "platform2.png", 100))
        for i in range(101, 200):
            w = random.randint(250, 350)//self.difficulty
            x = random.randint(75, self.w - w)
            self.platforms.append(Platform(x, self.h - 120*i, w, 50, "platform2.png", i))
            self.temp = 120 * i 
        for i in range(3):
            self.platforms.append(Platform(75 + (self.w * i)/3, self.g - self.temp, self.w/3 - 20, 50, "platform3.png", 200))
        for i in range(201, 300):
            w = random.randint(150, 250)//self.difficulty
            x = random.randint(75, self.w - w)
            self.platforms.append(Platform(x, self.h - 120*i, w, 50, "platform3.png", i))
            self.temp = 120 * i 
        for i in range(3):
            self.platforms.append(Platform(75 + (self.w * i)/3, self.g - self.temp, self.w/3 - 20, 50, "platform4.png", 300))
        for i in range(301, 400):
            w = random.randint(150, 250)//self.difficulty
            x = random.randint(75, self.w - w)
            self.platforms.append(Platform(x, self.h - 120*i, w, 50, "platform4.png", i))
        # creating platforms with different widths and images
        random_platform1 = random.choice(self.platforms)
        random_platform2 = random.choice(self.platforms)
        
        self.powerups.append(PowerUp(int(random_platform1.x + random_platform1.w/2 - 108), random_platform1.y, "spring", 4, 108, 32))
        self.powerups.append(PowerUp(int(random_platform2.x + random_platform2.w/2 - 102), random_platform2.y, "multiplier", 4, 102, 115))
        # creating two powerups
        self.harold = Hero(self.w/2, self.h - 30, 40, self.g, {"idle":114/3, "walking":37, "spin":60, "jump":38, "jump2": 38, "fall":38}, {"idle":73, "walking":73, "spin":60, "jump":71, "jump2": 71, "fall":71}, [4, 4, 12], self.character)            
        # creating character
        self.level = 4
        
    def makePlatforms(self, level):
        # creating platforms whenever player gets near the roof
        for i in range(3):
            self.platforms.append(Platform(75 + (self.w * i)/3, self.g - self.temp, self.w/3 - 20, 50, "platform4.png", self.level * 100))
        for i in range(self.level * 100 + 1, (self.level + 1) * 100):
            w = random.randint(150, 250)//self.difficulty
            x = random.randint(75, self.w - w)
            self.platforms.append(Platform(x, self.h - 120*i, w, 50, "platform4.png", i))
            self.temp = 120 * i
        
    def display(self):
        global background_sound
        self.font = createFont("RoteFlora.ttf", 32)
        global leaderboard
        self.screen.runScreen()
        if self.screen == game_screen:
            background_sound.pause()
            # pausing music in game
            for i in range(10):
                if i in range(len(self.platforms)):
                    if self.platforms[i].y + self.y_shift  - 120 > self.h:
                        self.platforms.remove(self.platforms[i])
                        # removing platforms that go out of the screen
                    else:
                        self.platforms[i].showPlatform()
                        # showing platforms 10 at a time
                else:
                    self.makePlatforms(self.level)
                    self.level += 1
                    # if the player is less than 10 platforms away from the roof we create 1 more level and so on
            for powerup in self.powerups: 
                if powerup.on:
                    powerup.showPowerUp()
                else:
                    self.powerups.remove(powerup)    
                # showing powerups and removing used powerups
                
           
             # for conf in self.confetti:
            #     if not conf.alive:
            #         self.confetti.remove(conf)
            #     else:
            #         conf.showConfetti()
            if self.harold.alive:
                self.harold.show()
                platform = self.harold.hitPlatform()
                # gets current platform harold is on
                if self.floor[0] < platform.floor:
                    self.floor[0] = platform.floor
                    # floor[0] is the highest floor reached x 10, while floor[1] is score accumulated on a jump boost
                    self.red = random.randint(0, 255)
                    self.blue = random.randint(0, 255)
                    self.green = random.randint(0, 255)
                    # new colors every floor, looks pretty
                self.score = int((self.floor[0] + self.floor[1]) * self.score_multiplier * self.difficulty)
                # so the total score is the score accumulated on a jump boost + score from floors times the multiplier (if any) and the difficulty
                fill(self.red, self.green, self.blue)
                textFont(self.font, 60)
                text(str(self.score), 25, self.h - 100)
                self.temp = self.y_shift
                # this temp stores the current y shift so when the player diesthe screen stops shifting
            if not self.harold.alive:
                if self.score > leaderboard[-1][1] and not self.dead:
                    # checks if player score is higher than the least score on the leaderboard (faster than a for loop)
                    # and displayes the high score image and asks user for their name and displays it as he's writing
                    image(self.high_score_img, SCREEN_W/2 - 462/2, SCREEN_H / 2 - 100, 462, 86)
                    self.y_shift = self.temp
                    fill(255)
                    textFont(self.font, 70)
                    textAlign(CENTER)
                    text("Name", SCREEN_W/2, SCREEN_H/2 + 50)
                    textAlign(CENTER, BOTTOM)
                    text(self.name, SCREEN_W/2, SCREEN_H/2 + 150)
                else:
                    image(self.go_img, 375, 300, 400, 340)
                    fill(0)
                    textFont(self.font, 40)
                    textAlign(RIGHT)
                    text(self.score, 760, 420)
                    textAlign(RIGHT)
                    text(self.floor[0], 760, 480)
                    for button in self.screen.buttons:
                        button.showButton()  
                    # showing game over image
                    
        if self.screen == leaderboard_screen:
            fill(0)
            textFont(self.font, 80)
            textAlign(LEFT)
            text("NAME", self.w/2 - 300, 300)
            i = 0
            for row in leaderboard:
                i += 1
                textAlign(LEFT)
                text(row[0], self.w/2 - 300, 300 + 100*i)
            textAlign(LEFT)
            text("Score", self.w/2 + 200, 300)
            i = 0
            for row in leaderboard:
                i += 1
                textAlign(LEFT)
                text(row[1], self.w/2 + 200, 300 + 100*i)
            # showing leaderboard
        if self.music and not background_sound.isPlaying() and self.screen != game_screen:
            background_sound.rewind()
            background_sound.play()
        elif not self.music:
            background_sound.pause()
           
       
def restart():
    global game
    game = Game(1000, 800)
    game.screen = game_screen
    # restarting game

def getLeaderboard():
    leaderboard = []
    leaderboard_file = open("leaderboard.csv", "r")
    for line in leaderboard_file:
        row = line.strip().split(",")
        row[1] = int(row[1])
        leaderboard.append(row)
    leaderboard_file.close()
    leaderboard.sort(key=lambda x: x[1], reverse = True)
    return leaderboard
    # getting leaderboard from csv file and sorting them depending on scores

def updateLeaderboard():
    global leaderboard, game
    if game.score > leaderboard[2][1]:
        leaderboard[2] = [game.name, game.score]
        leaderboard.sort(key=lambda x: x[1], reverse = True)
    leaderboard_file = open("leaderboard.csv", "w")
    for row in leaderboard:
        leaderboard_file.write(row[0] + "," + str(row[1]) + "\n")
    leaderboard_file.close()
    # writing the new leaderboard to the same csv file

background_sound = player.loadFile(path + "/assets/audio/theme-song.mp3")
pause = Button(50, 50, 50, 50, "pause")
play = Button(700, 400, 271, 76, "play" )
instructions = Button(700, 500, 271, 76, "instructions")
sound = Button(50, 150, 50, 50, "sound")
play_again = Button(400, 550, 134, 34, "play-again")
main = Button(400, 600, 134, 34, "main-menu")
leader = Button(700, 600, 271, 76, "leader")
options = Button(700, 700, 192, 58, "options")
on1 = Button(750, 105, 90, 60)
on1.on = True
on2 = Button(750, 245, 90, 60)
on2.on = True
off1 = Button(895, 100, 105, 60)
off2 = Button(895, 245, 105, 60)
rookie = Button(240, 495, 165, 55)
rookie.on = True
amateur = Button(410, 495, 220, 55)
pro = Button(645, 495, 90, 50)
legend = Button(745, 495, 160, 50)
character1 = Button(795, 560, 60, 100)
character1.on = True
character2 = Button(900, 560, 60, 100)
back = Button(200, 700, 195, 60, "back")
options_screen = Screen("options.jpg", [on1, on2, off1, off2, rookie, amateur, pro, legend, character1, character2, back])
home_screen = Screen("bg1.jpg", [play, instructions, leader, options])
instructions_screen = Screen("instructions.jpg", [back])
game_screen = Screen("bg2.jpg", [play_again, main])
leaderboard_screen = Screen("high-scores.jpg", [back]) 
# buttons and screens   
leaderboard = getLeaderboard()
game = Game(1000, 800)

def keyPressed():
    global game
    if not game.harold.alive and game.screen == game_screen:
        if key == DELETE or key == BACKSPACE:
            game.name = game.name[:-1]
        elif key == RETURN or key == ENTER:
            updateLeaderboard()
            game.dead = True
        elif key == SHIFT:
            pass
        else:
            game.name += str(key)
        # player writes name
    else:
        if keyCode == LEFT:
            game.harold.key_handler[LEFT] = True
        elif keyCode == RIGHT:
            game.harold.key_handler[RIGHT] = True
        # elif keyCode == UP:
        elif key == " " or keyCode == UP:
            game.harold.key_handler[UP] = True 
      # changes direction based on key pressed  
        
        
def keyReleased():
    if keyCode == LEFT:
        game.harold.key_handler[LEFT] = False
    elif keyCode == RIGHT:
        game.harold.key_handler[RIGHT] = False
    elif key == " " or keyCode == UP:
        game.harold.key_handler[UP] = False   
    # turns direction off when the key is released    
    
def setup():
    size(SCREEN_W, SCREEN_H)
    background(0)
    
def draw():
    background(0)
    game.display()
    
def mouseClicked():
    for button in game.screen.buttons:
        if mouseX in range(button.x, button.x + button.w) and mouseY in range(button.y, button.y + button.h):
            game.screen.clickButton(button)
            break
    # when mouse is clicked, this function looks through each button in the screen, and iff the mouseX and mouseY are inside the borders of the button it calls the clickButton function
