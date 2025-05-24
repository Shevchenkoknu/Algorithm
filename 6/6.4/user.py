_hash_table = []
_capacity = 0
_size = 0

def _hash(author, title):
    return hash((author, title))

def _resize():
    global _hash_table, _capacity, _size
    old_hash_table = _hash_table
    old_capacity = _capacity

    _capacity *= 2
    if _capacity == 0:
        _capacity = 8
    _hash_table = [[] for _ in range(_capacity)]
    _size = 0

    for bucket in old_hash_table:
        for author, title in bucket:
            addBook(author, title)

def init():
    global _hash_table, _capacity, _size
    _capacity = 8
    _hash_table = [[] for _ in range(_capacity)]
    _size = 0

def addBook(author, title):
    global _hash_table, _capacity, _size

    if _capacity == 0:
        init()
    if _size / _capacity >= 0.75:
        _resize()

    index = _hash(author, title) % _capacity
    book_entry = (author, title)

    if book_entry not in _hash_table[index]:
        _hash_table[index].append(book_entry)
        _size += 1

def find(author, title):
    global _hash_table, _capacity

    if _capacity == 0:
        return False

    index = _hash(author, title) % _capacity
    book_entry = (author, title)
    return book_entry in _hash_table[index]

def delete(author, title):
    global _hash_table, _capacity, _size

    if _capacity == 0:
        return

    index = _hash(author, title) % _capacity
    book_entry = (author, title)

    if book_entry in _hash_table[index]:
        _hash_table[index].remove(book_entry)
        _size -= 1

def findByAuthor(author):
    global _hash_table
    result_titles = []

    for bucket in _hash_table:
        for book_author, book_title in bucket:
            if book_author == author:
                result_titles.append(book_title)

    return sorted(result_titles)