import threading 
import time 
start = time.perf_counter()

def do_something (): 
  print('sleeping in 3 seconds..')
  time.sleep(3) 
  print('done sleeping')

# Cria quantidade de processos no for
threads=[]
for _ in range (10):
  t = threading.Thread(target=do_something)
  t.start()
  threads.append(t)

for thread in threads:
  thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)') 