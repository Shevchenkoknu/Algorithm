class Node:
    def __init__(self, is_leaf=False, value=None):
        self.value = value
        self.children = []
        self.is_leaf = is_leaf

    def add(self, child):
        self.children.append(child)

    def evaluate(self, is_first_player_turn):
        if self.is_leaf:
            return self.value
        results = [child.evaluate(not is_first_player_turn) for child in self.children]
        return max(results) if is_first_player_turn else min(results)

def tree(data):
    nodes = {i + 1: Node() for i in range(len(data) + 1)}

    for i, line in enumerate(data, start=2):
        parts = line.split()
        node_type = parts[0]
        parent_index = int(parts[1])

        if node_type == 'L':
            value = int(parts[2])
            nodes[i] = Node(is_leaf=True, value=value)

        nodes[parent_index].add(nodes[i])

    return nodes[1]

def main():
    n = int(input())
    data = [input().strip() for _ in range(n - 1)]
    root = tree(data)
    result = root.evaluate(is_first_player_turn=True)
    if result > 0:
        print(f'+{result}')
    else:
        print(result)

if __name__ == "__main__":
    main()
