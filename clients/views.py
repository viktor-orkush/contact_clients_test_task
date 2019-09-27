from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from clients.forms import ClientForm
from clients.models import Client


def all_clients(request):
    clients = Client.objects.all()
    return render(request, 'all_clients.html', {'clients': clients})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_clients')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


def edit_client(request, id_client):
    client = get_object_or_404(Client, id=id_client)
    form = ClientForm(request.POST or None, instance=client)
    if request.method == 'POST':
        if form.is_valid():
            obj_client = form.save(commit=False)
            obj_client.save()
            # TODO dont show successfully message
            messages.success(request, "You successfully updated the clint's information contacts")
            return redirect('all_clients')
        else:
            return render(request, 'edit_client.html',
                          {'form': form,
                           'error': 'The form was not updated successfully. '
                                    'Please enter correct information'})
    else:
        return render(request, 'edit_client.html', {'form': form})


