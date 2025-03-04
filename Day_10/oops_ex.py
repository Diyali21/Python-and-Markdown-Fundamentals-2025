# ## Object
# ### BMW
# - Wheels - 4
# - Engine - v8
# - model - x5
# - Doors - 4

# ### Jeep
# - Wheels - 4
# - Engine - v6
# - model - wrangler
# - Doors - 5

# ### Mclaren
# - Wheels - 4
# - Engine - v8
# - model - 650s
# - Doors - 2


class Car:
    def __init__(self, wheels, engine, model, doors):
        self.wheels = wheels
        self.engine = engine
        self.model = model
        self.doors = doors

    def horn(self):
        return "Vroom Vroom"


bmw = Car(4, "v8", "x5", 4)
jeep = Car(4, "v6", "wrangler", 5)
mclaren = Car(2, "v8", "650s", 2)
mercedes = Car(4, "v8", "G-Wagon", 4)

print(mercedes.horn())
