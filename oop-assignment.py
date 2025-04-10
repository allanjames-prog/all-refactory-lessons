# Base class: Creature
class Creature:
    def __init__(self, name, species, power_level, speed, habitat, special_ability, weakness):
        """Initialize the attributes of a generic creature."""
        self.name = name
        self.species = species
        # Strength level of the creature
        self.power_level = power_level  
        # Speed rating
        self.speed = speed  
        # Natural environment
        self.habitat = habitat  
        # Unique power
        self.special_ability = special_ability  
        # Specific vulnerability
        self.weakness = weakness  

    def describe(self):
        """Prints out the details of the creature."""
        print(f"Creature: {self.name}")
        print(f"Species: {self.species}")
        print(f"Power Level: {self.power_level}")
        print(f"Speed: {self.speed}")
        print(f"Habitat: {self.habitat}")
        print(f"Special Ability: {self.special_ability}")
        print(f"Weakness: {self.weakness}")
        print("-" * 30)

    def use_ability(self):
        """Simulates the use of the creature's special ability."""
        print(f"{self.name} uses {self.special_ability}!")


# Subclass for Dragon
class Dragon(Creature):
    def __init__(self, name, power_level, speed):
        """Initialize a Dragon with predefined species, habitat, ability, and weakness."""
        super().__init__(name, "Dragon", power_level, speed, "Mountains", "Fire Breath", "Cold")
    
    def fly(self):
        """Simulates the dragon flying."""
        print(f"{self.name} spreads its wings and takes off into the sky!")


# Subclass for Elf
class Elf(Creature):
    def __init__(self, name, power_level, speed):
        """Initialize an Elf with predefined species, habitat, ability, and weakness."""
        super().__init__(name, "Elf", power_level, speed, "Forests", "Archery Mastery", "Dark Magic")
    
    def stealth(self):
        """Simulates the elf becoming invisible."""
        print(f"{self.name} blends into the shadows, becoming nearly invisible.")


# Subclass for Mermaid
class Mermaid(Creature):
    def __init__(self, name, power_level, speed):
        """Initialize a Mermaid with predefined species, habitat, ability, and weakness."""
        super().__init__(name, "Mermaid", power_level, speed, "Ocean", "Siren Song", "Drought")
    
    def swim(self):
        """Simulates the mermaid swimming gracefully."""
        print(f"{self.name} glides effortlessly through the waves.")


# Subclass for Golem
class Golem(Creature):
    def __init__(self, name, power_level, speed):
        """Initialize a Golem with predefined species, habitat, ability, and weakness."""
        super().__init__(name, "Golem", power_level, speed, "Caves", "Stone Armor", "Water")
    
    def smash(self):
        """Simulates the golem smashing the ground."""
        print(f"{self.name} slams the ground, causing a small earthquake!")


# Create instances of each subclass
drake = Dragon("Drake", 90, 60)
legolas = Elf("Legolas", 80, 100)
ariel = Mermaid("Ariel", 70, 80)
rocky = Golem("Rocky", 95, 30)

# Call methods for each creature to demonstrate functionality
drake.describe()
drake.use_ability()
drake.fly()

legolas.describe()
legolas.use_ability()
legolas.stealth()

ariel.describe()
ariel.use_ability()
ariel.swim()

rocky.describe()
rocky.use_ability()
rocky.smash()
