class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def imprimir(self) -> None:
        NoAtual = self
        while NoAtual:
            print(NoAtual.dado, end = "->")
            NoAtual  = NoAtual.proximo
        print("Null")

def CriaNo(lista,dado) -> Node:
    Notemp = Node(dado)
    Notemp.proximo = lista
    return Notemp




node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.proximo = node2
node2.proximo = node3
node3.proximo = node4
node4.proximo = node5

node1.imprimir()