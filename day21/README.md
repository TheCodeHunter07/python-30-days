## Day 21 – Inheritance

### Topics Covered
- Parent and Child Classes
- Inheritance in Python
- Method Overriding
- `super()` Function
- Composition
- Polymorphism

### Assignments

**1. vehicles.py – Vehicle Inheritance**
- Created a `Vehicle` base class.
- Created `Car` and `Bike` subclasses.
- Used inheritance to reuse parent class attributes and methods.
- Overrode the `describe()` method in child classes.

**2. people.py – Person Inheritance**
- Created a `Person` base class.
- Created `Student` and `Teacher` subclasses.
- Used `super().__init__()` to initialize parent class attributes.
- Added additional attributes specific to each subclass.

**3. shapes.py – Shape Inheritance**
- Created a `Shape` base class.
- Created `Circle`, `Square`, and `Triangle` subclasses.
- Implemented the `area()` method in each subclass.
- Used method overriding to calculate areas differently.

### Stretch Task – Polymorphism
- Created a list containing different shape objects.
- Used a loop to iterate through the objects.
- Called the same `area()` method on different objects.
- Demonstrated polymorphism through a common method interface.

### Concepts Practiced
- Code Reusability
- Parent and Child Classes
- Inheritance
- Method Overriding
- Constructor Inheritance
- `super()` Function
- Composition
- Polymorphism
- Object-Oriented Programming

### Folder Structure

```text
day-21/
│
├── vehicles.py
├── people.py
└── shapes.py
```

**Status:** Completed