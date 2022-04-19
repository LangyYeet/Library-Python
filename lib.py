class Prestup:
    'Knihovna vytvorena za ucelem zjednoduseni vypoctu prestupneho roku.'
    
    def __init__(self):
        self.year = int(input("zadej rok:"))


    def icheckYear(self):
        if self.year % 4 == 0: print("Rok je prestupny.")
        elif self.year % 100 == 0: print("Rok neni prestupny. ")
        elif self.year % 400 == 0: print("Rok je prestupny.")
        else: print("rok neni prestupny.")
'Zkontroluje zda-li je rok prestupny ci ne.'