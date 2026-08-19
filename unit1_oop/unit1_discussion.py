"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # This is a class variable, it is shared by every object unless an instance overrides it.
    # Since every car will have 4 wheels, we will store it once instead of repeating it on every object.
    wheels = 4

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Wheels: {self.wheels}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # This is a new class variable that is specific to the Car but not in the parent.
    category = "Passenger"

    total_cars_made = 0

    def __init__(self, make: str, model: str, year: int):
        # Reuse our parent constructor to reuse the make/model.
        super().__init__(make, model)

        self.year = year

        self.features = []

        # Increment total cars every time a Car is made.
        ChildClass.total_cars_made += 1

    def add_features(self, feature: str):
        # New method not in parent class.
        self.features.append(feature)

    def display_info(self):
        # Override of parent class
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Wheels: {self.wheels}, "
        f"Category: {self.category}, Features: {self.features}")

    @classmethod
    def show_total_cars_made(cls):
        # Shows total Cars made so far.
        print(f"Total cars made: {cls.total_cars_made}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    car1 = ChildClass("Hyundai", "Santa Fe", "2019")
    car2 = ChildClass("Ford", "F150", "2008")

    # Access a class variable through the class itself.
    print(f"Accessed through class: ChildClass.category = {ChildClass.category}")

    # Access the same class variable through an object.
    print(f"Accessed through instance: car1.category = {car1.category}")

    # Add a new attribute to only one object after it is created.
    car1.color = "Black"

    #Display each object's namespace using __dict__.
    print(f"\ncar1.__dict__ = {car1.__dict__}")
    print(f"car2.__dict__ = {car2.__dict__}")

    # Display information about the class namespace.
    print(f"\nChildClass.__dict__ (class namespace, partial view):")
    print(f"category - {ChildClass.__dict__.get('category')}")
    print(f"wheels (inherited, not in ChildClass's own __dict__) - "
          f"{'wheels' in ChildClass.__dict__}")

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    # Create an object that contains nested mutable data.
    original = ChildClass("Hyundai", "Santa Fe", "2019")
    original.add_features("Sunroof")
    original.add_features("Heated Seats")

    # Create a shallow copy.
    shallow = copy(original)

    # Create a deep copy.
    deep = deepcopy(original)

    # Modify the original object's nested data.
    original.add_features("Leather Seats")

    # Display the original object, shallow copy, and deep copy.
    print(f"Original features: {original.features}")
    print(f"Shallow copy features: {shallow.features}")
    print(f"Deep copy features: {deep.features}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    parent_obj = ParentClass("Generic", "Car")
    parent_obj.display_info()

    print("\nTODO: Create and test your child object")
    child_obj = ChildClass("Dodge", "Ram", "2020")
    child_obj.add_features("Tow")
    child_obj.display_info()

    # Call your namespace demonstration function.
    demonstrate_namespaces()

    # Call your copy demonstration function.
    demonstrate_copying()

    # Final count after the demo creates more Cars.
    ChildClass.show_total_cars_made()


if __name__ == "__main__":
    main()