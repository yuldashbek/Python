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
