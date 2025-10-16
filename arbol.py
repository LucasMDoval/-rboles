import time


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(nodo.der, valor)

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorden(nodo.der)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.valor, end=" ")

arbol = ArbolBST()
nodos = [50, 30, 70, 20, 40, 60, 80]
for n in nodos:
    arbol.insertar(n)

print("Recorrido en preorden:")
inicio = time.time()
arbol.preorden(arbol.raiz)
print("\nTiempo:", time.time() - inicio)

print("\nRecorrido en inorden:")
inicio = time.time()
arbol.inorden(arbol.raiz)
print("\nTiempo:", time.time() - inicio)

print("\nRecorrido en postorden:")
inicio = time.time()
arbol.postorden(arbol.raiz)
print("\nTiempo:", time.time() - inicio)
