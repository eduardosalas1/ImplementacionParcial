

class Observer():

    def __init__(self):
        self.numbers = []
        self.win = False

    def update(self,subject):
        pass

    def verify(self):
        pass


class CincoNumerosPares(Observer):

    def update(self,juego):
        num = juego.num
        self.numbers.append(num)
        counter = 0

        for i in self.numbers:
            if (i % 2) == 0:
                counter += 1
        
        if counter >= 5:
            self.win = True
            juego.winner = True

    def verify(self):
        if self.win == True:
            print('Ganador con estrategia de Cinco Numeros Pares')



class CincoNumerosImpares(Observer):

    def update(self,juego):
        num = juego.num
        self.numbers.append(num)
        counter = 0

        for i in self.numbers:
            if (i % 2) != 0:
                counter += 1

        if counter >= 5:
            self.win = True
            juego.winner = True

    def verify(self):
        if self.win == True:
            print('Ganador con estrategia de Cinco Numeros Impares')

class NumeroPrimo(Observer):

    def esPrimo(num):
        if num < 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    def update(self,juego):
        self.win = self.esPrimo(juego.num)
        juego.winner = self.win
        
    def verify(self):
        if self.win == True:
            print('Ganador con estrategia de Numero Primo')


class TresNumerosMultDiez:

    def update(self,juego):
        num = juego.num
        self.numbers.append(num)
        counter = 0

        for i in self.numbers :
            if (i % 10) == 0:
                counter += 1

        if counter >= 3:
            self.win = True
            juego.winner = True

    def verify(self):
        if self.win == True:
            print('Ganador con estrategia de Tres Numeros multiplos de 10')


class DosNumerosMult25:

    def update(self,juego):
        num = juego.num
        self.numbers.append(num)
        counter = 0

        for i in self.numbers :
            if (i % 25) == 0:
                counter += 1

        if counter >= 2:
            self.win = True
            juego.winner = True

    def verify(self):
        if self.win == True:
            print('Ganador con estrategia de dos numeros multiplos de 25')