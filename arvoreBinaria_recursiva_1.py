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

    def BuscaEmLargura(self):
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
    
    #implementar BuscaEmLargura de modo que a saida seja do ultimo nivel para o primeiro
    #no loop, mandar para a lista 'resultados' os nós da direita pra esquerda, ao invés da esquerda para direita, e imprimir a lista de trás pra frente

    def BuscaEmLargura_contrario(self):
        current_node = self.root
        queue = []
        resultados = []
        queue.append(current_node)

        while(len(queue)) > 0:
            current_node = queue.pop(0)
            resultados.append(current_node.value)
            if current_node.right is not None:
                queue.append(current_node.right)
            if current_node.left is not None:
                queue.append(current_node.left)
        return resultados[::-1] #inverte a lista
    
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
    
    def preOrdemRecursivo(self):
        self.visitaRecursiva(self.root)
    def visitaRecursiva(self, root):
        if root:
            print(root.value)
            self.visitaRecursiva(root.left)
            self.visitaRecursiva(root.right)
    
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
    
    def inOrdemRecursivo(self):
        self.visitaRecursiva(self.root)
    def visitaRecursiva(self, root):
        if root:
            self.visitaRecursiva(root.left)
            print(root.value)
            self.visitaRecursiva(root.right)

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
    
    def posOrdemRecursivo(self):
        self.visitaRecursiva(self.root)
    def visitaRecursiva(self, root):
        if root:
            self.visitaRecursiva(root.left)
            self.visitaRecursiva(root.right)
            print(root.value)
    
    #Implemetar método para calcular a altura de uma árvore, de uma sub-árvore da esquerda e sub-árvore da direita e qual sub-árvore é maior
    
    #ESTUDAR VARIAÇÕES DOS MÉTODOS DE ORDENAÇÃO PARA A PROVA

minha_arvore = ArvoreBinaria()
minha_arvore.insere(4)
minha_arvore.insere(2)
minha_arvore.insere(1)
minha_arvore.insere(3)
minha_arvore.insere(6)
minha_arvore.insere(7)
minha_arvore.insere(5)

print('Raiz:', minha_arvore.root.value)
print('Raiz - esquerda:', minha_arvore.root.left.value)
print('Raiz - direita:', minha_arvore.root.right.value)
print(minha_arvore.BuscaEmLargura())
print(minha_arvore.BuscaEmLargura_contrario())
print(minha_arvore.pre_ordem())
print(minha_arvore.in_ordem())
print(minha_arvore.pos_ordem())
minha_arvore.preOrdemRecursivo()
minha_arvore.inOrdemRecursivo()
minha_arvore.posOrdemRecursivo()
