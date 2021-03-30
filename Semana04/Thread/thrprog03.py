import threading 
import time 
start = time.perf_counter()

def do_something (seconds): 
  print(f'sleeping {seconds} in second(s)..')
  time.sleep(seconds) 
  print('\ndone sleeping')

# cria funcao com argumento específico
threads=[]
for _ in range (5):
  t = threading.Thread(target=do_something, args=[5.0])
  t.start()
  threads.append(t)

for thread in threads:
  thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)')