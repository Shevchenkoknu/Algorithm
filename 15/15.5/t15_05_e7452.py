n = int(input())
values = map(int, input().split())

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None
        self.prev: 'Node | None' = None

class List:
    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def Tail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def Reverse(self) -> None:
        current = self.tail
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

lst = List()
for val in values:
    lst.Tail(val)

lst.Print()
lst.Reverse()
