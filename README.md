# Ex.05 Design a Website for Server Side Processing
## Date:28-11-2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html


<html>
<head>
    <style>

.edge
 { display: block;
    margin-top: 400px;
    margin-bottom: auto;
    margin-left: auto;
    margin-right: auto;
    border-style: dashed;
    border-color: rgba(197, 14, 38, 0.816);
   background-color: rgb(180, 228, 35);
    padding-top: 70px;
    padding-right: 50px;
    padding-bottom: 60px;
    padding-left: 70px;
    width: 25%;
    flex-direction: column;
    
  }
  body{
    background-color: rgba(159, 6, 6, 0.881);
  }
div.formelt
{
    font-size: 150%;
   color: red;
  
    
}
div.box
{
  color: rgb(100, 39, 11);
  text-align: center;
  font-style: unset;
  background-color: yellow;
  
}
input
{
  padding: 15px;
  border: 2px solid;
  border-radius: 10px;
  width: 30%;
  align-items: center;
}
    </style>
</head>
<body>
    <div class="edge">
        <div class="box">
            <h1>POWER OF A LAMP FILAMENT</h1>
            <h2>Sunil A (24900526)</h2>
            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
                    <br>
                    Intensity : <input type="text" name="Intensity" value="{{I}}"> (in W/m<sup>2</sup>)<br>
                </div>
                <div class="formelt">
                    <br>
                    Resistance : <input type="text" name="Resistance" value="{{R}}"> (in ohm)<br>
                </div>
                <div class="formelt">
                    <br>
                    <input type="submit" value="Calculate"><br>
                </div>
                <div class="formelt">
                    <br>
                    Power : <input type="text" name="power" value="{{power}}"> (in watt)<br>
                </div>
            </form>
        </div>
    </div>
</body>
</html>


views.py


from django.shortcuts import render 
def powerbulb(request): 
    context={} 
    context['power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('Intensity','0')
        R = request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        power = (int(I) * int(I))*int(R)
        context['power'] = power 
        context['I'] = I
        context['R'] = R
        print('power=',power) 
    return render(request,'mathapp/math.html',context)


urls.py


from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerofalamp/',views.powerbulb,name="powerofalamp"),
    path('',views.powerbulb,name="powerofalamp")
]

```


## SERVER SIDE PROCESSING:
![alt text](2(.).png)

## HOMEPAGE:
![alt text](1(.).png)

## RESULT:
The program for performing server side processing is completed successfully.
