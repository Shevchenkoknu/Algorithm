from collections import deque
import sys

class Deque:
    def __init__(self):
        self.deque = deque()

    def front(self):
        if self.deque:
            return self.deque[0]
        else:
            return "error"

    def back(self):
        if self.deque:
            return self.deque[-1]
        else:
            return "error"

    def size(self):
        return len(self.deque)

    def clear(self):
        self.deque.clear()
        return "ok"

    def push_front(self, n):
        self.deque.appendleft(n)
        return "ok"

    def push_back(self, n):
        self.deque.append(n)
        return "ok"

    def pop_front(self):
        if self.deque:
            return self.deque.popleft()
        else:
            return "error"

    def pop_back(self):
        if self.deque:
            return self.deque.pop()
        else:
            return "error"

def main():
    d = Deque()
    for line in sys.stdin:
        command = line.strip()
        if not command:
            continue

        if command.startswith("push_front"):
            _, num = command.split()
            print(d.push_front(int(num)))
        elif command.startswith("push_back"):
            _, num = command.split()
            print(d.push_back(int(num)))
        elif command == "pop_front":
            print(d.pop_front())
        elif command == "pop_back":
            print(d.pop_back())
        elif command == "front":
            print(d.front())
        elif command == "back":
            print(d.back())
        elif command == "size":
            print(d.size())
        elif command == "clear":
            print(d.clear())
        elif command == "exit":
            print("bye")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
