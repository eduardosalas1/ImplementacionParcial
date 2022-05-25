import numbers
from tokenize import Number
from Observer import*
from random import seed
from random import randint

class Subject():

    def __init__(self):
        self.lista = []
        self.num = -1
        self.ready = False
        self.numbers = []
        self.winner = False

    def attach(self,obs):
        pass
    def detach(self,obs):
        pass

    def notify(self):
        pass


class Juego(Subject):

    def attach(self,obs):
        self.lista.append(obs)
        if len(self.lista) == 5:
            self.ready = True
            self.notify()
         

    def detach(self, obs):
        self.lista.remove(obs)

    def notify(self):

        seed(1)

        while True :

            self.num = randint(1,100)

            if self.num not in self.numbers:
                self.numbers.append(self.num)
                break
            else :
                continue
        print(self.num,',')
        for obs in self.lista:
            obs.update(self)

    def verify(self):
        if self.winner == True:
            for i in self.lista:
                i.verify()
            return True

        return False






