
from django.shortcuts import render, redirect

from aboutme.models import AboutModel
from services.models import ServiceModel
from skills.models import SkillModel
from sendmessageme.models import  MessageMe, CoderModel, SocialMediaModel, GetInTouch
from .models import Project, Quote

def home_view(request):
    form = AboutModel.objects.all()
    service_context = ServiceModel.objects.all()
    # email = AboutModel.objects.get(email='email')
    skill_context = SkillModel.objects.all()
    coder_context = CoderModel.objects.all()
    socialmedia_context = SocialMediaModel.objects.all()
    getintouch_context = GetInTouch.objects.all()
    project_context = Project.objects.all()
    quote_context = Quote.objects.all()
    print(quote_context)
    # print(request.method)

    return render(request, 'mainport/index.html', {
                            'form'                  :   form,
                            'service_context'       :   service_context,
                            'form'                  :   form,
                            'skill_context'         :   skill_context,
                            'coder_context'         :   coder_context,
                            'socialmedia_context'   :   socialmedia_context,
                            'getintouch_context'    :   getintouch_context,
                            'project_context'       :   project_context,
                            'quote_context'         :   quote_context,    
                            # 'messageme_context'     :   messageme_context,
                        }
                    )

def thank(request):
    # print(request.method)
    # name = request.POST.get('your_name')
    # print(name)
    if request.method == 'POST':
        name = request.POST.get('your_name')
        email = request.POST.get('your_email')
        subject = request.POST.get('your_subject')
        message = request.POST.get('your_message')
        if name == '' and email == '' and subject == '' and message == '':      # If name, email etc has nothing send ValeError try block mean be work as well
            raise ValueError('Fill something then try to send me')
        else:
            contact_me = MessageMe(your_name=name, your_email=email, your_subject=subject, your_message=message)
            contact_me.save()
            contact_me = MessageMe()

            return render(request, 'thank/thankyou.html')
    return redirect('/')