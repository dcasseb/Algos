class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def __contem_recursivo(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node:
            return True
        if value < current_node.value:
            return self.__contem_recursivo(current_node.left, value)
        if value > current_node.value:
            return self.__contem_recursivo(current_node.right, value)
        
    def contem(self, value):
        return self.__contem_recursivo(self.root, value)
    
    def __insere_recursivo(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__insere_recursivo(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__insere_recursivo(current_node.right, value)
        return current_node

    def insere(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__insere_recursivo(self.root, value)

    def BFS(self):
        current_node = self.root
        queue = []
        resultados = []
        queue.append(current_node)

        while(len(queue)) > 0:
            current_node = queue.pop(0)
            resultados.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return resultados
    
    def pre_ordem(self):
        resultados = []
        def caminho(current_node):
            resultados.append(current_node.value)
            if current_node.left is not None:
                caminho(current_node.left)
            if current_node.right is not None:
                caminho(current_node.right)
        caminho(self.root)
        return resultados
    
    def in_ordem(self):
        resultados = []
        def caminho(current_node):
            if current_node.left is not None:
                caminho(current_node.left)
            resultados.append(current_node.value)
            if current_node.right is not None:
                caminho(current_node.right)
        caminho(self.root)
        return resultados
    
    def pos_ordem(self):
        resultados = []
        def caminho(current_node):
            if current_node.left is not None:
                caminho(current_node.left)
            if current_node.right is not None:
                caminho(current_node.right)
            resultados.append(current_node.value)
        caminho(self.root)
        return resultados

#minha_arvore = ArvoreBinaria()
#minha_arvore.insere(4)
#minha_arvore.insere(2)
#minha_arvore.insere(1)
#minha_arvore.insere(3)
#minha_arvore.insere(6)
#minha_arvore.insere(7)
#minha_arvore.insere(5)

#print('Raiz:', minha_arvore.root.value)
#print('Raiz - esquerda:', minha_arvore.root.left.value)
#print('Raiz - direita:', minha_arvore.root.right.value)
#print(minha_arvore.BFS())
#print(minha_arvore.pre_ordem())
#print(minha_arvore.in_ordem())
#print(minha_arvore.pos_ordem())