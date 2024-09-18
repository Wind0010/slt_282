class Flying:
    def __init__(self):
        self.state = "на земле"

    def fly(self):
        self.state = "в воздухе"
        print(f"Амфибия теперь: {self.state}")

class Swimming:
    def __init__(self):
        self.state = "на земле"

    def swim(self):
        self.state = "в воде"
        print(f"Амфибия теперь: {self.state}")

class Amphibian(Flying, Swimming):
    def __init__(self):
        super().__init__()
        self.state = "на земле"

    def land(self):
        self.state = "на земле"
        print(f"Амфибия теперь: {self.state}")

    def get_state(self):
        print(f"Текущее состояние амфибии: {self.state}")


amphibian = Amphibian()


amphibian.get_state()


amphibian.fly()
amphibian.get_state()


amphibian.land()
amphibian.get_state()


amphibian.swim()
amphibian.get_state()

amphibian.land()
amphibian.get_state()

