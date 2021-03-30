import threading 
import time 
start = time.perf_counter()

# cria a função
def do_something (): 
  print('sleeping in 3 seconds..')
#    Aguarda 3 segundos
  time.sleep(3) 
  print('done sleeping')

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t1.start()
t2.start()
t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)') 