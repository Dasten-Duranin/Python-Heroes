import json

class Hero: # Définition de notre classe Hero 
    """Classe définissant un hero caractérisée par :
    - life
    - canFly
    - name
    - strength
    - speed
    - position"""

    def __init__(self, name = 'heroe', life = 50, strength = 5, speed = 1, canFly = False, position = (2, 5)): # Notre méthode constructeur
        self.name     = name
        self.life     = life
        self.strength = strength
        self.speed    = speed
        self.canFly   = canFly
        self.position = position

    def __str__(self):
        return "Hero instance with name is%s"%self.name

    @classmethod
    def getByConf(cls, name = 'superman'):
        hero = None

        with open('../conf/heroes.json') as confs_file:
            confs = json.load(confs_file)

            if name in confs:
                conf = confs[name]
                conf['name'] = name
                hero = cls(**conf)
            else:
                print('hero doesen\'t exist, you\'ll get the default hero')

        if hero is None:
            hero = cls()

        return hero
