import pygame

class Textureclass:

    def __init__(self, theme):
        path = "images/" + theme + "/"

        self.closed = pygame.image.load(path + "blank.gif")
        self.closed.convert()
        self.open0 = pygame.image.load(path + "open0.gif")
        self.open0.convert()
        self.open1 = pygame.image.load(path + "open1.gif")
        self.open1.convert()
        self.open2 = pygame.image.load(path + "open2.gif")
        self.open2.convert()
        self.open3 = pygame.image.load(path + "open3.gif")
        self.open3.convert()
        self.open4 = pygame.image.load(path + "open4.gif")
        self.open4.convert()
        self.open5 = pygame.image.load(path + "open5.gif")
        self.open5.convert()
        self.open6 = pygame.image.load(path + "open6.gif")
        self.open6.convert()
        self.open7 = pygame.image.load(path + "open7.gif")
        self.open7.convert()
        self.open8 = pygame.image.load(path + "open8.gif")
        self.open8.convert()
        self.bomb = pygame.image.load(path + "bombrevealed.gif")
        self.bomb.convert()
        self.bombdeath = pygame.image.load(path + "bombdeath.gif")
        self.bombdeath.convert()
        self.flaga = pygame.image.load(path + "bombflagged.gif")
        self.flaga.convert()
        self.bombmisflagged = pygame.image.load(path + "bombmisflagged.gif")
        self.bombmisflagged.convert()

        self.won = pygame.image.load(path + "facewin.gif")
        self.won.convert()
        self.lost = pygame.image.load(path + "facedead.gif")
        self.lost.convert()
        self.smile = pygame.image.load(path + "facesmile.gif")
        self.smile.convert()

        self.borderl = pygame.image.load(path + "borderl.gif")
        self.borderl.convert()
        self.borderbl = pygame.image.load(path + "borderbl.gif")
        self.borderbl.convert()
        self.bordertb = pygame.image.load(path + "bordertb.gif")
        self.bordertb.convert()
        self.borderbr = pygame.image.load(path + "borderbr.gif")
        self.borderbr.convert()
        self.bordertl = pygame.image.load(path + "bordertl.gif")
        self.bordertl.convert()
        self.bordertr = pygame.image.load(path + "bordertr.gif")
        self.bordertr.convert()
        self.borderlr = pygame.image.load(path + "borderlr.gif")
        self.borderlr.convert()
        self.borderjl = pygame.image.load(path + "borderjl.gif")
        self.borderjl.convert()
        self.borderjr = pygame.image.load(path + "borderjr.gif")
        self.borderjr.convert()

        self.button = pygame.image.load(path + "button.gif")
        self.button.convert()

        self.time0 = pygame.image.load(path + "time0.gif")
        self.time0.convert()
        self.time1 = pygame.image.load(path + "time1.gif")
        self.time1.convert()
        self.time2 = pygame.image.load(path + "time2.gif")
        self.time2.convert()
        self.time3 = pygame.image.load(path + "time3.gif")
        self.time3.convert()
        self.time4 = pygame.image.load(path + "time4.gif")
        self.time4.convert()
        self.time5 = pygame.image.load(path + "time5.gif")
        self.time5.convert()
        self.time6 = pygame.image.load(path + "time6.gif")
        self.time6.convert()
        self.time7 = pygame.image.load(path + "time7.gif")
        self.time7.convert()
        self.time8 = pygame.image.load(path + "time8.gif")
        self.time8.convert()
        self.time9 = pygame.image.load(path + "time9.gif")
        self.time9.convert()