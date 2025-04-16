class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} just ate. Hunger is now {self.hunger}, Happiness is now {self.happiness}.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy is now {self.energy}.")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            return
        self.energy -= 2
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played and is now happier! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}.")

    def get_status(self):
        print(f"🐾 {self.name}'s Status:\n  Hunger: {self.hunger}\n  Energy: {self.energy}\n  Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")



# class Pet:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 5
#         self.energy = 5
#         self.happiness = 5
#         self.tricks = []

#     def eat(self):
#         # TODO

#     def sleep(self):
#         # TODO

#     def play(self):
#         # TODO

#     def train(self, trick):
#         # TODO

#     def show_tricks(self):
#         # TODO

#     def get_status(self):
#         # TODO
