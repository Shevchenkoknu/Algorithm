_hash_table = []
_capacity = 0
_size = 0
_DELETED = object()

def _hash(author, title):
    return hash((author, title))

def _resize():
    global _hash_table, _capacity, _size
    old_hash_table = _hash_table
    old_capacity = _capacity
    _capacity *= 2

    if _capacity == 0:
        _capacity = 8
    _hash_table = [None] * _capacity
    _size = 0

    for i in range(old_capacity):
        item = old_hash_table[i]
        if item is not None and item is not _DELETED:
            addBook(item[0], item[1])

def init():
    global _hash_table, _capacity, _size
    _capacity = 8
    _hash_table = [None] * _capacity
    _size = 0

def addBook(author, title):
    global _hash_table, _capacity, _size
    if _size >= _capacity // 2:
        _resize()
    initial_index = _hash(author, title) % _capacity
    index = initial_index

    while True:
        if _hash_table[index] is None or _hash_table[index] is _DELETED:
            _hash_table[index] = (author, title)
            _size += 1
            return
        elif _hash_table[index] == (author, title):
            return
        index = (index + 1) % _capacity

def find(author, title):
    global _hash_table, _capacity

    if _capacity == 0:
        return False

    initial_index = _hash(author, title) % _capacity
    index = initial_index

    while True:
        if _hash_table[index] is None:
            return False
        elif _hash_table[index] == (author, title):
            return True

        index = (index + 1) % _capacity
        if index == initial_index:
            return False

def delete(author, title):
    global _hash_table, _capacity, _size

    if _capacity == 0:
        return

    initial_index = _hash(author, title) % _capacity
    index = initial_index

    while True:
        if _hash_table[index] is None:
            return
        elif _hash_table[index] == (author, title):
            _hash_table[index] = _DELETED
            _size -= 1
            return

        index = (index + 1) % _capacity
        if index == initial_index:
            return

def findByAuthor(author):
    global _hash_table

    result_titles = []
    for item in _hash_table:
        if item is not None and item is not _DELETED and item[0] == author:
            result_titles.append(item[1])

    return sorted(result_titles)
