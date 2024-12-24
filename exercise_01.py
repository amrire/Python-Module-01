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
        

def zombie_horde(N: int, name: str) -> list[Zombie]:
    """
    Create a horde of N zombies with the same name.
    :param N: The number of zombies in the horde.
    :param name: The base name for all zombies.
    :return: A list of Zombie instances.
    """
    return [Zombie(f"{name}_{i+1}") for i in range(N)]


if __name__ == "__main__":
    print("\nCreating a horde of zombies...")
    horde = zombie_horde(5, "Zombie")
    print("\nAnnouncing the horde...")
    for zombie in horde:
        zombie.announce()
    print("\nEnd of program.")
  