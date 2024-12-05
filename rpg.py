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

os.system("cls")

print("""

    ____  ____  ______                               
   / __ \/ __ \/ ____/     ____ _____ ____  ____ _____ 
  / /_/ / /_/ / / ________/ __ `/ __ `/ _ \/ __ `__  /
 / _, _/ ____/ /_/ /_____/ /_/ / /_/ /  __/ / / / / /
/_/ |_/_/    \____/      \__, /\__,_/\___/_/ /_/ /_/ 
                        /____/                       

           a generic rpg game by: Skuli

""")
input("\nNyomj ENTER-t!")

while user_alive == True:
    os.system("cls")

    if wave % 5 == 0:
            user_atk += int((wave/5))
            user_max_hp += wave
            print("""
---------------------------------------
 _                    _   _   _       
| |                  | | | | | |      
| |     _____   _____| | | | | |_ __  
| |    / _ \ \ / / _ \ | | | | | '_ \ 
| |___|  __/\ V /  __/ | | |_| | |_) |
\_____/\___| \_/ \___|_|  \___/| .__/ 
                               | |    
                               |_|   
---------------------------------------

            """)
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

        print("""
--------------------------
______ _       _     _   
|  ___(_)     | |   | |  
| |_   _  __ _| |__ | |_ 
|  _| | |/ _` | '_ \| __|
| |   | | (_| | | | | |_ 
\_|   |_|\__, |_| |_|\__|
          __/ |          
         |___/  
--------------------------

        """)

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
            print(f"\nMeghaltál!\nÖléseid száma: {kills}\nKöreid száma: {wave}")
            print("""

---------------------------------------
__   __           ______ _          _ 
\ \ / /           |  _  (_)        | |
 \ V /___  _   _  | | | |_  ___  __| |
  \ // _ \| | | | | | | | |/ _ \/ _` |
  | | (_) | |_| | | |/ /| |  __/ (_| |
  \_/\___/ \__,_| |___/ |_|\___|\__,_|
---------------------------------------
            """)
            break

        time.sleep(1)
        input("\nNyomj ENTER-t a továbblépéshez!")

input()