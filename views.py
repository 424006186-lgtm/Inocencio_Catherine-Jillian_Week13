
from django.shortcuts import render, redirect
from .forms import GuestbookForm
from .models import GuestbookEntry


def guestbook_view(request):

    if request.method == 'POST':
        form = GuestbookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('guestbook')

    else:
        form = GuestbookForm()

    entries = GuestbookEntry.objects.order_by('-created_at')

    return render(request, 'guestbook/guestbook.html', {
        'form': form,
        'entries': entries
    })
