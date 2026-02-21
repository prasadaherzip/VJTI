# ================= NODE CLASSES =================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ================= ARRAY FUNCTIONS =================

def array_insert(arr, pos, val, comps, shifts):
    comps += 2
    if pos < 0 or pos > len(arr):
        print("Invalid position")
        return arr, comps, shifts

    arr.append(0)
    for i in range(len(arr) - 1, pos, -1):
        arr[i] = arr[i - 1]
        shifts += 1

    arr[pos] = val
    return arr, comps, shifts


 array_search(arr, key, comps):
    for i in range(len(arr)):
        comps += 1
        if arr[i] == key:
            print("Match found at position", i + 1)
            return i, comps
    print("Match not found")
    return -1, comps


def array_update(arr, pos, val, comps):
    comps += 2
    if pos < 0 or pos >= len(arr):
        print("Invalid position")
        return arr, comps
    arr[pos] = val
    return arr, comps


def array_delete(arr, pos, comps, shifts):
    comps += 2
    if pos < 0 or pos >= len(arr):
        print("Invalid position")
        return arr, comps, shifts

    for i in range(pos, len(arr) - 1):
        arr[i] = arr[i + 1]
        shifts += 1

    arr.pop()
    return arr, comps, shifts


def array_reverse(arr, shifts):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        shifts += 2
        i += 1
        j -= 1
    return arr, shifts


# ================= SLL FUNCTIONS =================

def sll_create(n):
    head = None
    tail = None
    for _ in range(n):
        val = int(input("Enter value: "))
        new_node = Node(val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


def sll_insert(head, val, pos, comps):
    new_node = Node(val)

    if pos == 0:
        new_node.next = head
        return new_node, comps

    temp = head
    curr = 0

    while temp and curr < pos - 1:
        comps += 1
        temp = temp.next
        curr += 1

    if temp is None:
        print("Invalid position")
        return head, comps

    new_node.next = temp.next
    temp.next = new_node
    return head, comps


def sll_search(head, key, comps):
    temp = head
    pos = 0
    while temp:
        comps += 1
        if temp.data == key:
            print("Match found at position", pos + 1)
            return pos, comps
        temp = temp.next
        pos += 1
    print("Match not found")
    return -1, comps


def sll_update(head, pos, val, comps):
    temp = head
    curr = 0
    while temp and curr < pos:
        comps += 1
        temp = temp.next
        curr += 1

    if temp is None:
        print("Invalid position")
        return head, comps

    temp.data = val
    return head, comps


def sll_delete(head, pos, comps):
    if head is None:
        return None, comps

    if pos == 0:
        return head.next, comps

    temp = head
    curr = 0

    while temp.next and curr < pos - 1:
        comps += 1
        temp = temp.next
        curr += 1

    if temp.next is None:
        print("Invalid position")
        return head, comps

    temp.next = temp.next.next
    return head, comps


def sll_reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def sll_print(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


# ================= DLL FUNCTIONS =================

def dll_create(n):
    head = None
    tail = None
    for _ in range(n):
        val = int(input("Enter value: "))
        new_node = DNode(val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            new_node.prev = tail
            tail = new_node
    return head


def dll_insert(head, val, pos, comps):
    new_node = DNode(val)

    if pos == 0:
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node, comps

    temp = head
    curr = 0

    while temp and curr < pos - 1:
        comps += 1
        temp = temp.next
        curr += 1

    if temp is None:
        print("Invalid position")
        return head, comps

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next:
        temp.next.prev = new_node

    temp.next = new_node
    return head, comps


def dll_search(head, key, comps):
    temp = head
    pos = 0
    while temp:
        comps += 1
        if temp.data == key:
            print("Match found at position", pos + 1)
            return pos, comps
        temp = temp.next
        pos += 1
    print("Match not found")
    return -1, comps


def dll_update(head, pos, val, comps):
    temp = head
    curr = 0
    while temp and curr < pos:
        comps += 1
        temp = temp.next
        curr += 1

    if temp is None:
        print("Invalid position")
        return head, comps

    temp.data = val
    return head, comps


def dll_delete(head, pos, comps):
    if head is None:
        return None, comps

    if pos == 0:
        head = head.next
        if head:
            head.prev = None
        return head, comps

    temp = head
    curr = 0

    while temp and curr < pos:
        comps += 1
        temp = temp.next
        curr += 1

    if temp is None:
        print("Invalid position")
        return head, comps

    if temp.next:
        temp.next.prev = temp.prev

    if temp.prev:
        temp.prev.next = temp.next

    return head, comps


def dll_reverse(head):
    temp = None
    curr = head

    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev

    if temp:
        head = temp.prev

    return head


def dll_print(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")


# ================= MAIN PROGRAM =================

arr = []
sll_head = None
dll_head = None
comps = 0
shifts = 0

while True:
    print("\nSELECT DATA STRUCTURE")
    print("1. Array")
    print("2. Singly Linked List")
    print("3. Doubly Linked List")
    print("4. Exit")

    ds_choice = int(input("Enter choice: "))

    if ds_choice == 4:
        break

    print("\n1.Create 2.Insert 3.Search 4.Update 5.Delete 6.Reverse 7.Display")
    op = int(input("Enter operation: "))

    # ARRAY
    if ds_choice == 1:
        if op == 1:
            n = int(input("Enter size: "))
            arr = [int(input("Enter element: ")) for _ in range(n)]
            comps = shifts = 0
        elif op == 2:
            val = int(input("Enter value: "))
            pos = int(input("Enter position (1-based): ")) - 1
            arr, comps, shifts = array_insert(arr, pos, val, comps, shifts)
        elif op == 3:
            key = int(input("Enter value: "))
            _, comps = array_search(arr, key, comps)
        elif op == 4:
            pos = int(input("Enter position (1-based): ")) - 1
            val = int(input("Enter new value: "))
            arr, comps = array_update(arr, pos, val, comps)
        elif op == 5:
            pos = int(input("Enter position (1-based): ")) - 1
            arr, comps, shifts = array_delete(arr, pos, comps, shifts)
        elif op == 6:
            arr, shifts = array_reverse(arr, shifts)
        elif op == 7:
            print("Array:", arr)
            print("Comparisons:", comps)
            print("Shifts:", shifts)

    # SLL
    elif ds_choice == 2:
        if op == 1:
            n = int(input("Enter size: "))
            sll_head = sll_create(n)
            comps = 0
        elif op == 2:
            val = int(input("Enter value: "))
            pos = int(input("Enter position (1-based): ")) - 1
            sll_head, comps = sll_insert(sll_head, val, pos, comps)
        elif op == 3:
            key = int(input("Enter value: "))
            _, comps = sll_search(sll_head, key, comps)
        elif op == 4:
            pos = int(input("Enter position (1-based): ")) - 1
            val = int(input("Enter new value: "))
            sll_head, comps = sll_update(sll_head, pos, val, comps)
        elif op == 5:
            pos = int(input("Enter position (1-based): ")) - 1
            sll_head, comps = sll_delete(sll_head, pos, comps)
        elif op == 6:
            sll_head = sll_reverse(sll_head)
        elif op == 7:
            sll_print(sll_head)
            print("Comparisons:", comps)

    # DLL
    elif ds_choice == 3:
        if op == 1:
            n = int(input("Enter size: "))
            dll_head = dll_create(n)
            comps = 0
        elif op == 2:
            val = int(input("Enter value: "))
            pos = int(input("Enter position (1-based): ")) - 1
            dll_head, comps = dll_insert(dll_head, val, pos, comps)
        elif op == 3:
            key = int(input("Enter value: "))
            _, comps = dll_search(dll_head, key, comps)
        elif op == 4:
            pos = int(input("Enter position (1-based): ")) - 1
            val = int(input("Enter new value: "))
            dll_head, comps = dll_update(dll_head, pos, val, comps)
        elif op == 5:
            pos = int(input("Enter position (1-based): ")) - 1
            dll_head, comps = dll_delete(dll_head, pos, comps)
        elif op == 6:
            dll_head = dll_reverse(dll_head)
        elif op == 7:
            dll_print(dll_head)
            print("Comparisons:", comps)