## Day 20 – Class Design

### Topics Covered
- Class Attributes vs Instance Attributes
- `@classmethod`
- `@staticmethod`
- `@property`
- Encapsulation using underscore naming
- Controlled Access to Attributes

### Assignments

**1. employee.py – Employee Counter**
- Created an `Employee` class.
- Used a class attribute to maintain the total number of employees.
- Counted employees created using multiple objects.

**2. temperature_class.py – Temperature Class**
- Created a `Temperature` class.
- Used `@property` to control access to temperature values.
- Prevented temperature values below absolute zero.
- Used property setters for validation.

**3. date_parser.py – Date Parser**
- Created a date class.
- Used `@classmethod` to create objects from date strings.
- Supported the `DD-MM-YYYY` date format.

### Stretch Task
- Implemented a `@staticmethod` to validate date string format.
- Separated date validation logic from object creation.

### Concepts Practiced
- Python Class Design
- Class and Instance Attributes
- Class Methods
- Static Methods
- Property Decorators
- Encapsulation
- Data Validation
- Object Creation

### Folder Structure

```text
day-20/
│
├── employee.py
├── temperature_class.py
└── date_parser.py
```

**Status:** Completed