# ================= STACK CLASS =================
class Stack:
    def __init__(self):
        self.stack = []
        self.comps = 0
        self.shifts = 0

    def insert(self, value):
        self.stack.append(value)
        self.shifts += 1

    def search(self, value):
        for item in self.stack:
            self.comps += 1
            if item == value:
                return True
        return False

    def delete(self):
        if len(self.stack) == 0:
            return None
        self.shifts += 1
        return self.stack.pop()

    def update(self, pos, value):
        if 0 <= pos < len(self.stack):
            self.comps += 1
            self.stack[pos] = value
            return True
        return False

    def display(self):
        print("Stack:", self.stack)
        print("Comparisons:", self.comps)
        print("Shifts:", self.shifts)


# ================= QUEUE CLASS =================
class Queue:
    def __init__(self):
        self.queue = []
        self.comps = 0
        self.shifts = 0

    def insert(self, value):
        self.queue.append(value)
        self.shifts += 1

    def search(self, value):
        for item in self.queue:
            self.comps += 1
            if item == value:
                return True
        return False

    def delete(self):
        if len(self.queue) == 0:
            return None
        self.shifts += len(self.queue) - 1
        return self.queue.pop(0)

    def update(self, pos, value):
        if 0 <= pos < len(self.queue):
            self.comps += 1
            self.queue[pos] = value
            return True
        return False

    def display(self):
        print("Queue:", self.queue)
        print("Comparisons:", self.comps)
        print("Shifts:", self.shifts)


# ================= PROGRAM START =================

print("Select Data Structure")
print("1. Stack")
print("2. Queue")

ds_choice = int(input("Enter choice: "))

if ds_choice == 1:
    ds = Stack()
    print("Working on Stack")
elif ds_choice == 2:
    ds = Queue()
    print("Working on Queue")
else:
    print("Invalid choice")
    exit()


# ===== Operation Loop =====
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Update")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        ds.insert(value)

    elif choice == 2:
        value = int(input("Enter value to search: "))
        print("Found" if ds.search(value) else "Not Found")

    elif choice == 3:
        result = ds.delete()
        if result is None:
            print("Structure is empty")
        else:
            print("Deleted:", result)

    elif choice == 4:
        pos = int(input("Enter pos (0-based): "))
        value = int(input("Enter new value: "))
        if ds.update(pos, value):
            print("Updated successfully")
        else:
            print("Invalid pos")

    elif choice == 5:
        ds.display()

    elif choice == 6:
        break

    else:
        print("Invalid choice")