from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Note
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from rest_framework.authtoken.models import Token

from .serializers import NoteSerializer
# Create your views here.

class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner = user)

# to set current logged in as owner
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
        #     # Get or create token for this user
        #     token, created = Token.objects.get_or_create(user=user)
        #     # Return token as JSON
        #     return JsonResponse({'token': token.key})
        # else:
        #     return JsonResponse({'error': 'Invalid credentials'}, status=400)

            return redirect('/api/notes/user/')  # or wherever you want to go after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

    


