from django.shortcuts import render
import smtplib
import ssl

def index(request):

    if request.method == "POST":
        try:
            name = request.POST.get("name")
            mobileno = request.POST.get("mobileno")
            message = request.POST.get("message")
            context = ssl.create_default_context()
            con = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
            con.ehlo()
            con.login('smartstudysquare@gmail.com', 'avin_9blue')
            con.sendmail('smartstudysquare@gmail.com', 'smartstudysquare@gmail.com',
                         "Subject:Query received\n\n Name :- "+name+"\n MobileNo :- "+str(mobileno)+"\n Message :-"+message)
            return render(request, 'SmartstudySquare/index.html', {})
        except:
            return render(request, 'SmartstudySquare/index.html', {})
    else:
        return render(request, 'SmartstudySquare/index.html', {})
