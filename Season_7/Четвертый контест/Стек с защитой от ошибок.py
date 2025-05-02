import sys

stack = []
for line in sys.stdin:
    cmd = line.strip().split()
    if not cmd:
        continue
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
        print("ok")
    elif cmd[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print("error")
    elif cmd[0] == "back":
        if stack:
            print(stack[-1])
        else:
            print("error")
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "clear":
        stack.clear()
        print("ok")
    elif cmd[0] == "exit":
        print("bye")
        break