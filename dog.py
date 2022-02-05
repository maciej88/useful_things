
class Dog():
    """Prosta poba modelowania psa"""

    def __init__(self, name, age):
        """inicjalizacja atrybuow name i aget"""
        self.name = name
        self.age = age

    def sit(self):
        """symulacja siadania"""
        print(f"{self.name.title()} teraz siedzi")

    def roll_over(self):
        """symulacja tzania sie psa"""
        print(f"{self.name.title()} terez kula sie")
