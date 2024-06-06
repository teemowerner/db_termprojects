import csv, sqlite3


## .db 파일을 생성
conn = sqlite3.connect('/Users/kimdong-keon/Desktop/projects/customer.db')
cur = conn.cursor()
conn.close

with open('/Users/kimdong-keon/Desktop/projects/archive/shopping_trends.csv', mode='r', encoding='UTF-8') as f:
    dr = csv.DictReader(f)
    # temp = [(i['Customer ID'], i['Age']) for i in dr]
    temp = [i for i in dr]
    keys_list = temp[0].keys()
    for i in range(3):
        print(temp[i])




    # print(temp[1]['Customer ID'])