import multiprocessing 
import time 
start = time.perf_counter()


def do_something ():
  print('sleeping in 3 seconds..')
  time.sleep(3)
  print('done sleeping')

p1 = multiprocessing.Process(target = do_something)
p2 = multiprocessing.Process(target = do_something)

# Inicia o dois processos
p1.start()
p2.start()

# Continuidade do codigo
p1.join() 
p2.join() 

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)')