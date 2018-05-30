import json


class Hero:  # Définition de notre classe Hero
    """Classe définissant un hero caractérisée par :
    - life
    - canFly
    - name
    - strength
    - speed
    - position"""

    def __init__(self, name='heroe', life=50, strength=5, speed=1, canFly=False,
                 position=(2, 5)):  # Notre méthode constructeur
        self.name = name
        self.life = life
        self.strength = strength
        self.speed = speed
        self.canFly = canFly

    def move(self, x, y):
        self.position = (x, y)

    def troll(self):
        print(self + ' : Tu va crever')

    def punch(self, enemy):
        print(" BAM *** ")
        enemy.life = enemy.life - (self.speed * self.strength)

    def __str__(self):
        return "Hero instance with name is %s" % self.name

    @classmethod
    def get_by_conf(cls, name='superman'):
        hero = None

        with open('conf/heroes.json') as confs_file:
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

    @classmethod
    def get_by_id(cls, id):
        with open("conf/heroes.json") as confs_file:
            config = json.load(confs_file)

        for name in config:
            if int(config[name]['id']) == id:
                hero_data = config[name]
                return Hero(name, hero_data['life'], hero_data['strength'], hero_data['speed'], hero_data['canFly'])

        return None
