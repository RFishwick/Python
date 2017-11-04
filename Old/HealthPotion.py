import random
import math
difficulty = 3
health = 50
potion_health = int(random.randint(25,50) / difficulty)
print(potion_health)

health += potion_health
print(health)