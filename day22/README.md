## Day 22 – Special Methods and Dataclasses

### Topics Covered
- Special Methods (Dunder Methods)
- `__str__()` and `__repr__()`
- `__eq__()` for comparing objects
- `__lt__()` for object comparison
- `__len__()` for measuring object length
- Operator Overloading
- `@dataclass` Decorator

### Assignments

**1. student_class.py – Student Special Methods**
- Updated the Student class.
- Implemented `__str__()` for readable object representation.
- Implemented `__repr__()` for developer-friendly object representation.

**2. money.py – Money Class**
- Created a `Money` class.
- Implemented `__add__()` to support addition using the `+` operator.
- Implemented `__eq__()` to compare Money objects using `==`.

**3. playlist.py – Playlist Class**
- Created a `Playlist` class.
- Implemented `__len__()` to return the number of songs.
- Enabled the use of `len(playlist)`.

**4. rectangle.py – Dataclass**
- Rewrote the Rectangle class using `@dataclass`.
- Used dataclass features to simplify class implementation.

### Stretch Task
- Implemented `__lt__()` in the Student class.
- Enabled sorting of Student objects based on average marks.

### Concepts Practiced
- Python Special Methods
- Dunder Methods
- Operator Overloading
- Object Comparison
- Object Representation
- Custom Length Implementation
- Dataclasses
- Object Sorting

### Folder Structure

```text
day-22/
│
├── student_class.py
├── money.py
├── playlist.py
└── rectangle.py
```

**Status:** Completed