from tasks import soma, hello

if __name__ == "__main__":
    print("Enviando tarefas...")

    r1 = soma.delay(10, 20)
    r2 = hello.delay("Rodrigo")

    print("Tarefa soma enviada:", r1.id)
    print("Tarefa hello enviada:", r2.id)

    print("Aguardando resultados...")

    print("Resultado soma:", r1.get(timeout=10))
    print("Resultado hello:", r2.get(timeout=10))