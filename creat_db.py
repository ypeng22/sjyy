#create temporary databasefor a hackathon
#input is name, set right now as test_table_1 for testing purposes
import mysql.connector as m

Host = "35.226.207.58"
Db = "Perm_Users"
User = "root"
Pass = "sjyy"
name = "test_table_1" #param
db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
print(db_connect.get_server_info())
handler = db_connect.cursor()
temp = "CREATE TABLE " + name + " LIKE perm"
handler.execute(temp)
temp1 = "alter table " + name + " drop column password" 
handler.execute(temp1)

temp2 = "alter table " + name + " add column team varchar(1)" #y or n 
handler.execute(temp1)
db_connect.commit()


#add student to a temp db
#email and name should be input if this is the function
import mysql.connector as m

Host = "35.226.207.58"
Db = "Perm_Users"
User = "root"
Pass = "sjyy"
name = "test_table_1" #param
email = "ypeng22@jh.edu" #param
db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
print(db_connect.get_server_info())
handler = db_connect.cursor()
temp = "insert into " + name + " (name, year,languages,skills,focus_area,time_zone,project_ideas,hackathon_exp,major,about_me,email) select name, year, languages, skills, focus_area, time_zone, project_ideas, hackathon_exp ,major, about_me, email from perm where email=\"" + email + "\""        
handler.execute(temp)
db_connect.commit()


#querry database and sort by #
import mysql.connector as m
import numpy as np

Host = "35.226.207.58"
Db = "Perm_Users"
User = "root"
Pass = "sjyy"
sorts = {"name": ['bob'], "major": ['cs'] } #param
name = 'test_table_1' #param
sort_by = list(sorts.keys())

db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
print(db_connect.get_server_info())
handler = db_connect.cursor()
temp = "select * from " + name + " where "
i = 0
for s in sort_by:
    for v in sorts[s]:
        if i != 0:
            temp += " and "
        i += 1
        temp = temp + s + " like \'%" + v + "%\'"
handler.execute(temp)
#db_connect.commit()
res = handler.fetchall()
for r in res:
    print(r)