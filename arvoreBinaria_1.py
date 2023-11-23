class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def insere(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contem(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

minha_arvore = ArvoreBinaria()
minha_arvore.insere(4)
minha_arvore.insere(5)
minha_arvore.insere(3)

print(minha_arvore.root.value)
print(minha_arvore.root.left.value)
print(minha_arvore.root.right.value)
print(minha_arvore.contem(2))

#O CÓDIGO APRESENTA ERROS QUANDO OS DOIS VALORES A SEREM INSERIDOS SAO MAIORES QUE O NÓ RAIZ