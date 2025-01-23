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
    ```python
    import pygame
    import random
    
    # Parent class: GameObject
    class GameObject(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface((width, height))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, 500)
            self.rect.y = random.randint(0, 400)
    
        def move(self, x_change, y_change):
            self.rect.x += x_change
            self.rect.y += y_change
    
    # Child class: Player
    class Player(GameObject):
        def __init__(self, color, width, height):
            super().__init__(color, width, height)
            self.speed = 5  # Additional attribute for the Player class
    
        def handle_keys(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.move(0, -self.speed)
            if keys[pygame.K_DOWN]:
                self.move(0, self.speed)
            if keys[pygame.K_LEFT]:
                self.move(-self.speed, 0)
            if keys[pygame.K_RIGHT]:
                self.move(self.speed, 0)
    
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Single Inheritance Example")
    clock = pygame.time.Clock()
    
    # Create a player object
    player = Player((255, 0, 0), 50, 50)
    all_sprites = pygame.sprite.Group(player)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill((0, 0, 0))
        player.handle_keys()  # Player-specific behavior
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
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

4. **Hierarchical Inheritance**: Multiple child classes inherit from the same parent class.
    ```python
    class Parent:
        pass

    class Child1(Parent):
        pass

    class Child2(Parent):
        pass
    ```

5. **Hybrid Inheritance**: A combination of multiple types of inheritance.
    ```python
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
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

Let me know if you'd like deeper examples or clarification on any part!
