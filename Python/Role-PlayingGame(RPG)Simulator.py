class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")


class Enemy:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated.")


# Using the classes
player = Character("Hero", 5, 100)
enemy = Enemy("Dragon", 7, 200)
player.attack(enemy)
enemy.take_damage(50)
