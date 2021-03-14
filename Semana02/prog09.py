import os
from datetime import datetime

os.getcwd()

os.chdir('/')
os.listdir()

os.mkdir('OS-Demo') 
os.makedirs('OS-Demo/Sub-Dir-1') 


os.rmdir('OS-Demo')
os.removedirs('OS-Demo')

os.rename('test.txt', 'demo.txt')


os.stat('test.txt')
print(os.stat('demo.txt').st_size) 

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


for dirpath, dirnames, filenames in os.walk('/media/yuri/Local/OneDrive/Git/SEII-YuriLimaAlmeida/Semana02'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()


os.environ.get('HOME')
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')


os.path.basename
os.path.dirname('/tmp/test.txt')
os.path.split('/tmp/test.txt')
os.path.exists('/tmp/test.txt')
os.path.isdir('/tmp/test.txt')
os.path.isfile('/tmp/test.txt')
os.path.splitext('/tmp/test.txt')