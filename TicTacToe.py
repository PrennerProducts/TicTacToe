from IPython.display import clear_output

def spielfeld_anzeigen(spielfeld):
 
    clear_output()

    print(' ' + spielfeld[1] + ' | ' + spielfeld[2] + ' | ' + spielfeld[3])
 
    print('-----------')

    print(' ' + spielfeld[4] + ' | ' + spielfeld[5] + ' | ' + spielfeld[6])

    print('-----------')

    print(' ' + spielfeld[7] + ' | ' + spielfeld[8] + ' | ' + spielfeld[9])

 
 

  

#spielfeld = ["X"] *10
#spielfeld_anzeigen([])


def spieler_eingabe():
    markierung = " "
    while not (markierung == "X" or markierung == "O"):
        markierung = input("Spieler 1: Willst du X oder O sein? ").upper()
    
    if markierung == "X":
        return("X","O")
    else:
        return("O","X")
    
#spieler_eingabe()


def markierung_setzen(spielfeld, markierung, position):
    spielfeld[position] = markierung



def sieg_check(spielfeld, markierung):
    sieg = ((spielfeld[1] == markierung and spielfeld[2] == markierung and spielfeld [3] == markierung) or  # oben
        (spielfeld[4] == markierung and spielfeld[5] == markierung and spielfeld [6] == markierung) or # mitte
        (spielfeld[7] == markierung and spielfeld[8] == markierung and spielfeld [9] == markierung) or # unten
        (spielfeld[1] == markierung and spielfeld[4] == markierung and spielfeld [7] == markierung) or # links runter
        (spielfeld[2] == markierung and spielfeld[5] == markierung and spielfeld [8] == markierung) or # mitte runter
        (spielfeld[3] == markierung and spielfeld[6] == markierung and spielfeld [9] == markierung) or # rechts runter
        (spielfeld[1] == markierung and spielfeld[5] == markierung and spielfeld [9] == markierung) or # diagonal ol nach ur
        (spielfeld[7] == markierung and spielfeld[5] == markierung and spielfeld [3] == markierung))   # diagonal ul nach or        
    return sieg    
            


import random
def beginner():
    if random.randint(0,1) == 0:
        return "Spieler 2"
    else:
        return "Spieler 1"    

#beginner()

def platz_check(spielfeld, position):
     return spielfeld[position] == " "
        

    
def spielfeld_voll(spielfeld):
    for i in range(1,10):
        if platz_check(spielfeld, i):
            return False
    return True


def spieler_wahl(spielfeld):
    position = " "
    while position not in  "1 2 3 4 5 6 7 8 9".split() or not platz_check(spielfeld, int(position)):
        position = input("Wähle eine Position von 1-9: ")
    return int (position)
    

def neues_spiel():
    return input("Möchtest du nochmal Spielen? geb Ja oder Nein ein: ").lower().startswith("j")




print("Willkommen in meinem Supercoolen Tic Tac Toe!")

while True:
    dasFeld = [" "]*10
    spieler1_markierung, spieler2_markierung = spieler_eingabe()
    zug = beginner()
    print(zug + " darf beginnen.")
    spiel_laeuft = True

    while spiel_laeuft:
        if zug == "Spieler 1":
            spielfeld_anzeigen(dasFeld)
            position = spieler_wahl(dasFeld)
            markierung_setzen(dasFeld,spieler1_markierung,position)

            if sieg_check(dasFeld, spieler1_markierung):
                spielfeld_anzeigen(dasFeld)
                print("Gratuliere du hast gewonnen!")
                break
            else:
                if spielfeld_voll(dasFeld):
                    spielfeld_anzeigen(dasFeld)
                    print("es gibt kein Gewinner, es steht Unendschieden!")
                    break
                else:
                    zug = "Spieler 2"
        else:
            spielfeld_anzeigen(dasFeld)
            position = spieler_wahl(dasFeld)
            markierung_setzen(dasFeld, spieler2_markierung, position)

            if sieg_check(dasFeld, spieler2_markierung):
                spielfeld_anzeigen(dasFeld)
                print("Gratuliere du hast gewonnen!")
                break
            else:
                if spielfeld_voll(dasFeld):
                    spielfeld_anzeigen(dasFeld)
                    print("es gibt kein Gewinner, es steht Unendschieden!")
                    break
                else:
                    zug = "Spieler 1"

    if not neues_spiel():
        break


