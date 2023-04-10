def make_file():
    with open("grades.txt", "w") as my_file:
        print("Popescu Ion;2;5;7", file=my_file)
        print("Ionescu Geta;10;7;9;7", file=my_file)
        print("Georgescu Gelu;4;2", file=my_file)
        print("Radulescu Ioana;5;9;6;4;10", file=my_file)
        print("Vasilescu Vasile;7;8;9;10", file=my_file)
        print("Bengescu Hortensia;10;9;8;9", file=my_file)


def averages():
    x = 'Student'
    y = 'Average'
    z = '-'
    temp = []
    av = []
    with open("grades.txt", "r") as read_file:
        print(f'{x:<50}{y:>5} \n{z * 55}')
        for line in read_file:
            temp.append(str(line).replace(";", ":", 1).replace(";", ",").replace("\n", "").split(':'))
            for element in temp:
                names = element[0]
                grades = element[1].split(',')
                for num in grades:
                    av.append(int(num))
                mean = round(sum(av)/len(av), 1)
                print(f'{names:<50}{mean:>5}')
                av.clear()
            temp.clear()


def averages2():
    w = 'Surname'
    x = 'First Name'
    y = 'Average'
    z = '-'
    nota = 'Grades'
    temp = []
    av = []
    with open("grades.txt", "r") as read_file:
        with open("students.txt", "w") as my_file:
            print(f'{w:<25}{x:<25}{y:>5}{nota:^15} \n{z * 65}', file=my_file)
            for line in read_file:
                temp.append(str(line).replace(";", ":", 1).replace(";", ",").replace("\n", "").split(':'))
                for element in temp:
                    names = element[0].split()
                    grades = element[1].split(',')
                    for num in grades:
                        av.append(int(num))
                    mean = round(sum(av)/len(av), 1)
                    if num:
                        count = len(av)
                    print(f'{names[0]:<25}{names[1]:<25}{mean:>5}{count:^15}', file=my_file)
                    av.clear()
                temp.clear()


def make_sorted_dict():
    # extracts data
    z = '-'
    temp = []
    names = []
    av = []
    values = []
    with open("grades.txt", "r") as read:
        for line in read:
            temp.append(str(line).replace(";", ":", 1).replace(";", ",").replace("\n", "").split(':'))
            for element in temp:
                names.append(element[0])
                grades = element[1].split(',')
                for num in grades:
                    av.append(int(num))
                mean = round(sum(av) / len(av), 1)
                values.append(mean)
                av.clear()
                temp.clear()

    # creates a dictonary

    dc = dict(zip(names, values))
    sorted_values = sorted(dc.values(), reverse=True)
    sorted_dict = {}

    # sorts the dictionary

    for i in sorted_values:
        for k in dc.keys():
            if dc[k] == i:
                sorted_dict[k] = dc[k]

    # prints to file
    it = 1
    with open("Sorted_by_Grades.txt", "w") as write:
        print(f'{"Top 6 in Grade":<25}{"Student":<25}{"Average":>10}\n{z * 60}', file=write)
        for k, v in sorted_dict.items():
            print(f'{it:<25}{k:<25}{v:>10}', file=write)
            it += 1


def choose(x):
    """Multifunction grade sorter.
    Parameters
    ----------
    x: int
    This function groups all the functions into one handy document to use as little code as possible
    """
    if x == 1:
        make_file()
        averages()
    elif x == 2:
        averages2()
    elif x == 3:
        make_sorted_dict()
    else:
        print('Invalid selection.')


if __name__ == '__main__':

    choose(int(input('''Please choose one of the available options
    by typing the corresponding number:
    1 -> Make Initial File
    2 -> Calculate Averages
    3 -> Sort the Students by Grade and Display Top 6 Winners
    
    Please note, options 2-4 will not runn without first running option 1.
    
    Option selected: ''')))
