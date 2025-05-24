class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def insert(self, path_parts):
        if not path_parts:
            return
        first, *rest = path_parts
        if first not in self.children:
            self.children[first] = Node(first)
        self.children[first].insert(rest)

    def tree(self, depth=0):
        for name in sorted(self.children):
            print(' ' * depth + name)
            self.children[name].tree(depth + 1)

def main():
    n = int(input())
    root = Node("")
    for _ in range(n):
        path = input().strip()
        parts = path.split("\\")
        root.insert(parts)

    root.tree()

if __name__ == "__main__":
    main()
