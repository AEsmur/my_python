import random
class Hero:
    def __init__(self, x, y, power, name = "NoName"):
        self.name = name
        self.x = x
        self.y = y
        self.z = 0 
        self.hp = 100
        self.power = power
        self.alive = True
        print("\nHero", name, "with 100 health and",
              self.power, "power is created")
    def run(self, dx, dy):
        if self.alive:
            self.x += dx
            self.y += dy
            print("\n", self.name, "ran from coordinates",
                  (self.x - dx, self.y - dy), "to",
                  (self.x, self.y), "\n")
    def shoot(self, enemy):
        if self.alive:
            enemy.hp -= self.power
            print(self.name, "fires to", enemy.name,
                  "\nNow", enemy.name, "has", enemy.hp, "health\n")
            if enemy.hp <= 0:
                print(enemy.name, "is dead")
                enemy.alive = False
    def claim(self, obj):
        if self.alive:
            if self.x == obj.x and self.y == obj.y:
                self.hp -= obj.damage
                self.hp += obj.health_boost
                self.power += obj.power_boost
                print(self.name, "claimed", obj.name,
                      "\nNow he has", self.hp,
                      "health and", self.power, "power\n")
                
class FlyingHero(Hero):
    def fly(self, dz):
        self.z += dz
        print("Wow! This hero has an ability to fly!\nAnd",
              self.name, "now is at height", self.z, "\n")
    
class Object:
    def __init__(self):
        self.x = random.randint(0, 2) #на земле в случайных точках
        self.y = random.randint(0, 2) #карты создаются предметы
        self.z = 0
class Bomb(Object):
    def __init__(self, damage):
        Object.__init__(self)
        print("bomb is at", (self.x, self.y, self.z),
              "and it has", damage, "damage")
        self.damage = damage
        self.health_boost = 0
        self.power_boost = 0
        self.name = "bomb"
class HP_Booster(Object):
    def __init__(self, health_boost):
        Object.__init__(self)
        print("health booster is at", (self.x, self.y, self.z),
              "and it restores", health_boost, "health")
        self.damage = 0
        self.health_boost = health_boost
        self.power_boost = 0
        self.name = "hp_booster"
class Power_Booster(Object):
    def __init__(self, power_boost):
        Object.__init__(self)
        print("power booster is at", (self.x, self.y, self.z),
              "and it gives", power_boost, "more power")
        self.damage = 0
        self.health_boost = 0
        self.power_boost = power_boost
        self.name = "power_booster"
    
#создаём предметы и героев
bomb = Bomb(3)
bomb2 = Bomb(2)
bomb3 = Bomb(9)
hp = HP_Booster(4)
hp2 = HP_Booster(1)
hp3 = HP_Booster(16)
hp4 = HP_Booster(6)
power = Power_Booster(7)
power2 = Power_Booster(3)

hero1 = Hero(1, 1, 5, "Somebody")
hero2 = Hero(0, 0, 10, "Once")
hero3 = Hero(3, 0, 8, "Told")
hero4 = Hero(0, 2, 12, "Me")
hero5 = FlyingHero(2, 1, 66, "Thanos")

#действия героев
hero1.run(1, 1)
hero1.shoot(hero2)
hero4.run(0, -2)

hero5.fly(3)
hero5.fly(4)
hero5.fly(-7)

#собирание предметов. Если в данной клетке есть предмет, герой
#забирает его. Иначе — ...ничего не происходит
hero1.claim(bomb2)
hero1.claim(bomb3)
hero1.claim(hp3)
hero2.claim(bomb)
hero2.claim(hp4)
hero3.claim(power)
hero4.claim(hp)
hero5.claim(bomb)
hero5.claim(bomb2)
hero5.claim(bomb3)

#итоги
print("Final results\n", hero1.name, "has", hero1.hp, "health and",
      hero1.power, "power\n", hero2.name, "has", hero2.hp,
      "health and", hero2.power, "power\n", hero3.name, "has",
      hero3.hp, "health and", hero3.power, "power\n", hero4.name,
      "has", hero4.hp, "health and", hero4.power, "power\n",
      hero5.name, "has", hero5.hp, "health and", hero5.power,
      "power\n")
