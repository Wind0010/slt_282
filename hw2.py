class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    
    def get_name(self):
        return self.name

    
    def double_health(self):
        self.health_points *= 2

    
    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"

    
    def __len__(self):
        return len(self.catchphrase)
hero = SuperHero(
    name="Clark Kent",
    nickname="Superman",
    superpower="Flight",
    health_points=100,
    catchphrase="Up, up and away!"
)


print(hero.get_name())  
hero.double_health()   
print(hero)        
print(len(hero))      


class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = fly

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, wing_span):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.wing_span = wing_span

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the {self.catchphrase}"


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, terrain):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.terrain = terrain

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the {self.catchphrase}"


class Villain(SuperHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)

    def gen_x(self):
        pass  

    def crit(self, hero):
        if isinstance(hero, SuperHero):
            hero.damage **= 2


air_hero = AirHero(
    name="Maverick",
    nickname="SkyMaster",
    superpower="Supersonic Flight",
    health_points=120,
    catchphrase="The sky's the limit!",
    damage=50,
    wing_span=10
)

earth_hero = EarthHero(
    name="Rocky",
    nickname="Earthquake",
    superpower="Seismic Powers",
    health_points=150,
    catchphrase="Feel the ground shake!",
    damage=40,
    terrain="Mountains"
)

villain = Villain(
    name="Dr. Doom",
    nickname="The Destroyer",
    superpower="Destruction Beam",
    health_points=200,
    catchphrase="Bow before me!",
    damage=80
)

# Применяем методы

print(air_hero.get_name())        
air_hero.double_health()        
print(air_hero)                   
print(len(air_hero))              
print(air_hero.true_phrase())   

print(earth_hero.get_name())     
earth_hero.double_health()       
print(earth_hero)            
print(len(earth_hero))            
print(earth_hero.true_phrase())  


villain.crit(air_hero)
print(f"Air Hero's damage after crit: {air_hero.damage}")  
# :)
