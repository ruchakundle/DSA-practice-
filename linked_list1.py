class Node:
    def __init__(self, data):
        self.info = data
        self.link = None

class Linkedlist:
    def __init__(self):
        self.start = None

    def traversal(self):
        p = self.start
        while p is not None:
            print(p.info, end=" -> ")
            p = p.link
        print("None\n")

    def count(self):
        i = 0
        p = self.start
        while p is not None:
            i += 1
            p = p.link
        print("The total nodes are:", i)

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(f"The element {x} is found at position {position}")
                return
            p = p.link
            position += 1
        print(f"The element {x} is not found.")

    def InAtStart(self, data):
        # Always works, even when list is empty
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def InAtEnd(self, data):
        temp = Node(data)
        if self.start is None:
            # Case: List is empty
            self.start = temp
            return
        # Case: Normal case, insert after last node
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def AtSecLast(self, data):
        temp = Node(data)
        if self.start is None or self.start.link is None:
            # Case: List has 0 or 1 node → insert at start
            temp.link = self.start
            self.start = temp
            return
        # Case: Normal case → insert before last node
        p = self.start
        while p.link.link is not None:
            p = p.link
        temp.link = p.link
        p.link = temp

    def precedingToValue(self, data, y):
        temp = Node(data)
        if self.start is None:
            # Case: List is empty
            print("List is empty.")
            return
        if self.start.info == y:
            # Case: Target value is at the first node
            temp.link = self.start
            self.start = temp
            return
        # Case: Normal case → insert before matching node
        p = self.start
        while p.link is not None:
            if p.link.info == y:
                temp.link = p.link
                p.link = temp
                return
            p = p.link
        print(f"Value {y} not found in the list.")

    def AfterAValue(self, data, y):
        temp = Node(data)
        if self.start is None:
            # Case: List is empty
            print("List is empty. Cannot insert after a value.")
            return
        # Case: Normal case → insert after matching node
        p = self.start
        while p is not None:
            if p.info == y:
                temp.link = p.link
                p.link = temp
                return
            p = p.link
        print(f"Value {y} not found in the list.")

    def create_list(self):
        n = int(input("Enter number of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter data to insert: "))
            self.InAtEnd(data)

# 🚀 MAIN
list = Linkedlist()
list.create_list()
list.traversal()

print("MENU:")
print("1. Insert at the beginning")
print("2. Insert at the end")
print("3. Insert at second last position")
print("4. Insert before a given value")
print("5. Insert after a given value")
print("6. Count total nodes")
print("7. Search an element")

choice = int(input("Choose option: "))

if choice == 1:
    data = int(input("Enter value to insert at start: "))
    list.InAtStart(data)
    list.traversal()

elif choice == 2:
    data = int(input("Enter value to insert at end: "))
    list.InAtEnd(data)
    list.traversal()

elif choice == 3:
    data = int(input("Enter value to insert at second last position: "))
    list.AtSecLast(data)
    list.traversal()

elif choice == 4:
    y = int(input("Enter the value already in the list (to insert before): "))
    data = int(input("Enter value to insert: "))
    list.precedingToValue(data, y)
    list.traversal()

elif choice == 5:
    y = int(input("Enter the value already in the list (to insert after): "))
    data = int(input("Enter value to insert: "))
    list.AfterAValue(data, y)
    list.traversal()

elif choice == 6:
    list.count()

elif choice == 7:
    x = int(input("Enter value to search: "))
    list.search(x)

else:
    print("Invalid choice.")
