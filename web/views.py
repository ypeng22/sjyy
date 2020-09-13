from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as m
    
def signup(request):
   #sesh = request.session.get('num_visits', 0)
   #request.session['num_visits'] = sesh + 1
   return render(request, 'signup.html', {})

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
   temp = "insert into perm(name, year,languages,skills,focus_area,time_zone,project_ideas,hackathon_exp,major,about_me,email,password, admin) values (" \
       + "\"" + name + "\"," + str(year) + ",\"" + langs + "\",\"" + skills + "\",\"" + fa + "\"," + str(tz) + ",\"" + pi + "\"," + str(hack) + ",\"" + major + "\",\"" + am + "\",\"" + email + "\",\"" + pw + "\",\'n\')"
   print(temp)
   handler.execute(temp)
   db_connect.commit()
 
   return render(request, 'newpage.html', {})

def login(request):
    return render(request, 'login.html', {})

def home(request):
    email = request.session.get('emaillogin', None)
    return render(request, 'home.html', {'email':email})
    
def login_res(request):
    email = request.POST['email']
    pw = request.POST['pw']

    Host = "35.226.207.58"
    Db = "Perm_Users"
    User = "root"
    Pass = "sjyy"
    db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
    handler = db_connect.cursor()
    temp = "select admin from perm where email=\"" + email + "\" and password = \"" + pw + "\""
    handler.execute(temp)
    res = handler.fetchall()
    if len(res) == 0:
        return HttpResponse("invalid login")
    if res[0][0] == 'n':
        request.session['emaillogin'] = email
        return render(request, 'home.html', {'email':email})   
    elif res[0][0] == 'y':
        request.session['emaillogin'] = email
        return render(request, 'organizer.html', {'email':email})   
    else:
        return HttpResponse("invalid login")
    
def logout(request):
    request.session['emaillogin'] = None
    print("here")
    return render(request, 'home.html', {})

def events(request):
    return render(request, 'home.html', {})

def confirm(request):
    email = request.session.get('emaillogin', None)
    if email == None:
        return HttpResponse("log in first")
    en = request.POST['event_name']
    Host = "35.226.207.58"
    Db = "Perm_Users"
    User = "root"
    Pass = "sjyy"
    db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
    handler = db_connect.cursor()
    temp = "select * from perm where email=\"" + email + "\""
    handler.execute(temp)
    res = handler.fetchall()
    for i in range(len(res[0])):
        print(res[0][i])
    name = res[0][0]
    year = res[0][1]
    langs = res[0][2]
    skills = res[0][3]
    fa = res[0][4]
    tz = res[0][5]
    pi = res[0][6]
    hack = res[0][7]
    major = res[0][8]
    am = res[0][9]
    password = res[0][11]
    return render(request, 'confirm.html', {'en':en, 'password': password, 'email': email, 'name':name, 'year':year, 'langs':langs, 'skills':skills, 'fa':fa, 'tz':tz, 'pi':pi, 'hack':hack, 'major':major, 'am':am, })

def create(request):
    name = request.POST['create_name']
    Host = "35.226.207.58"
    Db = "Perm_Users"
    User = "root"
    Pass = "sjyy"
    db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
    handler = db_connect.cursor()
    temp = "CREATE TABLE " + name + " LIKE perm"
    handler.execute(temp)
    temp1 = "alter table " + name + " drop column password" 
    handler.execute(temp1)
    temp3 = "alter table " + name + " drop column admin" 
    handler.execute(temp3)
    temp2 = "alter table " + name + " add column team varchar(1)" #y or n 
    handler.execute(temp2)
    db_connect.commit()
    return HttpResponse("event created!")

def search(request):
    name = request.POST['event_name']
    Host = "35.226.207.58"
    Db = "Perm_Users"
    User = "root"
    Pass = "sjyy"
    db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
    handler = db_connect.cursor()
    temp = "select * from " + name
    handler.execute(temp)
    res = handler.fetchall()
    return render(request, 'participant_viewer.html', {'data': res[0], 'event_name':name})

def reg(request):
    email = request.session.get('emaillogin', None)
    name = request.POST['en']
    Host = "35.226.207.58"
    Db = "Perm_Users"
    User = "root"
    Pass = "sjyy"
    db_connect = m.connect(host=Host, database=Db, user=User, password=Pass)
    print(db_connect.get_server_info())
    handler = db_connect.cursor()
    temp = "insert into " + name + " (name, year,languages,skills,focus_area,time_zone,project_ideas,hackathon_exp,major,about_me,email) select name, year, languages, skills, focus_area, time_zone, project_ideas, hackathon_exp ,major, about_me, email from perm where email=\"" + email + "\""        
    handler.execute(temp)
    db_connect.commit()
    return HttpResponse("enrolled!")

    