import concurrent.futures
import time 
start = time.perf_counter()

def do_something (seconds): 
  print(f'sleeping {seconds} in second(s)..')
  time.sleep(seconds) 
  return'\ndone sleeping'

# utiliza o threadPoolExecutor para executar os processos
with concurrent.futures.ThreadPoolExecutor () as executor:
  f1 = executor.submit(do_something, 1) 
  f2 = executor.submit(do_something, 1) 

  print(f1.result())
  print(f2.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} segundos(s)') 