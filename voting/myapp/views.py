from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages as msg
from .models import *

# Create your views here.
def home(request):
    if (request.session.get('active_login')):
        return redirect('vote_machine')
    return render(request,'login.html')

def ajax(request):
    if request.method == "POST":
        ex = voter.objects.filter(voter_no = request.POST.get("v_no"),phone= request.POST.get("phone"))
        request.session['id'] = ex[0].voter_no
        request.session['name'] = ex[0].name
        request.session['active_login'] = True
        return JsonResponse({'data':ex.count()})
    else:
        return HttpResponse("Error")


def vote_machine(request):
    if(request.session.get('active_login')):
        if(vote_box.objects.filter(voter_id = voter.objects.get(voter_no=  request.session.get('id'))).count() > 0):
            return redirect('set_vote')
        context ={
            'party':parties.objects.all(),
        }
        return render(request,'home.html',context)
    else:
        return redirect('home')
   
    
def set_vote(request):
    if request.method == "POST":
        p = parties.objects.get(id=request.POST.get("id"))
        q = voter.objects.get(voter_no=request.session.get("id"))
        s1 = vote_box(vote_id=p,voter_id=q)
        s1.save()
        del request.session['id']
        del request.session['name']
        del request.session['active_login']
        return JsonResponse({'working':1})
    else:
        del request.session['id']
        del request.session['name']
        del request.session['active_login']
        msg.warning(request,'Your Vote Already Submited!')
        return redirect('home')
def win_election(request):
    di = {}
    mac=[]
    for id in parties.objects.all():
        di[id.party_name] = vote_box.objects.filter(vote_id=id).count()
        mac.append(vote_box.objects.filter(vote_id=id).count())
    context ={
        'data':di,
    }
    return render(request,'win_election.html',context)
    

