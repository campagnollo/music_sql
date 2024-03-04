import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="3A18Abnranger",
    database="testdatabase"
)
mycursor = db.cursor()

#mycursor.execute('DROP TABLE Albums')

perf = [['The Dead South', 'Canada', 'group'],['Colter Wall', 'Canada', 'solo'],['Trampled by Turtles', 'USA', 'group']
        ,['Ian Noe', 'USA', 'solo'],['Greensky Bluegrass', 'USA', 'group'],['Slaid Cleaves', 'USA', 'solo']]

alb=[[1,'Chains and Stakes',2024],[1,'Good Company',2014],[1,'Sugar and Joy',2019],[1,'Illusion and Doubt',2016],[1,'The Ocean Went Mad and We Were to Blame',2013],
     [3,'Life is good on the open Road',2018],[3,'Wild Animals',2014],[3,'Stars and Satellites',2012],[3,'Palomino',2010],[3,'Duluth',2008],
     [2,'Little Songs',2023],[2,'Song of the Plains',2018],[2,'Colter Wall', 2017],[2,'Imaginary Appalachia',2015],
     [4,'River Fools and Mountain Saints',2022], [4,'Between the Country',2019],[4,'Off this Mountaintop', 2017]]

alb2=[[5,'Stress Dreams',2022],[5,'All for Money',2019],[5,'Shouted, Written Down and Quoted',2016],[5,'If Sorrows Swim',2014],
      [6,'Together Through the Dark',2023], [6,'Ghost on the Car Radio',2017], [6,'Still Fighting the War',2013]]


Q1='CREATE TABLE Performers (perfid INT PRIMARY KEY AUTO_INCREMENT, ' \
   'perfname VARCHAR(50), country VARCHAR(50), ensemble ENUM("group","solo"))'

Q2='CREATE TABLE Albums (albid INT PRIMARY KEY AUTO_INCREMENT, perfid INT, ' \
   'FOREIGN KEY(perfid) REFERENCES Performers(perfid), albname VARCHAR(50),year INT)'

# mycursor.execute(Q2)
# for x in perf:
#     mycursor.execute('INSERT INTO Performers(perfname, country, ensemble) VALUES (%s, %s, %s)',tuple(x))
for x in alb2:
    mycursor.execute('INSERT INTO Albums(perfid, albname, year) VALUES (%s, %s, %s)', tuple(x))
db.commit()
#mycursor.execute('SELECT * FROM Albums')
mycursor.execute('SELECT * FROM Performers')
results=mycursor.fetchall()
for x in results:
    print(x)
print('\n\n')
mycursor.execute('SELECT perfname, albname FROM Performers INNER JOIN Albums ON Performers.perfid = Albums.perfid WHERE Performers.country="Canada"')
results=mycursor.fetchall()
for x in results:
    print(x)
