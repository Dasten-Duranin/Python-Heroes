class Hero: # Définition de notre classe Hero 
    """Classe définissant un hero caractérisée par :
    - life
    - canFly
    - name
    - strength
    - speed
    - position"""

    def __init__(self, name = 'heroe', life = 50, strength = 5, speed = 1, canFly = false, position = (2, 5)): # Notre méthode constructeur
        self.name     = name
        self.life     = life
        self.strength = strength
        self.speed    = speed
        self.canFly   = canFly
        self.position = position
