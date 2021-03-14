import os

# os.chdir('/home/')
# print(os.getcwd())



for f in os.listdir():

    f_name, f_ext = os.path.splitext(f)
    print(f_name)
    
    f_title, f_num = f_name.split('-')
    
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    
    print('{}-{}{}'.format(f_num, f_title, f_ext))

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)

    os.rename(f, new_name)