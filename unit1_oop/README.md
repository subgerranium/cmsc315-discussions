# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation

I implemented `ParentClass` as a generic vehicle representation with a class variable, `wheels`, set to 4, along with two instance variables, `make` and `model`, initialized through the constructor. I added a `display_info()` method to print an object's details.

I then created `ChildClass` (representing a `Car`) to inherit from `ParentClass`. I called `super().__init__()` inside its constructor to reuse the parent's initialization logic instead of duplicating it, and added a new class variable, `category`, along with two new instance variables, `year` and a mutable `features` list. I overrode `display_info()` to include the additional car-specific fields and added a new `add_feature()` method to append items to a car's feature list.

For the namespace demonstration, I created two `Car` objects and accessed the `category` class variable through both the class and an instance to show they resolved to the same value. I then added a `color` attribute to only one of the two objects and printed each object's `__dict__` to confirm their instance namespaces remained independent of one another.

For the copying demonstration, I created a `Car` object with a populated `features` list, then created both a shallow copy and a deep copy of it. After modifying the original object's `features` list, I printed all three objects to show that the shallow copy reflected the change (since it shared the same underlying list as the original), while the deep copy retained its own independent list and was unaffected.

For my student-created extension, I added a class-level counter, `total_cars_created`, that incremented each time a `Car` object was instantiated, along with a `show_total_created()` classmethod to report the running total. This extension reinforced the namespace concepts covered earlier in the assignment, since the counter is stored on the class itself rather than on any individual object.

I tested all functionality by running the script directly and confirming the printed output matched expected behavior for inheritance, namespace resolution, and copy semantics.