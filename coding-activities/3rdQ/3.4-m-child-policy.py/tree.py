class Vertex:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:

    def __init__(self, root_vrtx: Vertex):
        self.root = root_vrtx

    def print_tree(self, root = None, level = 0):
        if root is None:
            root = self.root

        print(('\t' * level) + str(root.value))
        for child in root.children:
            self.print_tree(child, level + 1)

    def compute_m(self, root = None):
        try:
            if root is None:
                    root = self.root
            count = len(root.children)
            for child in root.children:
                temp_child = self.compute_m(child)
                if temp_child > count:
                    count = temp_child
            return count 
        except Exception as e:
            return e    



        
