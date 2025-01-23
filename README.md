# Pygame: InheritanceDemo

Inheritance in Python is a fundamental concept in object-oriented programming (OOP) that allows one class (called a **child class** or **subclass**) to inherit the attributes and methods of another class (called a **parent class** or **superclass**). This allows for code reuse, better organization, and the creation of hierarchical relationships between classes.

### **Why Use Inheritance?**
- **Code Reusability**: Avoid duplicating code in multiple classes.
- **Extensibility**: Easily add new features or modify behavior in derived classes.
- **Hierarchy Representation**: Model real-world relationships (e.g., `Animal -> Dog -> Labrador`).

---

### **Basic Syntax**
```python
class ParentClass:
    # Parent class with some attributes and methods
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."

# Child class inherits from ParentClass
class ChildClass(ParentClass):
    # Constructor of the child class
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent class constructor
        self.age = age  # Add new attributes specific to the child class

    def introduce(self):
        return f"{self.greet()} I am {self.age} years old."
    
# Example usage
child = ChildClass("Alice", 25)
print(child.greet())        # Method from ParentClass
print(child.introduce())    # Method from ChildClass
```

**Output:**
```
Hello, my name is Alice.
Hello, my name is Alice. I am 25 years old.
```

---

### **Key Concepts**

#### 1. **Parent Class**
A parent class is the base class that provides attributes and methods to other classes.

#### 2. **Child Class**
A child class inherits from a parent class. It can:
- Use the parent class's methods and attributes.
- Override the parent class's methods to provide specialized behavior.
- Add its own methods and attributes.

#### 3. **`super()` Keyword**
The `super()` function is used to call methods from the parent class. It’s commonly used to initialize attributes in the parent class's constructor.

#### 4. **Overriding Methods**
A child class can redefine methods of the parent class to customize behavior.

Example:
```python
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark!"

dog = Dog()
print(dog.sound())  # Output: Bark!
```

---

### **Types of Inheritance**

1. **Single Inheritance**: A child class inherits from one parent class.
    ```python
    class Parent:
        pass

    class Child(Parent):
        pass
    ```
   

2. **Multiple Inheritance**: A child class inherits from more than one parent class.
    ```python
    class Parent1:
        pass

    class Parent2:
        pass

    class Child(Parent1, Parent2):
        pass
    ```

3. **Multilevel Inheritance**: A child class inherits from a parent class, and another child class inherits from it.
    ```python
    class Grandparent:
        pass

    class Parent(Grandparent):
        pass

    class Child(Parent):
        pass
    ```
---

### **Example with Overriding and `super()`**
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call the parent constructor
        self.model = model

    def info(self):
        # Override the parent method and extend its functionality
        return f"{super().info()}, Model: {self.model}"

car = Car("Toyota", "Corolla")
print(car.info())  # Output: Brand: Toyota, Model: Corolla
```

---

### **Key Advantages**
- **Modularity**: Breaks code into reusable chunks.
- **Scalability**: Easily extend functionality.
- **Maintenance**: Changes in the parent class automatically reflect in child classes.

### **Points to Remember**
- If the child class doesn't override a method, it uses the one from the parent class.
- Use `super()` to refer to the parent class's methods.
- Avoid excessive use of inheritance; sometimes, **composition** (has-a relationship) is a better choice than inheritance (is-a relationship).
