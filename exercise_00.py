#!/usr/bin/python3


class Zombie:
    def __init__(self, name: str):
        """
        Initialize a Zombie with a name.
        :param name: The name of the zombie.
        """
        self.__name = name
        print(f"Zombie {self.__name} is created")
        
    def announce(self):
        """
        Announce the zombie's presence.
        """
        print(f"Zombie {self.__name}: BraaiinnzzZ...")

    def __del__(self):
        """
        Destructor that is called when the Zombie object is destroyed.
        """
        print(f"Zombie {self.__name} has been destroyed.")

    
def new_zombie(name: str) -> Zombie:
    """
    Create a new zombie and return it.
    :param name: The name of the zombie.
    :return: A Zombie instance.
    """
    return Zombie(name)


def new_zombie_chump(name: str):
    """
    Create a zombie and announce it immediately.
    :param name: The name of the zombie.
    """
    zombie = Zombie(name)
    zombie.announce()


if __name__ == "__main__":
    print("\nCreating a zombie 'Alice' using new_zombie...")
    z1 = new_zombie("Alice")
    z1.announce()
    print("\nCreating a zombie 'Bob' using new_zombie_chump...")
    new_zombie_chump("Bob")
    print("\nEnd of program.")