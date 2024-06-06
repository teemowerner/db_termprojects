import sqlite3, os
print(os.getcwd())
# cast -> `cast` 함수 #### 조심 #####
# cast, crew, id 가 column
def actor_info(actor):
    conn = sqlite3.connect('data/dbfiles/CREDITS.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM CREDITS WHERE `cast` LIKE ?",
        ('%' + actor + '%',)
    )
    results = cur.fetchall()
    temp = tuple([i[-1] for i in results])
    # print(temp)
    conn = sqlite3.connect('data/dbfiles/TOTAL.db')

    cur = conn.cursor()
    cur.execute(
        "SELECT title FROM TOTAL WHERE id IN {}".format(temp)
    )
    results = cur.fetchall()
    return(results)

# print(actor_info("TOM CRUISE"))


# conn = sqlite3.connect('LINKS.db')
# cur = conn.cursor()
# cur.excute('SELECT movieID WHERE movieID ='+)
# cur.execute("SELECT * FROM CREDITS WHERE cast LIKE ?", ('%TOM CRUISE%',))

# def actor_info(actor):
#     conn = sqlite3.connect('CREDITS.db')
#     cur = conn.cursor()
#     cur.execute(
#     """
#     SELECT id FROM CREDITS WHERE `cast` LIKE '%TOM CRUISE%'
#     """
#     )
#     results = cur.fetchall()
#     temp = tuple([i[-1] for i in results])
#     print(temp)
#     conn = sqlite3.connect('TOTAL.db')

#     cur = conn.cursor()
#     cur.execute(
#         "SELECT title FROM TOTAL WHERE id IN {}".format(temp)
#     )
#     results = cur.fetchall()
#     print(results)
