#!/usr/bin/python3


class Weapon:
    def __init__(self, type_):
        """
        Initialize a Weapon with a type.
        :param type_: The type of the weapon.
        """
        self._type = type_
        
    def get_type(self):
        """
        Get the type of the weapon.
        :return: The type of the weapon.
        """
        return self._type
    
    def set_type(self, type_):
        """
        Set a new type for the weapon.
        :param type_: The new type of the weapon.
        """
        self._type = type_
        

class HumanA:
    def __init__(self, name: str, weapon: Weapon):
        """
        Initialize a HumanA with a name and a weapon.
        :param name: The name of the human.
        :param weapon: The weapon the human wields.
        """
        self.name = name
        self.weapon = weapon
        
    def attack(self):
        """
        Display the attack message using the weapon.
        """
        print(f"{self.name} attacks with a {self.weapon.get_type()}.")
        

class HumanB:
    def __init__(self, name: str):
        """
        Initialize a HumanB with a name and no weapon initially.
        :param name: The name of the human.
        """
        self.name = name
        self.weapon = None
        
    def set_weapon(self, weapon: Weapon):
        """
        Assign a weapon to the human.
        :param weapon: The weapon to assign.
        """
        self.weapon = weapon
        
    def attack(self):
        """
        Display the attack message if the human has a weapon.
        Otherwise, indicate they are unarmed.
        """
        if self.weapon:
            print(f"{self.name} attacks with a {self.weapon.get_type()}.")
        else:
            print(f"{self.name} attacks with bare hands.")


if __name__ == '__main__':
    print("\nCreating a weapon and assigning it to HumanA and HumanB...\n")
    sword = Weapon("Sword")
    human_a = HumanA("Alice", sword)
    human_a.attack()
    human_b = HumanB("Bob")
    human_b.attack()
    human_b.set_weapon(Weapon("Axe"))
    human_b.attack()
    print("\nEnd of program.")  