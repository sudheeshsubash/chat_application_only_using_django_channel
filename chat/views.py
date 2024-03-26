from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import Room, Message

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        room = request.POST.get('room')
        user = request.POST.get('user')
        if Room.objects.filter(name=room).exists():
            return redirect(f"{room}/?username={user}")
        else:
            Room.objects.create(name=room)
            return redirect(f"{room}/?username={user}")

    

class RomeView(View):
    def get(self, request, room):
        user = request.GET.get('username')
        messages = Message.objects.filter(room=room)
        return render(request, 'roomold.html', {'room':room,'messages':messages,'user':user})
    
    
def send_message(request):
        message = request.POST.get('message')
        user = request.POST.get('user')
        room = request.POST.get('room')
        Message.objects.create(value=message,name=user,room=room)
        return HttpResponse('successfully send message')


def get_messages(request,room):
    messages = Message.objects.filter(room=room)
    return JsonResponse({'messages':list(messages.values())})
