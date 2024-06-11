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

# 2번
def generation_movie(year):
    conn = sqlite3.connect('data/dbfiles/TOTAL.db')
    cur = conn.cursor()
    start_date = "19{}-01-01".format(year)
    end_date = "19{}9-12-31".format(year)
    cur.execute(
        f"""
            SELECT id, original_title FROM TOTAL WHERE release_date BETWEEN '{start_date}' AND '{end_date}' 
        """
    )
    answer = []
    results = cur.fetchall()
    temp = tuple([i[0] for i in results])

    conn = sqlite3.connect('data/dbfiles/RATINGS_6_11.db')
    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM rating WHERE userId IN {} order by rating DESC".format(temp)
    )
    results = cur.fetchall()

    conn = sqlite3.connect('data/dbfiles/TOTAL.db')
    cur = conn.cursor()
    for i in range(10):
        cur.execute(
            "SELECT original_title FROM TOTAL WHERE id = {}".format(results[i][1]))
        result = cur.fetchall()
        if result:
            # print(result[0][0])
            answer.append(result[0][0])
    return answer