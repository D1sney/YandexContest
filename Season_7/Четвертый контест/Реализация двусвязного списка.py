class Node:
    def __init__(self, value):
        # любое значение; в Python переменные — это по сути ссылки
        self.value = value  
        # ссылка на следующий узел (или None)
        self.next = None    
        # ссылка на предыдущий узел (или None)
        self.prev = None    

class DoublyLinkedList:
    def __init__(self):
        # голова и хвост пустого списка
        self.head = None
        self.tail = None

    def append(self, value):
        """Добавляет узел в конец списка."""
        new_node = Node(value)
        if not self.head:
            # список пустой → новый узел и голова, и хвост
            self.head = self.tail = new_node
        else:
            # связываем старый хвост и новый узел
            self.tail.next = new_node
            new_node.prev = self.tail
            # обновляем хвост
            self.tail = new_node

    def prepend(self, value):
        """Добавляет узел в начало списка."""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            # связываем новый узел и старую голову
            new_node.next = self.head
            self.head.prev = new_node
            # обновляем голову
            self.head = new_node

    def find(self, value):
        """Ищет первый узел с заданным значением."""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None  # не найден

    def insert_after(self, node, value):
        """Вставляет новый узел после заданного."""
        if node is self.tail:
            # эквивалент append
            self.append(value)
        else:
            new_node = Node(value)
            successor = node.next
            # перенастраиваем связи
            node.next = new_node
            new_node.prev = node
            new_node.next = successor
            successor.prev = new_node

    def delete(self, node):
        """Удаляет указанный узел из списка."""
        # если узел в середине или в начале
        if node.prev:
            node.prev.next = node.next
        else:
            # удаляем голову
            self.head = node.next
        # если узел в середине или в конце
        if node.next:
            node.next.prev = node.prev
        else:
            # удаляем хвост
            self.tail = node.prev
        # «отсоединяем» узел (не обязательно, но чисто)
        node.prev = None
        node.next = None

    def traverse_forward(self):
        """Генератор для прохода от головы к хвосту."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def traverse_backward(self):
        """Генератор для прохода от хвоста к голове."""
        current = self.tail
        while current:
            yield current.value
            current = current.prev



dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)

print(list(dll.traverse_forward()))   # [5, 10, 20]
print(list(dll.traverse_backward()))  # [20, 10, 5]

node_10 = dll.find(10)
dll.insert_after(node_10, 15)
print(list(dll.traverse_forward()))   # [5, 10, 15, 20]

dll.delete(node_10)
print(list(dll.traverse_forward()))   # [5, 15, 20]