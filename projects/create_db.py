import pandas as pd
import sqlite3

# csv 파일 네 개 수정 완료.


csv_file_path = '/Users/kimdong-keon/Desktop/projects/data/movies_metadata_cleaned.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path, encoding='mac_roman')

conn = sqlite3.connect('/Users/kimdong-keon/Desktop/projects/data/dbfiles/TOTAL.db')  # Replace with your database name
cursor = conn.cursor()

# Step 3: Convert DataFrame to SQL and insert into the database
# You can specify the table name and if_exists parameter (replace, append, fail)
df.to_sql('TOTAL', conn, if_exists='replace', index=False)

# Step 4: Commit the transaction and close the connection
conn.commit()
conn.close()