from abc import ABC, abstractmethod

# Абстрактный класс персонажа
class Creature(ABC) :
  @abstractmethod
  def rocket(self) :
    pass
  
# Конкретная реализация
class Angel(Creature) :
    def rocket(self) :
      return "Плавный взлет"
    
class Demon(Creature) :
    def rocket(self) :
      return "Резкий взлет"
        
# Фабричный метод
class CreatureFactory :
  @staticmethod
  def create_creature(creature_act) :
    if creature_act == "Полет ангела":
      return Angel()
    elif creature_act == "Полет демона":
      return Demon()
    else:
      raise ValueError("Неизвестный персонаж: {creature_act} ")
          
# Демонстрация
creature1 = CreatureFactory.create_creature("Полет ангела")
creature2 = CreatureFactory.create_creature("Полет демона")
print(creature1.rocket()) # Плавный взлет
print(creature2.rocket()) # Резкий взлет 