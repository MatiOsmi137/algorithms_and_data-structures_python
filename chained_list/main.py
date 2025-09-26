import datetime as dt


class Contact:
    def __init__(self, cid=None, birthday=None, first_name=None, last_name=None):
        self.cid = cid
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.cid + ", " + self.birthday.strftime("%d.%m.%Y") + "(" + str(
            calc_day_of_year(self.birthday)) + ") " + \
            self.first_name + " " + self.last_name


DATA_FILE = "data.csv"


def read_contacts(n):
    file = open(DATA_FILE, "r")
    contactlist = []
    lineCounter = 0
    for line in file.readlines():
        values = [x.strip() for x in line.split(";")[:-1]]
        birthday = dt.datetime.strptime(values[3], "%d.%m.%Y").date()
        contactlist.append(Contact(cid=values[0], birthday=birthday, first_name=values[1], last_name=values[2]))
        lineCounter += 1
        if lineCounter == n:
            return contactlist


HASH_TABLE_SIZE = 20
hash_table = [None] * HASH_TABLE_SIZE
DELETED = object()  # Markiert die gelöschten Elemente


def calc_day_of_year(date):
    return date.timetuple().tm_yday


def put_linear_probing(contact):
    hash_value = calc_hash_value(contact.birthday)
    original_hash_value = hash_value
    while hash_table[hash_value] is not None and hash_table[hash_value] is not DELETED:
        hash_value = (hash_value + 1) % HASH_TABLE_SIZE
        if hash_value == original_hash_value:
            raise Exception("Hash table is full")
    hash_table[hash_value] = contact


def get_linear_probing(day, month, year):
    d = dt.datetime(year=year, month=month, day=day).date()
    hash_value = calc_hash_value(d)
    original_hash_value = hash_value
    while hash_table[hash_value] is not None:
        if hash_table[hash_value] is not DELETED and hash_table[hash_value].birthday == d:
            return hash_table[hash_value]
        hash_value = (hash_value + 1) % HASH_TABLE_SIZE
        if hash_value == original_hash_value:
            return None
    return None


def delete_linear_probing(day, month, year):
    d = dt.datetime(year=year, month=month, day=day).date()
    hash_value = calc_hash_value(d)
    original_hash_value = hash_value
    while hash_table[hash_value] is not None:
        if hash_table[hash_value] is not DELETED and hash_table[hash_value].birthday == d:
            hash_table[hash_value] = DELETED
            return True
        hash_value = (hash_value + 1) % HASH_TABLE_SIZE
        if hash_value == original_hash_value:
            return False
    return False


def print_table():
    for i in range(len(hash_table)):
        if hash_table[i] is None:
            print(str(i) + ": None")
        elif hash_table[i] is DELETED:
            print(str(i) + ": DELETED")
        else:
            print(str(i) + ": " + str(hash_table[i]))


def calc_hash_value(date):
    return calc_day_of_year(date) % HASH_TABLE_SIZE


n = 20

# Example usage
contacts = read_contacts(n)
for contact in contacts:
    put_linear_probing(contact)

print_table()

print("\nDeleting contact ...\n")
delete_linear_probing(26, 12, 1950)

print_table()

if __name__ == '__main__':
    contacts = read_contacts(n)
    for c in contacts[:20]:
        print(c)

    print_table()
