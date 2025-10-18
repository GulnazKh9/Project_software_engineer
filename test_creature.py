import pytest
from abc import ABC
from creature import Creature, Angel, Demon, CreatureFactory

# Тест абстрактного класса
class TestCreature:
    def test_creature_is_abstract(self):
        """Проверка, что Creature является абстрактным классом"""
        assert isinstance(Creature, type(ABC))
        assert hasattr(Creature, "__abstractmethods__")
        assert "rocket" in Creature.__abstractmethods__

    def test_creature_cannot_be_instantiated(self):
        """Проверка, что абстрактный класс нельзя создать напрямую"""
        with pytest.raises(TypeError):
            Creature()

# Тест конкретных реализаций
class TestAngel:
    def setup_method(self):
        self.angel = Angel()

    def test_angel_inherits_from_creature(self):
        """Проверка наследования"""
        assert isinstance(self.angel, Creature)
        assert isinstance(self.angel, Angel)

    def test_angel_rocket(self):
        """Проверка метода rocket"""
        assert self.angel.rocket() == "Плавный взлет"

class TestDemon:
    def setup_method(self):
        self.demon = Demon()

    def test_demon_inherits_from_creature(self):
        """Проверка наследования"""
        assert isinstance(self.demon, Creature)
        assert isinstance(self.demon, Demon)

    def test_demon_rocket(self):
        """Проверка метода rocket"""
        assert self.demon.rocket() == "Резкий взлет"

# Тест фабричного метода
class TestCreatureFactory:
    def test_create_angel(self):
        """Проверка создания ангела"""
        creature = CreatureFactory.create_creature("Полет ангела")
        assert isinstance(creature, Angel)
        assert creature.rocket() == "Плавный взлет"

    def test_create_demon(self):
        """Проверка создания демона"""
        creature = CreatureFactory.create_creature("Полет демона")
        assert isinstance(creature, Demon)
        assert creature.rocket() == "Резкий взлет"

    def test_invalid_creature_type(self):
        """Проверка обработки неизвестного типа персонажа"""
        with pytest.raises(ValueError) as exc_info:
            CreatureFactory.create_creature("Неизвестный полет")
        assert "Неизвестный персонаж" in str(exc_info.value)

    def test_empty_creature_type(self):
        """Проверка пустой строки"""
        with pytest.raises(ValueError) as exc_info:
            CreatureFactory.create_creature("")
        assert "Неизвестный персонаж" in str(exc_info.value)

    def test_none_creature_type(self):
        """Проверка None"""
        with pytest.raises(ValueError) as exc_info:
            CreatureFactory.create_creature(None)
        assert "Неизвестный персонаж" in str(exc_info.value)

    def test_case_sensitive_matching(self):
        """Проверка чувствительности к регистру"""
        with pytest.raises(ValueError):
            CreatureFactory.create_creature("полет ангела")

    def test_whitespace_in_creature_type(self):
        """Проверка пробелов"""
        with pytest.raises(ValueError):
            CreatureFactory.create_creature(" Полет ангела")
        with pytest.raises(ValueError):
            CreatureFactory.create_creature("Полет ангела ")

# Тесты производительности и граничных значений
class TestCreatureFactoryEdgeCases:
    def test_create_multiple_instances(self):
        """Проверка создания нескольких экземпляров"""
        angel1 = CreatureFactory.create_creature("Полет ангела")
        angel2 = CreatureFactory.create_creature("Полет ангела")
        demon1 = CreatureFactory.create_creature("Полет демона")
        demon2 = CreatureFactory.create_creature("Полет демона")

        # Проверка, что объекты разных типов
        assert type(angel1) == type(angel2)
        assert type(demon1) == type(demon2)
        assert type(angel1) != type(demon1)

        # Проверка поведения каждого объекта
        assert angel1.rocket() == "Плавный взлет"
        assert demon1.rocket() == "Резкий взлет"

# Тест документации и строк
class TestStringRepresentations:
    def test_abstract_method_name(self):
        """Проверка имени абстрактного метода"""
        assert "rocket" in Creature.__abstractmethods__