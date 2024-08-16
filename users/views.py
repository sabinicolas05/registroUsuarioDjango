from django.shortcuts import render

from .models import Persona

# Create your views here.


def registerUser(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid:()
            form.save()

    else:
        form = PersonaForm()

    return render(request,
    template_name: 'registroUsuario.html',
    context:{'form':form}
    )
        
       

