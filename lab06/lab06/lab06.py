import sys



def print_args(in_list):
    for i in in_list:
        print(i)


def check(in_list):
    parameter = in_list[1]
    conditions = ['-p', '-i', '-h', '-w', '-r']
    if parameter in conditions:
        return True
    return False


def flags(in_list):
    flag = in_list[1]
    if check(in_list):
        if flag == '-p':
            for i in in_list[2:]:
                print(i)
        elif flag == '-i':
            print('Hello World')
        elif flag == '-h':
            print('''Valid flags:
-p : prints out all the command line arguments after the -p
-i : prints "Hello World"
-h : prints out a help command''')
        elif flag == '-w':
            with open(in_list[2], 'w') as file:
                if len(in_list) > 3:
                    for i in in_list[3:]:
                        file.write(i + '\n')
                else:
                    print('No Content Provided')
        elif flag == '-r':
            with open(in_list[2], 'r') as file:
                for i in file.readlines():
                    print(i, end='')


if check(sys.argv):
    flags(sys.argv)
else:
    print_args(sys.argv)