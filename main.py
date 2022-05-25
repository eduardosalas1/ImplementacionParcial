from ast import While
from juego import*


def main():

    juego = Juego()
    jugador1 = CincoNumerosPares()
    jugador2 = CincoNumerosImpares()
    jugador3 = NumeroPrimo()
    jugador4 = TresNumerosMultDiez()
    jugador5 = DosNumerosMult25()

    juego.attach(jugador1)
    juego.attach(jugador2)
    juego.attach(jugador3)
    juego.attach(jugador4)
    juego.attach(jugador5)

    if juego.ready == True:

        while(juego.verify() == False):

            juego.notify()

        
    juego.detach(jugador2)



main()
