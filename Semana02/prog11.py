#f = open('test.txt', 'r')
#print(f.name)
#print(f.mode)
#f.close()


#with open("test.txt", "r") as f:
    #pass
    
    #f_contents = f.read()
    #print(f_contents)

    #f_contents = f.readlines()
    #print(f_contents)

   
    #f_contents = f.readline()
    #print(f_contents)
    #f_contents = f.readline()
    #print(f_contents)


    #f_contents = f.readline()
    #print(f_contents, end = '')
    #f_contents = f.readline()
    #print(f_contents, end = '')

    #for line in f:
        #print(line, end = '')


    #f_contents = f.read(100)
    #print(f_contents, end = '')
    #f_contents = f.read(100)
    #print(f_contents, end = '')
    #f_contents = f.read(100)
    #print(f_contents, end = '')


    #size_to_read = 10
    #f_contents = f.read(size_to_read)
    #while len(f_contents) > 0:
        #print(f_contents, end = '*')
        #_contents = f.read(size_to_read)


    #size_to_read = 10
    #f_contents = f.read(size_to_read)
    #print(f_contents, end = '')
    #f.seek(0)
    #_contents = f.read(size_to_read)
#print(f.mode)
#print(f.closed)



#with open("test2.txt", "w") as f:
    #f.write("Test")
    #f.seek(0)
    #f.write("R")



with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)
