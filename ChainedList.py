class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, name, number):
        new_node = Node(name, number)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current:
            if name < current.name:
                if current.prev:
                    current.prev.next = new_node
                    new_node.prev = current.prev
                    new_node.next = current
                    current.prev = new_node
                else:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                return
            elif current.next is None:
                current.next = new_node
                new_node.prev = current
                return
            current = current.next

    def delete(self, name):
        current = self.head

        # Sucht nach dem angegebenen Namen
        while current:
            if current.name == name:
                # Wenn der Node existiert
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
            # Wenn der Node nicht existiert
        print(f"Ein Rekord mit dem Namen '{name}' nicht gefunden.")

    def print_list_asc(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Number: {current.number}")
            current = current.next

    def print_list_desc(self):
        #current = self.head
        current = self.tail
        # Bewegt sich über die Liste bis zum letzten Element:
        while current and current.next:
            current = current.next
        # Startet die Ausgabe von dem letzten Element und iteriert nach hinten bis zum ersten:
        while current:
            print(f"Name: {current.name}, Number: {current.number}")
            current = current.prev


# 1.
dll1 = DoublyLinkedList()
print("1.")
dll1.insert("John", 2137)
dll1.insert("Anna", 1928)
print("Aufsteigend:")
dll1.print_list_asc()
print("Absteigend:")
dll1.print_list_desc()

# 2.
dll2 = DoublyLinkedList()
print("2.")
dll2.insert("John", 2137)
dll2.insert("Kixi", 69)
print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 3.
print("3.")
dll2.insert("Steffi", 72632)
dll2.insert("Anna", 1928)
dll2.insert("Mati", 2330)

dll2.insert("Zenobius", 381)

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 4.
print("4.")
dll2.insert("Aaron", 878)

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 5.
print("5.")
dll2.insert("Zarathustra", 23832)

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 6.
print("6.")
dll2.insert("Abby", 2832)

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 7.
print("7.")
dll2.insert("Aceina", 2464)

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 8.
print("8.")
dll3 = DoublyLinkedList()
dll3.insert("Dorothy", 1327)
dll3.delete("Dorothy")

print("Aufsteigend:")
dll3.print_list_asc()
print("Absteigend:")
dll3.print_list_desc()

# 9.
print("9.")
dll1.delete("Anna")

print("Aufsteigend:")
dll1.print_list_asc()
print("Absteigend:")
dll1.print_list_desc()

# 10.
print("10.")
dll1.insert("Anthony", 22321)
dll1.delete("John")

print("Aufsteigend:")
dll1.print_list_asc()
print("Absteigend:")
dll1.print_list_desc()

# 11.
print("11.")
dll2.delete("Aceina")

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 12.
print("12.")
dll2.delete("Zarathustra")

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()

# 13.
print("13.")
dll2.delete("Zenobius")

print("Aufsteigend:")
dll2.print_list_asc()
print("Absteigend:")
dll2.print_list_desc()
