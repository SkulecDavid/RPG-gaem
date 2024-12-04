import random

enemy_max_hp = round(random.uniform((30 + (2 * 5)), (60 + (2 * 5))))
enemy_def_atk = round(random.uniform((2 + 5/4), (4 + 5/4)))
print(enemy_def_atk, enemy_max_hp)