class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty.")
            return None

    def display(self):
        """Display all elements in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(self.items):
                print(item)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()      # Should display 30, 20, 10

stack.pop()          # Should remove 30
stack.display()      # Should display 20, 10


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


r = float(input("Enter radius: "))
c = Circle(r)
    
class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def get_age(self, current_year):
        return current_year - self.birth_year


name = input("Enter name: ")
country = input("Enter country: ")
birth_year = int(input("Enter birth year: "))
current_year = 2025  # You can change this if needed

person = Person(name, country, birth_year)

print("Name:", person.name)
print("Country:", person.country)
print("Age:", person.get_age(current_year))

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero"


calc = Calculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.subtract(a, b))
print("Multiplication:", calc.multiply(a, b))
print("Division:", calc.divide(a, b))
import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c, height=None):
        self.a = a
        self.b = b
        self.c = c
        self.height = height  # Needed for area if using base-height formula

    def area(self):
        # If height is provided, use base*height/2
        if self.height:
            return 0.5 * self.a * self.height
        # Else use Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# Example usage
circle = Circle(5)
print("Circle - Area:", circle.area(), "Perimeter:", circle.perimeter())

square = Square(4)
print("Square - Area:", square.area(), "Perimeter:", square.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle - Area:", triangle.area(), "Perimeter:", triangle.perimeter())

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # If value == current.value, we do nothing (no duplicates)

    def search(self, value):
        """Search for a value in the BST. Returns True if found, else False."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

# Example usage
bst = BinarySearchTree()
n

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        """Return the number of items in the stack."""
        return len(s

# Node class represents each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class manages the list
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delet

class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their prices

    def add_item(self, item_name, price):
        """Add an item with its price to the cart."""
        self.items[item_name] = price
        print(f"{item_name} added to cart.")

    def remove_item(self, item_name):
        """Remove an item from the cart."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from cart.")
        else:
            print(f"{item_name} not found in cart.")

    def calculate_total(self):
        """Calculate the total price of all items in the cart."""
        return sum(self.items.values())

    def display_cart(self):
        """Display all items in the cart."""
        if not self.items:
            print("Cart is empty.")
        else:
            print("Items in cart:")
            for item, price in self.items.items():
                print(f"- {item}: ${price:.2f}")
            print(f"Total: ${self.calculate_total():.2f}")

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 0.99)
cart.add_item("Bread", 2.50)
cart.add_item("Milk", 1.75)

cart.display_cart()

cart.remove_item("Bread")
cart.display_cart()

