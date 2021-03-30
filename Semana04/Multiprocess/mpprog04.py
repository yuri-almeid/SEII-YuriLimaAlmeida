import concurrent.futures
import multiprocessing 
import time 
start = time.perf_counter()


def do_something (seconds):
  print('sleeping {seconds} in 1 seconds(s)..')
  time.sleep(seconds)
  return 'done sleeping'

# roda o executor
with concurrent.futures.ProcessPoolExecutor() as executor:
  f1 = executor.submit(do_something,1)
  print(f1.result())


finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)')