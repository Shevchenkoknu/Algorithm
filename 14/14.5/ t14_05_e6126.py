from collections import deque
import sys

class Queue:
    def __init__(self):
        self.queue = deque()

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return "error"

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()
        return "ok"

    def push(self, n):
        self.queue.append(n)
        return "ok"

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return "error"

def main():
    q = Queue()
    for line in sys.stdin:
        command = line.strip()
        if not command:
            continue

        if command.startswith("push"):
            _, num = command.split()
            print(q.push(int(num)))
        elif command == "pop":
            print(q.pop())
        elif command == "front":
            print(q.front())
        elif command == "size":
            print(q.size())
        elif command == "clear":
            print(q.clear())
        elif command == "exit":
            print("bye")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
