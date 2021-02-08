def writing_file(input_file, output_file):
    f = open(input_file, 'r')
    A = f.read().strip().split('\n')
    f.close()
    f = open(output_file, 'w')
    for i in A:
        f.write(i )
        f.write("    Programming Fundamental, Pakistan Studies" + '\n')
    f.close()
input_file = 'names.txt'
output_file = 'name_subj.txt'
writing_file(input_file, output_file)
