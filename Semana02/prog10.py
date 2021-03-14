
f = open("test.txt", "r")
f = open("test.txt", "w")
f = open("test.txt", "a")
f = open("test.txt", "r+")
print(f.name)
print(f.mode)
f.close()


with open("test.txt", "r") as f:
    pass
    
    f_contents = f.read()
    print(f_contents, end='')
    f_contents = f.readlines()
    print(f_contents)


    f_contents = f.readline()
    print(f_contents, end = '')
    f_contents = f.readline()
    print(f_contents, end = '')
    

    for line in f:
        print(line, end = '')


    f_contents = f.read(100)
    print(f_contents, end = '')

    size_to_read = 100
    f_contents = f.read(size_to_read)
    
    while len(f_contents) > 0:
        print(f_contents)
        f_contents = f.read(size_to_read)


    # size_to_read = 
    # f_contents = f.read(size_to_read)
    # print(f_contents, end = '')
    
    # print(f.tell())
    
    # f.seek(0)
    # f_contents = f.read(size_to_read)