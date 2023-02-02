import random

print("Sbien venido a la mazmorra aqui empieza tu abentura\n"
      "resulta que haz caido aqui intentando huir\n"
      "to objetvo es salir de aqui con vida \n"
      "la aventura empieza\n")

print("----------------------\n")
print('¿en frente de ti ves tres formas de moverte cual escojes?')
opcion = int(input("1)sales por la puerta de enfrente de ti\n"
                   "2)sales por una bajada a la alcantarilla\n"
                   "3)sales por una escalera hacia el techo\n"))
if opcion == 1:
    opcion = int(input("te haz encontrado a un guardia y estas desarmado ¿que haras?\n"
                       "1)te enfrentas a el\n"
                       "2)corrers despaborido\n"))
    if opcion == 1:
        print("al parecer no eres nada fuerte \n"
              "el guardia te atraveso con su espada y moriste\n"
              "GAME OVER")
        exit()
    elif opcion == 2:
        print("haz salido corriendo, eres un cobarde\n"
              "pero el guardia te alcanzo\n"
              "te ha atarvesado con su espada\n"
              "GAME OVER ")
    else:
        print("genial, te equivocaste i te evaporaste instantaneamente\n"
              "GAME OVER")
        exit()

elif opcion == 2:
    print("haz bajado por la alcantarilla y haz encontrado un troso de madera en forma de palo\n")
    palo = False
    palo_recojido = int(input("recojes el palo?\n"
                              "1)si\n"
                              "2)no\n"))
    if palo_recojido == 1:
        palo = True
    else:
        palo = False
    print("genial ahora sigues avanzando\n"
          "encuentras a una rata gigante\n"
          "te propone que si le contestas correctamente te dejara vivir\n")
    rata = random.randint(1, 100)
    print("la rata te pregunta cuanto es 5 * {}".format(rata))
    respuesta = int(input("cual es tu respuesta?: "))
    if respuesta == 5 * rata:
        print("uys la rata te ha matado resulta que no le gutan los cerebritos\n"
              "GAME OVER")
        exit()
    elif respuesta != 5 * rata:
        print("la rata te a tenido piedad por lo tonto que eres y te deja pasar\n"
              "sigues caminando y te encuentras con 2 caminos")
        opcion = int(input("cual tomas?\n"
                           "1)derecha\n"
                           "2)izquierda\n"))
        if opcion == 1:
            print("al parecer haz dado hacia un barranco y haz muerto\n"
                  "GAMEOVER")
        elif opcion == 2:
            print("haz encontrado una salida al mar, que buena suerte")
            opcion = int(input("hacia donde nadaras?\n"
                               "1)a la playa\n"
                               "2)a un barco cercano"))
            if opcion == 1:
                print("al parecer no haz podido llegar te ha comido un tiburon\n"
                      "GAME OVER ")
                exit()
            elif opcion == 2:
                print("haz subido al barco y te haz encontrado con un viejito")
                opcion = int(input("que haras?\n"
                                   "1)golpear al viejito\n"
                                   "2)regresar al agua\n"))
                if opcion == 1 and palo:
                    print("haz golpeado al viejito con el palo que tenias\n"
                          "genial te apoderaste del barco ahora eres libre\n"
                          "HAZ GANADO EL JUEGO FELICITACIONES")
                elif opcion == 1:
                    print("creo que el palo te hubiera servido en esta ocaccion\n"
                          "el viejito tiene un arma y te dispara\n"
                          "GAME OVER")
                    exit()
                elif opcion == 2:
                    print("al parecer los tiburones te estaban esperando\n"
                          "te han comido y moriste\n"
                          "GAME OVER")
                    exit()
                else:
                    print("no haz echo nada haci que el viejito te ha disparado\n"
                          "GAME OVER")
                    exit()
            else:
                print("no te haz movido asi que los tiburones fueron por ti y te comieron\n"
                      "GAME OVER")
                exit()
        else:
            print("no te haz movido\n"
                  "a la rata le dio hambre y te busco para comerte\n"
                  "la rata te come, al parecer tienes buen sabor\n"
                  "GAME OVER")
            exit()
    else:
        print("al parecer no haz echo nada y a la rata le dio hambre\n"
              "te ha comido\n"
              "GAME OVER")
        exit()
elif opcion == 3:
    print("genial saliste a la azotea\n"
          "al pareces una paloma radeoactiva te ha cagado la cabeza\n"
          "te haz muerto\n"
          "GAME OVER")
    exit()
else:
    print('te evaporaste instantaneamente\n'
          'que mala suerte\n'
          'GAME OVER')
    exit()