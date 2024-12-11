def rank(rank: str):
    print("\n", end="")
    for letter in "Rangod: ":
        print(letter, end="")
        time.sleep(0.2)
    time.sleep(1)
    print(f"--- {rank} ---")
    time.sleep(2)

def judge(dialouge: str, sec: int):
    print("\n", end="")
    for letter in dialouge:
        print(letter, end="")
        time.sleep(0.05)
    print("")
    time.sleep(sec)

def angry(dialouge: str, sec: int):
    print("\n", end="")
    for letter in dialouge:
        print(letter, end="")
        time.sleep(0.3)
    print("")
    time.sleep(sec)

def title(title: str, sec: int):
    print("\n", end="")
    for letter in title:
        print(letter, end="")
        time.sleep(0.005)
    print("")
    time.sleep(sec)

import random
import os
import time

names = ["Glorb", "Bintos", "Kolasimo", "Paurtil", "Kaloslav", "Jondes", "Giemothus", "Comitus", "Hárs", "Ganickin", "Putillion", "Gerius", "Barnabion", "Greg"]

act = ""

user_max_hp = random.randint(80, 120)
user_atk = random.randint(8, 12)

user_alive = True

user_hp = user_max_hp

kills = 0

wave = 1

parry = False
blocked = False
escape = False

suicide = False
cheat = False

os.system("cls")

title("""

    ____  ____  ______                               
   / __ \/ __ \/ ____/     ____ _____ ____  ____ _____ 
  / /_/ / /_/ / / ________/ __ `/ __ `/ _ \/ __ `__  /
 / _, _/ ____/ /_/ /_____/ /_/ / /_/ /  __/ / / / / /
/_/ |_/_/    \____/      \__, /\__,_/\___/_/ /_/ /_/ 
                        /____/                       

           a generic rpg game by: Skuli

""", 1)
input("\nNyomj ENTER-t!")

while user_alive == True:
    os.system("cls")

    if wave % 5 == 0:
            user_atk += int((wave/5))
            user_max_hp += wave
            title("""
 _                    _   _   _       
| |                  | | | | | |      
| |     _____   _____| | | | | |_ __  
| |    / _ \ \ / / _ \ | | | | | '_ \ 
| |___|  __/\ V /  __/ | | |_| | |_) |
\_____/\___| \_/ \___|_|  \___/| .__/ 
                               | |    
                               |_|   \n
            """, 1)
            print(f"Gratulálok, elérted a {wave}. kört!")
            time.sleep(1)
            print(f"\nÚj maximum életerő: {user_max_hp}\nÚj támadási erő: {user_atk-2}-{user_atk+2}")
            time.sleep(1)
            input("\nNyomj ENTER-t a továbblépéshez!")
    
    if user_hp > user_max_hp:
        user_hp = user_max_hp

    user_hp = round(user_hp)
    user_max_hp = round(user_max_hp)
    user_atk = round(user_atk)

    os.system("cls")

    user_luck = random.randint(1, 100)

    enemy_alive = True

    enemy_max_hp = round(random.uniform((30 + (2 * wave)), (50 + (2 * wave))))
    enemy_def_atk = round(random.uniform((2 + wave/4), (4 + wave/4)))
    enemy_name = random.choice(names)

    enemy_hp = enemy_max_hp
    enemy_atk = enemy_def_atk

    while enemy_alive == True:
        os.system("cls")

        title("""
______ _       _     _   
|  ___(_)     | |   | |  
| |_   _  __ _| |__ | |_ 
|  _| | |/ _` | '_ \| __|
| |   | | (_| | | | | |_ 
\_|   |_|\__, |_| |_|\__|
          __/ |          
         |___/  \n
        """, 1)

        print(f"{wave}. kör\n")

        run = 0

        print(f"A te életerőd: {user_hp}/{user_max_hp}\nA te támadóerőd: {user_atk-2}-{user_atk+2}\nA te szerencséd: {user_luck}/100\n")
        time.sleep(1)

        print(f"{enemy_name} életereje: {enemy_hp}/{enemy_max_hp}\n{enemy_name} támadóereje: {enemy_atk-1}-{enemy_atk+1}\n")
        time.sleep(1)

        while True:
            act = (input("Mit teszel?\n1 - Támadás\n2 - Védekezés\n3 - Menekülés\n>>> "))
            if act == "1":
                crit = random.randint(1, 100)
                miss = random.randint(1, 20)
                if miss == 20:
                    time.sleep(1)
                    print("\nNem talált")
                    break
                elif crit <= (user_luck/5):
                    user_damage = ((user_atk + random.randint(-2, 2)) * 2)
                    enemy_hp -= user_damage
                    time.sleep(1)
                    print("\nKRITIKUS TÁMADÁS!")
                    print(f"\n{user_damage}-t sebeztél {enemy_name}-ba")
                    break
                else:
                    user_damage = (user_atk + random.randint(-2, 2))
                    enemy_hp -= user_damage
                    time.sleep(1)
                    print(f"\nTe {user_damage}-t sebeztél {enemy_name}-ba")
                    break
            elif act == "2":
                block = random.randint(1, 100)
                if block <= (user_luck/2):
                    parry = True
                else:
                    blocked = True
                print("\nVédekezel")
                break
            elif act == "3":
                run = random.randint(1, 100)
                if run <= user_luck:
                    escape = True
                    break
                else:
                    time.sleep(1)
                    print("\nNem sikerült elmenekülni")
                    break
            elif act == "killself":
                user_hp = 0
                suicide = True
                break
            elif act == "uwu":
                print("\nDEVMODE ON\n")
                wave = int(input("wave >>> "))
                kills = int(input("kills >>> "))
                user_max_hp = int(input("hp >>> "))
                user_hp = user_max_hp
                user_atk = int(input("atk >>> "))
                user_luck = int(input("luck >>> "))
                if input("kill enemy? (y/n) >>> ") == "y":
                    enemy_hp -= 999
                if input("kill self? (y/n) >>> ") == "y":
                    user_hp -= 999
                break
            elif act == "kill":
                enemy_hp = 0
                cheat = True
                break
            elif act == "cheat":
                print("\nCHEATS ACTIVATED")
                wave = int(input("wave >>> "))
                kills = int(input("kills >>> "))
                cheat = True
                break
            else:
                print("\nNincs ilyen lehetőség\n")
                time.sleep(1)

        if run <= user_luck and escape == True:
            escape = False
            wave += 1
            time.sleep(1)
            print("\nElmenekültél")
            time.sleep(2)
            print("\nKözeledik egy új ellenség!")
            time.sleep(1)
            input("\nNyomj ENTER-t a továbblépéshez!")
            break

        if enemy_hp <= 0:
            enemy_alive = False
            user_hp += random.randint(10, 20)
            kills += 1
            wave += 1
            time.sleep(1)
            print(f"\nMegölted {enemy_name}-t!")
            time.sleep(1)
            print(f"\nFelgyógyultál egy kicsit")
            time.sleep(1)
            print("\nKözeledik egy új ellenség!")
            time.sleep(1)
            input("\nNyomj ENTER-t a továbblépéshez!")
            break

        time.sleep(1)
        print(f"\n{enemy_name} támad!")
        miss = random.randint(1, 20)
        crit = random.randint(1, 20)
        if miss == 20:
            time.sleep(1)
            print(f"\n{enemy_name} nem talált")
        else:
            if parry == True:
                parry = False
                if crit == 20:
                    enemy_damage = round(((enemy_atk + random.randint(-1, 1)) * 2))
                    enemy_hp -= enemy_damage
                    enemy_hp = round(enemy_hp)
                    time.sleep(1)
                    print("\nKRITIKUS PARRY!")
                    print(f"\n{enemy_name} támadását visszafordítottad, így {enemy_damage}-t sebződött")
                else:
                    enemy_damage = round((enemy_atk + random.randint(-1, 1)))
                    enemy_hp -= (enemy_damage/2)
                    enemy_hp = round(enemy_hp)
                    time.sleep(1)
                    print("\nPARRY!")
                    print(f"\n{enemy_name} támadását visszafordítottad, így {enemy_damage}-t sebződött")
            elif blocked == True:
                blocked = False
                if crit == 20:
                    enemy_damage = round((enemy_atk + random.randint(-1, 1)))
                    user_hp -= enemy_damage
                    time.sleep(1)
                    print("\nKRITIKUS TÁMADÁS!")
                    print(f"\n{enemy_name} {enemy_damage}-t sebzett beléd")
                else:
                    enemy_damage = round(((enemy_atk + random.randint(-1, 1)) / 2))
                    user_hp -= enemy_damage
                    time.sleep(1)
                    print(f"\n{enemy_name} {enemy_damage}-t sebzett beléd")
            else:
                if crit == 20:
                    enemy_damage = round(((enemy_atk + random.randint(-1, 1)) * 2))
                    user_hp -= enemy_damage
                    time.sleep(1)
                    print("\nKRITIKUS TÁMADÁS!")
                    print(f"\n{enemy_name} {enemy_damage}-t sebzett beléd")
                else:
                    enemy_damage = round((enemy_atk + random.randint(-1, 1)))
                    user_hp -= enemy_damage
                    time.sleep(1)
                    print(f"\n{enemy_name} {enemy_damage}-t sebzett beléd")

        if user_hp <= 0:
            user_alive = False
            time.sleep(1)
            title("""
__   __           ______ _          _ 
\ \ / /           |  _  (_)        | |
 \ V /___  _   _  | | | |_  ___  __| |
  \ // _ \| | | | | | | | |/ _ \/ _` |
  | | (_) | |_| | | |/ /| |  __/ (_| |
  \_/\___/ \__,_| |___/ |_|\___|\__,_|\n
            """, 1)
            print(f"\nMeghaltál!\nÖléseid száma: {kills}\nNyert köreid száma: {wave-1}")
            time.sleep(1)
            if suicide == True:
                rank("Öngyilkos")
                judge("Oh, erre nem számítottam...", 2)
                angry("Miért?", 2)

            elif cheat == True:
                rank("Mocskos csaló")
                judge("Ha ezt olvasod, akkor szégyelld magad", 1)
                angry("Tünés a szemem elől...", 1)

            elif kills == 0:
                if wave == 1:
                    rank("Abszolút vesztes")
                    angry("...", 2)
                    judge("Komolyan? Még egy körnél sem voltál képes továbbjutni?", 1)
                    judge("Csalódtam benned... Többet ne is lássalak!", 1)

                elif wave < 20:
                    rank("Ijedős nyúl")
                    judge("Nem öltél meg senkit, csak folyamatosan menekültél...", 1)
                    judge("Hát, ez a te döntésed volt, nem is jutottál túl messzire", 1)
                    judge("Legközelebb lehetnél egy kicsit keményebb, csak egy kis jótanács", 1)
                    judge("Most tünés! Szedd a lábaidat kisnyuszi!", 1)

                else:
                    rank("Igazi pacifista")
                    judge("Nem öltél meg senkit, és sokáig is jutottál", 1)
                    judge("Te aztán tényleg elkötelezett vagy", 2)
                    judge("Hé, legalább nem írtottad ki az egész népességet! Ezért büszke lehetsz magadra", 1)
                    judge("Adieu! Remélem még találkozunk", 1)

            elif kills == wave-1:
                if kills <= 10:
                    rank("Gyilkos növendék")
                    judge("Rossz úton jársz kölyök", 1)
                    judge("Ha így folytatod, rengetegen fognak szenvedni csak miattad", 1)
                    judge("Ajánlom, hogy megváltozzál mire újra találkozunk...", 1)

                else:
                    rank("Vérbeli gyilkos")
                    judge("Megöltél mindenkit aki az utadba állt...", 2)
                    angry("...", 2)
                    act = input("\nBüszke vagy magadra? (igen / nem)\n>>> ")
                    time.sleep(2)
                    if act.lower() == "igen":
                        judge("Hm...", 2)
                        judge("Legalább őszinte vagy magaddal", 1)
                        angry("Te szívtelen szörny", 1)
                    elif act.lower() == "nem":
                        judge("Aha, persze", 1)
                        judge("Engem nem csapsz be!", 1)
                    else:
                        judge("Mindegy mit mondasz", 1)
                        judge("Most már nem számít", 1)
                    judge("Most távozz!", 1)

            elif wave < 5:
                rank("Gyenge harcos")
                judge("Nem jutottál túl messzire, de ez nem jelenti, hogy nincs benned potenciál", 1)
                judge("Gyerünk, állj fel, és próbáld újra!", 1)
                judge("Legközelebb majd jobban sikerül", 1)
            
            elif wave < 10:
                rank("Közepes katona")
                judge("Viszonylag messzire eljutottál, ez dicséretes", 1)
                judge("Tudom, hogy te jobbat tudsz ennél, próbálkozz meg mégegyszer", 1)

            elif wave < 15:
                rank("Átlagos kardforgató")
                judge("Két alkalomma fejlődtél a kalandod során", 1)
                judge("Körülbelül eddig jut el egy átlagos ember ha nem menekül állandóan", 1)
                judge("Legközelebb majd jobban sikerül, addig is a viszontlátásra!", 1)

            elif wave < 25:
                rank("Tapasztalt túlélő")
                judge("Gratulálok, nem sokan jutottak el ilyen sokáig!", 1)
                judge("Büszke lehetsz magadra, én az vagyok", 1)
                judge("Remélem még találkozunk, Mester", 1)
            
            elif wave >= 25:
                rank("Valóságos legenda")
                judge("Minden tiszteletem!", 1)
                judge("Soha senki nem jutott el olyan messzire, mint te", 1)
                judge("És a megérdemelt jutalmad...", 3)
                angry("Cheat Kódok!", 1)
                judge("A cheat kódok: cheat, kill, killself", 1)
                judge("Használd egészséggel ;)", 1)

            else:
                rank("ERROR")
                judge("Upsz, valami nem oké", 1)
                judge("Bocsi a kellemetlenségért!", 1)
            break
        input("\nNyomj ENTER-t a továbblépéshez!")

input("\n\n\n\nNyomj ENTER-t a kilépéshez!")