from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from phonebook.models import Contact, PhoneNo
from phonebook.forms import ContactForm, PhoneNoForm

def contacts(request):
    latest_contact_list = Contact.objects.all().order_by('name')
   
    return render_to_response('phonebook/contacts.html',
    {'latest_contact_list': latest_contact_list,})

def contact_add(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(contacts)

    return render_to_response('phonebook/contact_add.html',
                              {'contact_form': form},
                              context_instance=RequestContext(request))

def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
        contact = form.save()
        contact.save()
        return redirect(contacts)

    return render_to_response('phonebook/contact_edit.html',
                              {'contact_form': form,
                               'contact_id': contact_id},
                              context_instance=RequestContext(request))
                             
def contact_delete(request, contact_id):
    c = Contact.objects.get(pk=contact_id).delete()

    return redirect(contacts)
