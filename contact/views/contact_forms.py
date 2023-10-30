from django.shortcuts import render, redirect

from contact.forms import ContactForm


def create(request):
    # verifica se o método é POST
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context
        )

    # método GET
    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )
