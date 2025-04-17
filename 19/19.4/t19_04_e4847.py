import sys
import heapq

class Queue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = '<removed>'
        self.counter = 0

    def add(self, id, priority):
        entry = [-priority, self.counter, id]
        self.entry_finder[id] = entry
        heapq.heappush(self.heap, entry)
        self.counter += 1

    def pop(self):
        while self.heap:
            priority, _, id = heapq.heappop(self.heap)
            if id != self.REMOVED:
                del self.entry_finder[id]
                return f"{id} {-priority}"
        return None

    def change(self, id, new_priority):
        old = self.entry_finder.pop(id)
        old[2] = self.REMOVED
        new = [-new_priority, self.counter, id]
        self.entry_finder[id] = new
        heapq.heappush(self.heap, new)
        self.counter += 1

def main():
    pq = Queue()
    output = []

    for line in sys.stdin:
        parts = line.strip().split()
        if not parts:
            continue
        command = parts[0]

        if command == "ADD":
            id = parts[1]
            priority = int(parts[2])
            pq.add(id, priority)
        elif command == "POP":
            result = pq.pop()
            if result:
                output.append(result)
        elif command == "CHANGE":
            id = parts[1]
            new_priority = int(parts[2])
            pq.change(id, new_priority)

    print('\n'.join(output))

if __name__ == "__main__":
    main()