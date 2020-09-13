from django.shortcuts import render
import mysql.connector as m
    
def home(request):
   return render(request, 'home.html')

def new_page(request):
   print(request.POST.keys())
   name = request.POST['name']
   year = request.POST['year']
   if isinstance(year, int) == False:
       year = 0;
   major = request.POST['major']
   langs = request.POST['langs']
   skills = request.POST['skills']
   hack = request.POST['hack']
   if isinstance(hack, int) == False:
       hack = 0;
   fa = request.POST['fa'] #focus area
   tz = request.POST['tz'] #time zone
   if isinstance(tz, int) == False:
       tz = 0;
   pi = request.POST['pi'] #project idea
   am = request.POST['am'] #about me
   email = request.POST['email'] 
   pw = request.POST['pw']
   

   Host = "35.226.207.58"
   Db = "Perm_Users"
   User = "root"
   Pass = "sjyy"
   db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
   print(db_connect.get_server_info())
   handler = db_connect.cursor()

    #name, year,languages,skills,focus_area,time_zone,project_ideas,hackathon_exp,major,about_me,email,password
   temp = "insert into perm(name, year,languages,skills,focus_area,time_zone,project_ideas,hackathon_exp,major,about_me,email,password) values (" \
       + "\"" + name + "\"," + str(year) + ",\"" + langs + "\",\"" + skills + "\",\"" + fa + "\"," + str(tz) + ",\"" + pi + "\"," + str(hack) + ",\"" + major + "\",\"" + am + "\",\"" + email + "\",\"" + pw + "\")"
   print(temp)
   handler.execute(temp)
   db_connect.commit()
 
   return render(request, 'newpage.html', {})

def post(request):
    print("HERE: ", type(request.Post))