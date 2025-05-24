class Stack:
    def __init__(self):
        self.stack = []

    def back(self):
        if self.stack:
            return self.stack[-1]
        else:
            return "error"

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
        return "ok"

    def push(self, n):
        self.stack.append(n)
        return "ok"

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "error"

def main():
    s = Stack()
    while True:
        command = input().strip()
        if command == "exit":
            print("bye")
            break
        elif command.startswith("push"):
            _, n = command.split()
            print(s.push(int(n)))
        elif command == "pop":
            print(s.pop())
        elif command == "back":
            print(s.back())
        elif command == "size":
            print(s.size())
        elif command == "clear":
            print(s.clear())

if __name__ == "__main__":
    main()