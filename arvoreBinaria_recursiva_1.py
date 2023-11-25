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
        return self.__contem_recursivo(self.root, value) #chama a função recursiva de verificação que está protegida
    
    def __insere_recursivo(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__insere_recursivo(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__insere_recursivo(current_node.right, value)
        return current_node

    def insere(self, value):
        if self.root is None: #se raiz estiver vazia:
            self.root = Node(value) #a raiz receberá o valor do nó inserido
        self.__insere_recursivo(self.root, value) #chama a função recursiva de inserção que está protegida

    def BuscaEmLargura(self): #a Busca em Largura (BFS, Breadth First Search) busca os nós pelo nível, ou altura que eles se encontram
        current_node = self.root #define o nó atual sendo a raiz
        queue = [] #inicializa uma fila vazia
        resultados = [] #inicializa uma fila 'resultados' vazia, onde serão armazenados os valores dos nós que serão retirados da árvore
        queue.append(current_node) #adiciona os nós da árvore na fila 'queue'

        while(len(queue)) > 0: #enquanto a fila 'queue' não estiver vazia:
            current_node = queue.pop(0) #retira a nó atual da fila (raiz)
            resultados.append(current_node.value) #adiciona para a fila 'resultados' o valor do nó atual
            if current_node.left is not None: #se existir nó na esquerda:
                queue.append(current_node.left) #o nó da esquerda e adicionado na última posição (append) da fila
            if current_node.right is not None: #se existir nó na direita:
                queue.append(current_node.right) #o nó da direita e adicionado na última posição (append) atualizada da fila
        return resultados #o resultado retornado é a fila composta de todos os nós presentes na árvore que levaram 'pop' na busca
    
    #implementar BuscaEmLargura de modo que a saida seja do ultimo nivel para o primeiro
    #no loop, mandar para a fila 'resultados' os nós da direita pra esquerda, ao invés da esquerda para direita, e imprimir a fila de trás pra frente

    def BuscaEmLargura_contrario(self): #a Busca em Largura reversa busca os nós pela altura mais alta que eles se encontram até a raiz 
        current_node = self.root #define o nó atual como sendo a raiz
        queue = [] #inicializa uma fila 'queue' vazia
        resultados = [] #inicializa uma fila 'resultados' vazia
        queue.append(current_node) #adiciona a árvore na fila 'queue'
        #o processo é basicamente o mesmo da Busca em Largura normal, apenas invertendo algumas ordens de busca
        while(len(queue)) > 0:
            current_node = queue.pop(0) #retira a primeiro nó (raiz) da fila
            resultados.append(current_node.value) #adiciona para a fila 'resultados' o valor do nó atual
            if current_node.right is not None: #começa a percorrer primeiramente os nós da direita
                queue.append(current_node.right)
            if current_node.left is not None: #depois percorre os nós da esquerda
                queue.append(current_node.left)
        return resultados[::-1] #inverte a fila
    
    def pre_ordem(self):
        resultados = [] #inicializa uma fila vazia para conter os nós presentes na árvore
        def caminho(current_node): #a função é inicializada a partir do nó atual (raiz)
            resultados.append(current_node.value) #a fila 'resultados' recebe os valores do nó atual percorrido pela função
            if current_node.left is not None: #se existir nó na esquerda:
                caminho(current_node.left) #a função percorrerá pela esquerda
            if current_node.right is not None: #se existir nó na direita:
                caminho(current_node.right) #a função percorrerá pela direita
        caminho(self.root) #faz chamada da função 'caminho' iniciando na raiz
        return resultados #o resultado retornado é a fila composta de todos os nós presentes na árvore
    
    def preOrdemRecursivo(self):
        self.visitaRecursiva_Pre(self.root) #faz chamada pra função recursiva Pre Ordem e inicializa ela a partir da raiz
    def visitaRecursiva_Pre(self, root):
        if root: # se a raiz não for nula:
            print(root.value) #são impressos na tela um nó por linha presentes na árvore
            self.visitaRecursiva_Pre(root.left) #a função percorre os nós da esquerda
            self.visitaRecursiva_Pre(root.right) #a função percorre os nós da esquerda

    def in_ordem(self):
        resultados = []
        def caminho(current_node): #a função é inicializada a partir do nó atual (raiz)
            if current_node.left is not None:
                caminho(current_node.left)
            resultados.append(current_node.value) #a fila 'resultados' recebe os valores do nó atual percorrido pela função
            if current_node.right is not None:
                caminho(current_node.right)
        caminho(self.root) #faz chamada da função 'caminho' iniciando na raiz
        return resultados #o resultado retornado é a fila composta de todos os nós presentes na árvore
    
    def inOrdemRecursivo(self):
        self.visitaRecursiva_In(self.root) #faz chamada pra função recursiva In Ordem e inicializa ela a partir da raiz
    def visitaRecursiva_In(self, root):
        if root:
            self.visitaRecursiva_In(root.left) #a função percorre os nós da esquerda
            print(root.value) #são impressos na tela um nó por linha presentes na árvore
            self.visitaRecursiva_In(root.right) #a função percorre os nós da direita

    def pos_ordem(self): #a função é inicializada a partir do nó atual (raiz)
        resultados = []
        def caminho(current_node):
            if current_node.left is not None: #se a esquerda do nó atual não estiver vazia:
                caminho(current_node.left) #a função percorrerá o lado esquerdo do nó
            if current_node.right is not None: #se a direita do nó atual não estiver vazia:
                caminho(current_node.right) #a função percorrerá o lado direito do nó
            resultados.append(current_node.value) #a fila 'resultados' recebe os valores do nó atual percorrido pela função
        caminho(self.root) #faz chamada da função 'caminho' iniciando na raiz
        return resultados #o resultado retornado é a fila composta de todos os nós presentes na árvore
    
    def posOrdemRecursivo(self):
        self.visitaRecursiva_Pos(self.root) #faz chamada pra função recursiva Pos Ordem e inicializa ela a partir da raiz
    def visitaRecursiva_Pos(self, root):
        if root: #se a raiz não for nula:
            self.visitaRecursiva_Pos(root.left) #a função percorre os nós da esquerda
            self.visitaRecursiva_Pos(root.right) #a função percorre os nós da direita
            print(root.value) #são impressos na tela um nó por linha presentes na árvore
    
    #Implemetar método para calcular a altura de uma árvore, de uma sub-árvore da esquerda e sub-árvore da direita e qual sub-árvore é maior
    
    #ESTUDAR VARIAÇÕES DOS MÉTODOS DE ORDENAÇÃO PARA A PROVA

minha_arvore = ArvoreBinaria() #cria um objeto chamado 'minha_arvore' e define ele como sendo um objeto da classe 'ArvoreBinaria'
minha_arvore.insere(4) #utiliza a função 'insere' para adicionar os nós da árvore. * O primeiro nó é sempre a raiz *
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
print(minha_arvore.preOrdemRecursivo())
print(minha_arvore.inOrdemRecursivo())
print(minha_arvore.posOrdemRecursivo())
