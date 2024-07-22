import datetime #3,4
from django.http import HttpResponse #3,4,5
from django.template import Template,Context #5
from django.shortcuts import render #5,6
#p3
def currentdt(request):
    now = datetime.datetime.now()
    html = "<p>Current date and time is %s</p>" %now
    return HttpResponse(html)
#p4
def currentdt4(request):
    now=datetime.datetime.now()
    ahead = now + datetime.timedelta(hours = 4)
    behind = now - datetime.timedelta(hours=4)
    html1 = "<p>Current date and time is %s</p>" %now
    html2 = html1 + "<p>4hours ahead date and time is %s</p>" %ahead
    html3 = html2 + "<p>4hours behind date and time is %s</p>" %behind
    return HttpResponse(html3)

#p5
def lists(request):
    fruits = ['apple','banana','orange']
    students = ['anirudh','billy','hinata']
    raw_template = """    
    <ul>
        {% for i in fruits %}
        <li>{{i}}</li>
        {% endfor %}
    </ul>
     <ol>
        {% for i in students %}
        <li>{{i}}</li>
        {% endfor %}
    </ol>

    """
    t = Template(raw_template)
    c = Context({
        'fruits' : fruits,
        'students' : students,
    })

    return HttpResponse(t.render(c))

#p6
def home(request):
    title = "Home"
    name = "FSD"
    return render(request,'home.html',locals())
def about(request):
    title = "About"
    return render(request,'about.html',locals())
def contact(request):
    title = "Contact"
    name= "Anirudh"
    phone= "1234567890"
    email= 'example@gmail.com'
    return render(request,'contact.html',locals())
    

    