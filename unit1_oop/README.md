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

For this assignment, I made a vehicle system using a ParentClass (representing a generic vehicle) and a ChildClass called 
Car that inherits. The ParentClass defines a class variable called "wheels", set to 4 because every car in this model shares 
that common trait as well as two instance variables, "make" and "model", which are initialized in the constructor. The 
display_info() method prints those details. ChildClass extends the ParentClass using inheritance by calling super().__init__()
to reuse the parent's constructor logic instead of duplicating it. It adds its own class variable of "category" which is set 
to "Passenger", as well as two new instance variables, "year" and a mutable "features" list. I overrode display_info() so Cars 
print their additional details along with the inherited ones, and added add_feature() to append to a car's feature list. 
This was used to build out cars like the Dodge Ram with a tow package. For the student-created extension, I added a class-level
counter of "total_cars_created" that increments every time a Car object is made, along with a show_total_created() method to 
output it. This ties directly into the namespace concepts covered in the assignment because the counter is stored on the class
and not on an individual car. This makes it a good example of shared class level state vs per object instance state.