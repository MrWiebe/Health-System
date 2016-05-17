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
        
import Tkinter

root = Tkinter.Tk()

scrollbar = Tkinter.Scrollbar(root)
scrollbar.pack(side=Tkinter.RIGHT, fill = Tkinter.Y)

listbox = Tkinter.Listbox(root)
listbox.pack()

button = Tkinter.Button(root, text='Quit', width=10, height = 5, command = root.destroy)
button2 = Tkinter.Button(root, text='New Window', width=10, height = 5, command = root.destroy)
button.pack(side = Tkinter.LEFT)
button2.pack(side = Tkinter.LEFT)

for i in range(100):
    listbox.insert(Tkinter.END, i)

# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


Tkinter.mainloop()