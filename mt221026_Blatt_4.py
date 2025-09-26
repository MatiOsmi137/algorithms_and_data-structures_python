class TreeContactNode:
    def __init__(self, contact_name=None, phone=None):
        self.contact_name = contact_name
        self.phone = phone
        self.left = None
        self.right = None

    def __str__(self):
        return self.contact_name + ": " + self.phone

    def insert(self, name, phone):
        q = TreeContactNode(name, phone)
        r = None
        p = self

        while p is not None:
            r = p
            if q.contact_name < p.contact_name:
                p = p.left
            else:
                p = p.right

        if r is None:
            p = q
        else:
            if q.contact_name < r.contact_name:
                r.left = q
            else:
                r.right = q

    def inorder(self, p):
        if p is not None:
            self.inorder(p.left)
            print(p)
            self.inorder(p.right)

    def preorder(self, p):
        if p is not None:
            print(p)
            self.preorder(p.left)
            self.preorder(p.right)

    def postorder(self, p):
        if p is not None:
            self.postorder(p.left)
            self.postorder(p.right)
            print(p)

    def inorder_iterative(self, p):
        stack = []
        result = []

        current = p

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append((current.contact_name, current.phone))
                current = current.right

        return result

    def find_phone_number(self, name):
        if self.contact_name == name:
            return self.phone
        elif name < self.contact_name and self.left:
            return self.left.find_phone_number(name)
        elif name > self.contact_name and self.right:
            return self.right.find_phone_number(name)
        else:
            return None

    def minimum(self):
        current = self
        while current.left:
            current = current.left
        return current.contact_name

    def maximum(self):
        current = self
        while current.right:
            current = current.right
        return current.contact_name


root = TreeContactNode("mati", "2137")

root.insert("bert", "999")
root.insert("artner", "123")
root.insert("krist", "789")
root.insert("huber", "334")
root.insert("berger", "333")
print("0. Rekursiv inorder:")
root.inorder(root)
print("1. Iterativ in-order:")
print(root.inorder_iterative(root))
print("2a. Rekursiv post-order:")
root.preorder(root)
print("2b. Iterativ post-order:")
root.postorder(root)
nameToFind = "artner"
print(f"3. Die Nummer von {nameToFind} ist {root.find_phone_number(nameToFind)}")
print("4a. Minimus des Baums:")
print(root.minimum())
print("4b. Maximus des Baums:")
print(root.maximum())
