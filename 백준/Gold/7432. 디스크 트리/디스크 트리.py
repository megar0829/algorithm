class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []

def insert_directory(root, path):
    current = root
    components = path.split("\\")
    
    for component in components:
        found = False
        for child in current.children:
            if child.name == component:
                current = child
                found = True
                break
        
        if not found:
            new_directory = Directory(component)
            current.children.append(new_directory)
            current = new_directory

def print_directory_structure(directory, depth):
    print(" " * depth + directory.name)
    for child in sorted(directory.children, key=lambda x: x.name):
        print_directory_structure(child, depth + 1)

def main():
    n = int(input())
    root = Directory("ROOT")
    
    for _ in range(n):
        path = input()
        insert_directory(root, path)
    
    for child in sorted(root.children, key=lambda x: x.name):
        print_directory_structure(child, 0)

if __name__ == "__main__":
    main()