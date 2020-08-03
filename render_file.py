import pandas as pd
import sqlalchemy
import webbrowser
import os

engine = sqlalchemy.create_engine('mysql+pymysql://root:Radikalfire@localhost/data_of_employees')
df = pd.read_sql_table('employees', engine)
# print(df.head())
html = df.to_html()
from_sql = open('from_sql.html', 'w')
from_sql.write(html)
# url = 'http://localhost:8080/from_sql.html'
# webbrowser.open(url)

path = os.path.abspath('from_sql.html')
url = 'file://' + path
webbrowser.open(url)