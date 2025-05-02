from collections import deque
import sys

def main():
    queue = deque()
    for line in sys.stdin:
        parts = line.strip().split()
        if not parts:
            continue
        cmd = parts[0]
        if cmd == "push":
            queue.append(int(parts[1]))
            print("ok")
        elif cmd == "pop":
            if queue:
                print(queue.popleft())  # O(1)
            else:
                print("error")
        elif cmd == "front":
            if queue:
                print(queue[0])         # O(1)
            else:
                print("error")
        elif cmd == "size":
            print(len(queue))           # O(1)
        elif cmd == "clear":
            queue.clear()               # O(1)
            print("ok")
        elif cmd == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()