import random
seed = 30
random.seed(seed)
validation_set = random.sample(range(1,401),40)
training_set = [i for i in range(1,401) if i not in validation_set]
print("249: ",training_set[248])