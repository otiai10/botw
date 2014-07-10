import random
from system import conf

print(random.randrange(100))

print((random.random() < conf.monologue_rate))
