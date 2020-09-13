import mysql.connector as m

Host = "35.226.207.58"
Db = "Perm_Users"
User = "root"
Pass = "sjyy"
db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
print(db_connect.get_server_info())
handler = db_connect.cursor()

handler.execute("show databases")
res = handler.fetchall()
for r in res:
    print(r)

#name, year,languages,skills,focus_area,time_zone,project_ideas,hackathon_exp,major,about_me,email,password

handler.execute("select * from perm")
res = handler.fetchall()
for r in res:
    print(r)
    
    
    
    #<label for="team">Looking for a team? y or n:</label>
  #<input type="number" id="team" name="team"><br><br>
  
  covar myObject = {
        "profiles": 
            {{ data }}
        
    };