from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from booth.models import Booth, Participation
from booth.forms import ParticipationForm
from account.models import User
from django.contrib import messages
# Create your views here.
# Create your views here.

def oc_portal(request):
    if request.user.is_authenticated == False:
        return redirect('/')
    if request.user.user_type == 'student':
        return redirect('/404')
    return render(request, 'oc/oc_portal.html')

def search_profile(request):
    # profile = get_object_or_404(Student, user=request.user)
    template = loader.get_template('oc/search_profile.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("You're voting on question %s." % question_id)


def list_booth(request):
    booths = Booth.objects.filter(booth_admins__in=[request.user])
    # profile = get_object_or_404(Student, user=request.user)
    if len(booths) > 1:
        template = loader.get_template('oc/booth_list.html')
        context = {
            'booths': booths
        }
        return HttpResponse(template.render(context, request))
    if len(booths) == 1:
        return redirect('/oc/booth/{}'.format(booths[0].id))
    else:
        return redirect('404')

def booth_home(request, booth_id):
    booth = get_object_or_404(Booth, id=booth_id)
    request.session['booth'] = booth.id
    template = loader.get_template('oc/booth_home.html')
    context = {
        'booth': booth
    }
    return HttpResponse(template.render(context, request))

def check_player(request, booth_id, user_id=""):
    booth = get_object_or_404(Booth, id=booth_id)
    request.session['booth'] = booth.id
    template = loader.get_template('oc/check_player.html')
    context = {
        'booth': booth
    }
    print(user_id)
    if user_id == "":
        return HttpResponse(template.render(context, request))
    else:
        try:
            user = User.objects.get(id=user_id)
            player = user.player
        except:
            context['message'] = '查無此玩家!'
            return HttpResponse(template.render(context, request))
        qualify = booth.requirement.check_player(player)
        if len(qualify) == 0:
            return redirect('/oc/booth/{}/register/{}'.format(booth.id, user.id))
        else:
            context['message'] = '此玩家不符合資格!'
        return HttpResponse(template.render(context, request))

def register_page(request, booth_id, user_id):
    booth = get_object_or_404(Booth, id=booth_id)
    score_options = [option for option in booth.score_options.all()]
    user = get_object_or_404(User, id=user_id)
    template = loader.get_template('oc/booth_register.html')
    
    context = {
        'booth': booth,
        'user': user,
        'score_options': score_options
    }
    return HttpResponse(template.render(context, request))

def register_player(request, booth_id, user_id, participation=""):
    booth = get_object_or_404(Booth, id=booth_id)
    score_options = [option for option in booth.score_options.all()]
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        print(form)
        if form.is_valid():
            print("VALID FORM")
            new_parti = Participation(
                booth = booth, player=user.player,
            )
            new_parti.save()
            messages.success(request, '成功登記該玩家!')
        else:
            print("INVALID FORM")
    template = loader.get_template('oc/booth_register.html')
    
    context = {
        'booth': booth,
        'user': user,
        'score_options': score_options
    }
    return HttpResponse(template.render(context, request))