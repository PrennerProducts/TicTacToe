from IPython.display import clear_output

def spielfeld_anzeigen(spielfeld):
   clear_output()

 
   print(" "+ spielfeld[1]+ " | " + spielfeld[2]+ " | " + spielfeld[3])
   print("-----------")
   print(" "+ spielfeld[4]+ " | " + spielfeld[5]+ " | " + spielfeld[6])
   print("-----------")
   print(" "+ spielfeld[7]+ " | " + spielfeld[8]+ " | " + spielfeld[9])
  

spielfeld = ["X"] *10
spielfeld_anzeigen(spielfeld)


def spieler_eingabe():
    markierung = ""
    while not (markierung== "X" or markierung == "O"):
        markierung = input("Spieler 1: Willst du X oder O sein?") .upper()
    
    if markierung == "X" :
        return ("X", "O")
    else:
        return("O", "X")
    
spieler_eingabe()


def markierung_setzen(speilfeld, markierung, position):
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