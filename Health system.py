import gc
enemies = []
class _Enemy(object):
    def __init__(self, health, defense, attack):
        self.health = health
        self.defense = defense
        self._attack = attack
    def attack(self, target):
        target.take_damage(self._attack)
        return target.health
    def take_damage(self, amount):
        self.health -= amount-self.defense
        if self.health <=0:
            print 'dead'
            enemies.remove(self)
        
class Orc(_Enemy):
    def __init__(self, health=100, defense=0, attack=10):
        super(Orc, self).__init__(health, defense, attack)
        enemies.append(self)

    
orc1 = Orc()
orc2 = Orc()
def kill():
    for i in range(10):
        orc1.attack(orc2)