import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True


def is_prefix(root, word):
    node = root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return True


def count_prefixes(words, queries):
    root = TrieNode()
    for word in words:
        insert_word(root, word)

    count = 0
    for query in queries:
        if is_prefix(root, query):
            count += 1

    return count


if __name__ == "__main__":
    N, M = map(int, input().split())
    
    set_S = []
    for _ in range(N):
        set_S.append(input().strip())

    query_strings = []
    for _ in range(M):
        query_strings.append(input().strip())

    result = count_prefixes(set_S, query_strings)
    print(result)