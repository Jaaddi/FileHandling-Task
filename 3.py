def length_counter(filename):
    f = open(filename, 'r')
    A = f.read().strip().split('\n')
    f.close()
    l_c = 0
    for i in A:
        l_c += len(i)
    print(l_c)
filename = 'names.txt'
length_counter(filename)
