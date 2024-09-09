import pyodbc
import os

SERVER = '10.0.100.20'
DATABASE = 'DEV_Econo'
USERNAME = 'DEVPython'
#PASSWORD = os.environ['MotDePassePourLaBD'] # variable d'environnement initiallisé dans la configuration du poste/serveur...
PASSWORD = 'cP7fae+iA06XcEHccC$%0TtLWl$?XV7JhqZQKnC'  # ne jamais mettre le mot de passe en clair dans le code. Utiliser une variable d'environnement.

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString) 


SQL_QUERY = """
SELECT 	Code_marche,
    dern_lecture,
	count(Date_lecture)  as NbLecture
FROM Marche 
left outer join Val_Marche
on Marche.Id_Marche = Val_Marche.Id_Marche
group by Code_marche,dern_lecture
Order by NbLecture desc;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.Code_marche}\t{r.NbLecture}\t{r.dern_lecture}")

    