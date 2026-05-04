from tasks import soma
import time

if __name__ == "__main__":
    print("Enviando tarefas para o Celery...")

    for i in range(5):
        result = soma.delay(i, i * 2)
        print(f"Tarefa enviada: {i} + {i*2} | task_id={result.id}")

    print("Aguardando resultados...")

    time.sleep(5)

    print("Finalizado.")