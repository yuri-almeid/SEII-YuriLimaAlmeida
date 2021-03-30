import concurrent.futures
import multiprocessing 
import time 
start = time.perf_counter()


def do_something (seconds):
  print(f'sleeping {seconds} second(s)..')
  time.sleep(seconds)
  return f'done sleeping.. {seconds}'


# cria processos com argumentos diferentes
with concurrent.futures.ProcessPoolExecutor() as executor:
  secs = [5,4,3,2,1]
  results = executor.map(do_something, secs)


  for result in results:
     print(result)       

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)')