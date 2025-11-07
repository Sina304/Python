class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, kid, edge=None):
        self.children.append((kid, edge))

    def DFS(self):
        values= [self.value]
        for child, edge in self.children:
            values.extend(child.DFS())
        return values
    
    def __str__(self):
        lines=[]
        def build_str(node, level=0, edge=None):
            if edge is not None:
                lines.append("  "*level+"-("+ edge + ") " + node.value)
            else:
                lines.append("  "*level+"-"+node.value)
            for child, label in node.children:
                build_str(child, level+1, label)
        build_str(self)
        return '\n'.join(lines)


###!ZASTOSOWANIE!###

root=Tree("Bogdan")
a=Tree("Stasiek (pierworodny)")
b=Tree("mid child")
c=Tree("youngest child")
a_a=Tree("Maciej")
a_a_a=Tree("Balerina")

root.add_child(a, "syn")
root.add_child(b, "syn")
root.add_child(c, "córka")
a.add_child(a_a, "wnuk")
a_a.add_child(a_a_a, "prawnuczka")


print("Przechodzenie drzewa DFS:")
print (root.DFS())

print("Ostateczna forma")
print(root)