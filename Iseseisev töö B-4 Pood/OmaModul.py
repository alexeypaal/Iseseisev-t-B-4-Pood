from math import *
from random import *

def pood():
    
    num_items = int(input("Sisestage toode kogus: "))# Запрос кол-ва продуктов
    
    
    ostud = []#списки 
    hinnad = []
    
    
    for i in range(num_items):
        item = input(f"Sisestage toode {i+1} nimetus: ")# Заполнение списков
        price = float(input(f"Sisestage toode {i+1} hind: "))
        ostud.append(item)
        hinnad.append(price)
    
      
        valik = int(input("Sisestage toimingu number: "))# Меню выбора действий
        
        if valik == 1:
            item = input("Sisestage ostetud toode nimetus: ")
            if item in ostud:
                index = ostud.index(item)
                del ostud[index]
                price = hinnad.pop(index)
                print(f"{item} за {price} eur. on lisatud ostetud kaupade nimekirja.")
                # TODO: составить чек
            else:
                print(f"Toode {item} ei leitud ostunimekirjast.")
        
        elif valik == 2:
            sorted_purchases = sorted(ostud)
            print("Ostunimekiri ja nende hinnad:")
            for item, price in zip(sorted_purchases, hinnad):
                print(f"{item}: {price} eur.")
        
        elif valik == 3:
            max_price = max(hinnad)
            index = hinnad.index(max_price)
            item = ostud[index]
            print(f"Kõige kallim toode: {item} за {max_price} eur.")
        
        elif valik == 4:
            min_price = min(hinnad)
            index = hinnad.index(min_price)
            item = ostud[index]
            print(f"Kõige odavaim toode: {item} за {min_price} eur.")
        
        elif valik == 5:
            item = input("Sisestage toode nimetus: ")
            if item in ostud:
                index = ostud.index(item)
                price = hinnad[index]
                print(f"Toode hind {item}: {price} eur.")
            else:
                print(f"Toode {item} ostunimekirjast ei leitud.")
        
        elif valik == 6:
            break
        
        else:
            print("Vale valik!!!!!!")

        print()