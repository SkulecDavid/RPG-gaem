import random
import os
import time

names = ["Glorb", "Bintos", "Kolasimo", "Paurtil", "Kaloslav", "Jondes", "Giemothus", "Comitus", "Hárs", "Ganickin", "Putillion", "Gerius", "Barnabion"]

act = ""

user_max_hp = random.randint(80, 120)
user_atk = random.randint(8, 12)

user_alive = True

user_hp = user_max_hp

kills = 0

wave = 0

while user_alive == True:
    os.system("cls")

    user_luck = random.randint(1, 70)

    enemy_alive = True

    enemy_max_hp = int(random.randrange((30 + (2 * wave)), (60 + (2 * wave))))
    enemy_def_atk = int(random.randrange((2 + wave/4), (4 + wave/4)))
    enemy_name = random.choice(names)

    enemy_hp = enemy_max_hp
    enemy_atk = enemy_def_atk

    while enemy_alive == True:
        os.system("cls")

        print(f"{wave + 1}. kör\n")

        run = 0

        print(f"A te életerőd: {user_hp}\nA te támadóerőd: {user_atk}\nA te szerencséd: {user_luck}\n")
        time.sleep(1)

        print(f"{enemy_name} életereje: {enemy_hp}\n{enemy_name} támadóereje: {enemy_atk}\n")
        time.sleep(1)

        while True:
            act = (input("Mit teszel?\n1 - Támadás\n2 - Védekezés\n3 - Menekülés\n"))
            if act == "1":
                crit = random.randint(1, 100)
                miss = random.randint(1, 20)
                if miss == 20:
                    time.sleep(1)
                    print("Nem talált")
                    break
                elif crit <= user_luck:
                    user_damage = ((user_atk + random.randint(-2, 2)) * 2)
                    enemy_hp -= user_damage
                    time.sleep(1)
                    print("\nKRITIKUS TÁMADÁS")
                    print(f"\n{user_damage}-t sebeztél {enemy_name}-ba")
                    break
                else:
                    user_damage = (user_atk + random.randint(-2, 2))
                    enemy_hp -= user_damage
                    time.sleep(1)
                    print(f"\nTe {user_damage}-t sebeztél {enemy_name}-ba")
                    break
            elif act == "2":
                if user_hp < user_max_hp:
                    heal = random.randint(1, 10)
                    user_hp += heal
                    time.sleep(1)
                    print(f"\nGyógyultál {heal} HP-t")
                    break
                else:
                    time.sleep(1)
                    print("\nMAX HP")
                    break
            elif act == "3":
                run = random.randint(0, 10)
                if run >= user_luck:
                    wave += 1
                    time.sleep(1)
                    print("\nElmenekültél")
                    time.sleep(2)
                    print("Közeledik egy új ellenség!")
                    time.sleep(1)
                    input("Nyomj ENTER-t a továbblépéshez!")
                    break
                else:
                    time.sleep(1)
                    print("\nNem sikerült elmenekülni")
                    time.sleep(1)
                    break
            else:
                print("\nNincs ilyen lehetőség")
                time.sleep(1)

        if run >= user_luck:
            break

        if enemy_hp <= 0:
            enemy_alive = False
            user_atk += 1
            user_hp += random.randint(10, 20)
            kills += 1
            wave += 1
            time.sleep(1)
            print(f"\nMegölted {enemy_name}-t!")
            time.sleep(1)
            print("Közeledik egy új ellenség!")
            time.sleep(1)
            input("Nyomj ENTER-t a továbblépéshez!")
            break

        time.sleep(1)
        print(f"\n{enemy_name} támad!")
        miss = random.randint(1, 5)
        crit = random.randint(1, 6)
        if miss <= (user_luck / 2):
            time.sleep(1)
            print(f"\n{enemy_name} nem talált")
        elif crit == 6:
            enemy_damage = ((enemy_atk + random.randint(-2, 2)) * 2)
            user_hp -= enemy_damage
            time.sleep(1)
            print("\nKRITIKUS TÁMADÁS")
            print(f"\n{enemy_name} {enemy_damage}-t sebzett beléd")
        else:
            enemy_damage = (enemy_atk + random.randint(-2, 2))
            user_hp -= enemy_damage
            time.sleep(1)
            print(f"\n{enemy_name} {enemy_damage}-t sebzett beléd")

        if user_hp <= 0:
            user_alive = False
            time.sleep(1)
            print(f"\nMeghaltál! Öléseid száma: {kills}")
            break

        time.sleep(1)
        input("Nyomj ENTER-t a továbblépéshez!")

input()