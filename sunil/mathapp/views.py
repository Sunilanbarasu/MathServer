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
