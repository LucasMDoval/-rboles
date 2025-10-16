from collections import deque

cola = deque(["Ana", "Luis", "Carlos", "Marta", "Sofía"])
print("Cola inicial:", list(cola))

for _ in range(3):
    atendido = cola.popleft()
    print(f"{atendido} fue atendido.")
    print("Estado actual de la cola:", list(cola))

print("\nPersonas con descuento para el próximo día:")
for persona in cola:
    print(f"{persona} recibe un descuento.")
