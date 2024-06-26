import pickle

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        """
        Конструктор класса Animal.
        Инициализирует атрибуты name (имя) и age (возраст) животного.
        """
        self.name = name
        self.age = age

    def make_sound(self):
        """
        Метод для издания звука.
        В базовом классе не определен, должен быть переопределен в подклассах.
        """
        pass

    def eat(self):
        """
        Метод для кормления животного.
        """
        print(f"{self.name} кушает")


# Подкласс Bird, наследует от Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        """
        Конструктор класса Bird.
        Инициализирует имя, возраст и размах крыльев птицы.
        """
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        """
        Переопределенный метод для издания звука птицы.
        """
        print(f"{self.name} щебечет")


# Подкласс Mammal, наследует от Animal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        """
        Конструктор класса Mammal.
        Инициализирует имя, возраст и цвет шерсти млекопитающего.
        """
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        """
        Переопределенный метод для издания звука млекопитающего.
        """
        print(f"{self.name} рычит")


# Подкласс Reptile, наследует от Animal
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        """
        Конструктор класса Reptile.
        Инициализирует имя, возраст и тип чешуи рептилии.
        """
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        """
        Переопределенный метод для издания звука рептилии.
        """
        print(f"{self.name} шипит")


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    """
    Функция для вызова метода make_sound() для каждого животного в списке.
    """
    for animal in animals:
        animal.make_sound()


# Класс Zoo для управления животными и сотрудниками
class Zoo:
    def __init__(self):
        """
        Конструктор класса Zoo.
        Инициализирует списки животных и сотрудников.
        """
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        """
        Метод для добавления животного в зоопарк.
        """
        self.animals.append(animal)

    def add_staff(self, staff_member):
        """
        Метод для добавления сотрудника в зоопарк.
        """
        self.staff.append(staff_member)

    def list_animals(self):
        """
        Метод для вывода списка животных в зоопарке.
        """
        for animal in self.animals:
            print(f"{animal.name}, Возраст: {animal.age}")

    def list_staff(self):
        """
        Метод для вывода списка сотрудников зоопарка.
        """
        for staff_member in self.staff:
            print(f"{staff_member.name}, Должность: {staff_member.__class__.__name__}")

    def save_to_file(self, filename):
        """
        Метод для сохранения информации о зоопарке в файл.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print("Зоопарк сохраняется в файл")

    @staticmethod
    def load_from_file(filename):
        """
        Метод для загрузки информации о зоопарке из файла.
        """
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print("Зоопарк загружен из файла")
        return zoo


# Базовый класс Staff для сотрудников
class Staff:
    def __init__(self, name):
        """
        Конструктор класса Staff.
        Инициализирует имя сотрудника.
        """
        self.name = name


# Подкласс ZooKeeper, наследует от Staff
class ZooKeeper(Staff):
    def feed_animal(self, animal):
        """
        Метод для кормления животного.
        """
        print(f"{self.name} кормит {animal.name}.")


# Подкласс Veterinarian, наследует от Staff
class Veterinarian(Staff):
    def heal_animal(self, animal):
        """
        Метод для лечения животного.
        """
        print(f"{self.name} лечит {animal.name}.")


# Пример использования

# Создаем экземпляр животного
animal = Animal("Кот", 5)
animal.eat()  # Выведет "Кот кушает"

# Создаем экземпляры подклассов Bird, Mammal, Reptile
bird = Bird("Попугай", 2, "Средний")
mammal = Mammal("Лев", 4, "Золотистый")
reptile = Reptile("Змея", 3, "Гладкий")

# Вызываем метод make_sound для каждого экземпляра
bird.make_sound()  # Попугай щебечет
mammal.make_sound()  # Лев рычит
reptile.make_sound()  # Змея шипит

# Демонстрация полиморфизма
animals = [bird, mammal, reptile]
animal_sound(animals)
# Попугай щебечет
# Лев рычит
# Змея шипит

# Создаем экземпляр зоопарка
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.list_animals()
# Попугай, Возраст: 2
# Лев, Возраст: 4
# Змея, Возраст: 3

# Создаем экземпляры сотрудников ZooKeeper и Veterinarian
keeper = ZooKeeper("Александр")
vet = Veterinarian("Алиса")

# Добавляем сотрудников в зоопарк и выводим их список
zoo.add_staff(keeper)
zoo.add_staff(vet)
zoo.list_staff()
# Александр, Должность: ZooKeeper
# Алиса, Должность: Veterinarian

# Используем методы сотрудников
keeper.feed_animal(bird)  # Александр кормит Попугай.
vet.heal_animal(mammal)   # Алиса лечит Лев.

# Сохраняем зоопарк в файл и загружаем его
zoo.save_to_file("zoo_data.pkl")
new_zoo = Zoo.load_from_file("zoo_data.pkl")
new_zoo.list_animals()
new_zoo.list_staff()
