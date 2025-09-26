import os.path
import re
import time

DATA_DIR = 'data'


def read_file_into_array(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    arr = [int(n) for n in lines]
    return arr


def check_env(pathname):
    if not os.path.exists(pathname):
        raise Exception('Datenverzeichnis kann nicht gefunden werden!')
    files = os.listdir(pathname)
    asc_files = [f for f in files if (re.compile('asc(1|2|4|8|16|32|64)k\\.txt')).match(f)]
    desc_files = [f for f in files if (re.compile('desc(1|2|4|8|16|32|64)k\\.txt')).match(f)]
    rand_files = [f for f in files if (re.compile('rand(1|2|4|8|16|32|64)k\\.txt')).match(f)]
    if len(asc_files) != 7 or len(desc_files) != 7 or len(rand_files) != 7:
        raise Exception('Einige oder alle Datenfiles können nicht gefunden werden!')


def run_sort_and_print_time(filename_or_arr):
    if type(filename_or_arr) is str:
        arr = read_file_into_array(filename_or_arr)
        start = time.time()
        sort(arr)
        end = time.time()
        print(filename_or_arr + ':', end - start, 's')
    else:
        return sort(filename_or_arr)


def sort(arr):

    # Sortieralgorithmus hier implementieren!
    for j in range(0, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr


if __name__ == "__main__":

    check_env(DATA_DIR)

    test_arr = run_sort_and_print_time([9, 2, 3, 2, 1, 7, 5, 9])

    print('soll: [1, 2, 2, 3, 5, 7, 9, 9]')
    print('ist:  ' + str(test_arr))

    if test_arr != [1, 2, 2, 3, 5, 7, 9, 9]:
        print('Deine Implementierung scheint NICHT zu funktionieren oder noch nicht fertig zu sein.\n'
              'Überprüfe die sort Funktion!')

    else:
        print('Deine Implementierung scheint zu funktionieren! :-) \n'
              'Weiter mit den Datenfiles...\n')
        print('Sortiere:')
        run_sort_and_print_time(DATA_DIR + '/desc1k.txt')
        run_sort_and_print_time(DATA_DIR + '/desc2k.txt')
        run_sort_and_print_time(DATA_DIR + '/desc4k.txt')
        run_sort_and_print_time(DATA_DIR + '/desc8k.txt')
        run_sort_and_print_time(DATA_DIR + '/desc16k.txt')
        run_sort_and_print_time(DATA_DIR + '/desc32k.txt')
        run_sort_and_print_time(DATA_DIR + '/desc64k.txt')

        run_sort_and_print_time(DATA_DIR + '/asc1k.txt')
        run_sort_and_print_time(DATA_DIR + '/asc2k.txt')
        run_sort_and_print_time(DATA_DIR + '/asc4k.txt')
        run_sort_and_print_time(DATA_DIR + '/asc8k.txt')
        run_sort_and_print_time(DATA_DIR + '/asc16k.txt')
        run_sort_and_print_time(DATA_DIR + '/asc32k.txt')
        run_sort_and_print_time(DATA_DIR + '/asc64k.txt')

        run_sort_and_print_time(DATA_DIR + '/rand1k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand2k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand4k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand8k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand16k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand32k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand64k.txt')
