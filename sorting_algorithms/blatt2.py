import os.path
import re
import time
import math

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
    rand_files = [f for f in files if (re.compile('rand(1|2|4|8|16|32|64|128|256|512)([kM])\\.txt')).match(f)]
    if len(rand_files) != 16:
        raise Exception('Einige oder alle Datenfiles können nicht gefunden werden!')


def run_sort_and_print_time(filename_or_arr):
    if type(filename_or_arr) is str:
        filename = filename_or_arr
        arr = read_file_into_array(filename)
        start = time.time()
        sort(arr)
        end = time.time()
        print(filename + ':', end - start, 's')
    else:
        arr = filename_or_arr
        arr = sort(arr)
        return arr


# global b_arr definition
b_arr = []


def fuegezusammen(arr, l, m, r):
    # TODO: Sortieralgorithmus hier implementieren
    i = l
    j = m + 1
    k = l
    b_arr = [0]*len(arr)

    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            b_arr[k] = arr[i]
            i += 1
        else:
            b_arr[k] = arr[j]
            j += 1
        k += 1
    if i > m:
        for h in range(j, r+1):
            b_arr[k + h - j] = arr[h]
    else:
        for h in range(i, m+1):
            b_arr[k + h - i] = arr[h]
    for h in range(l, r+1):
        arr[h] = b_arr[h]


def abrunden(x):
    if x - math.ceil(x) >= 0.5:
        return x+1
    else:
        return x

def sortiere(arr, l, r):
    if l < r:
        m = (l + r) // 2
        sortiere(arr, l, m)
        sortiere(arr, m + 1, r)
        fuegezusammen(arr, l, m, r)


def sort(arr):
    # Hier gibts nichts zu tun!

    # Initialisierung des globalen Hilfsarrays B
    global b_arr
    b_arr = [None] * len(arr)

    # erster Aufruf der rekursiven Funktion sortiere
    sortiere(arr, 0, len(arr) - 1)

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

        run_sort_and_print_time(DATA_DIR + '/rand1k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand2k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand4k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand8k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand16k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand32k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand64k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand128k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand256k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand512k.txt')
        run_sort_and_print_time(DATA_DIR + '/rand1M.txt')
        run_sort_and_print_time(DATA_DIR + '/rand2M.txt')
        run_sort_and_print_time(DATA_DIR + '/rand4M.txt')
        run_sort_and_print_time(DATA_DIR + '/rand8M.txt')
        run_sort_and_print_time(DATA_DIR + '/rand16M.txt')
        run_sort_and_print_time(DATA_DIR + '/rand32M.txt')
