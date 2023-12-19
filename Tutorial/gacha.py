import random
from datetime import datetime


now = datetime.now()

tech = ['Up size', '+1 topping', 'Discount 10%', 'Discount 20%', 'Play Station 5']
weight = [1, 1, 0.2, 0.1, 0.003]


for i in range(1, 100):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    print(random.choices(tech, weights = weight))
    