import multiprocessing 
import time 
start = time.perf_counter()


def do_something (seconds):
  print('sleeping {seconds} in 1 seconds(s)..')
  time.sleep(seconds)
  print('done sleeping')


# abre 10 processos que rodarão por 2 segundos de forma paralela
process = [] 
for _ in range(10): 
  p = multiprocessing.Process(target= do_something, args=[2.0])
  p.start()
  process.append(p)


for processo in process:
   processo.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)')