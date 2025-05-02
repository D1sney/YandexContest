class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_back(self):
        if not self.tail:
            raise IndexError("pop from empty list")
        val = self.tail.value
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.tail = None
        return val

    def back(self):
        if not self.tail:
            raise IndexError("back from empty list")
        return self.tail.value

    def clear(self):
        self.head = self.tail = None

    def size(self):
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next
        return cnt

def main():
    import sys
    dll = DoublyLinkedList()
    for line in sys.stdin:
        cmd = line.strip().split()
        if not cmd:
            continue
        if cmd[0] == "push":
            dll.append(int(cmd[1]))
            print("ok")
        elif cmd[0] == "pop":
            try:
                print(dll.pop_back())
            except IndexError:
                print("error")
        elif cmd[0] == "back":
            try:
                print(dll.back())
            except IndexError:
                print("error")
        elif cmd[0] == "size":
            print(dll.size())
        elif cmd[0] == "clear":
            dll.clear()
            print("ok")
        elif cmd[0] == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()