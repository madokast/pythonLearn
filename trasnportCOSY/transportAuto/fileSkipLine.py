# skip lines in an opened file

def skip(file,num):
    for i in range(num):
        file.readline()
        # print('skip~')

# test
# skip(None,2)
