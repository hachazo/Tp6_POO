import threading
import time

def print_hola(thread_id):
    time.sleep(thread_id)
    print(f"Hola, soy el hilo {thread_id}")

threads = []

for i in range(1,7):
    thread = threading.Thread(target=print_hola, args=(i,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

print("Fin del programa")