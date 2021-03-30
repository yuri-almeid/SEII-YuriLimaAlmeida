import time 
start = time.perf_counter()


def do_something ():
  print('sleeping in 3 seconds..')
  time.sleep(3)  
  print('done sleeping')

do_something()

do_something()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} second(s)')