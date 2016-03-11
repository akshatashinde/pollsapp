from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from notes.models import Note,Tag
from notes.forms import NoteForm, TagForm
from django.utils.text import slugify
# Create your views here.
def index(request):
	return HttpResponse("Hello")


def home_view(request):
	# if not request.user.is_authenticated():
		if request.method == 'POST':
			username = request.POST.get('username', None)
			password = request.POST.get('password', None)

			auth = authenticate(username=username, password=password)
			if auth is not None:
				login(request, auth)
				return HttpResponseRedirect(reverse('notes:index'))
			else:
				messages.add_message(request, messages.INFO, "Authentication Failed!")
				return HttpResponseRedirect(reverse('home'))
	# else:
	# 	return HttpResponseRedirect(reverse('notes:index'))		

		return render(request, 'notes/home.html', {})

def index_view(request):
	notes = Note.objects.all().order_by('-timestamp')
	tags = Tag.objects.all()
	return render(request, 'notes/index.html', {'notes': notes, 'tags':tags})	

def add_note(request):

	id = request.GET.get('id', None)
	if id is not None:
		note = get_object_or_404(Note, id=id)
	else:
		note = None

	if request.method == 'POST':
		if request.POST.get('control') == 'delete':
			note.delete()
			messages.add_message(request, messages.INFO, 'Note Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))

		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Note Added!')
			return HttpResponseRedirect(reverse('notes:index'))

	else:
			form = NoteForm(instance=note)

	return render(request, 'notes/addnote.html', {'form':form, 'note':note})	

def add_tag(request):
	id = request.GET.get('id', None)
	if id is not None:
		tag = get_object_or_404(Tag, id=id)
	else:
		tag = None
	
	if request.method == 'POST':
		if request.POST.get('control') == 'delete':
			tag.delete()
			messages.add_message(request, messages.INFO, 'Tag Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))
		
		form = TagForm(request.POST, instance=tag)
		if form.is_valid():
			t = form.save(commit=false)
			t.slug = slugify(t.label)
			t.save()
			messages.add_message(request, messages.INFO, 'Tag Added!')
			return HttpResponseRedirect(reverse('notes:index'))
	
	else:
		form = TagForm(instance=tag)
		
	return render(request, 'notes/addtag.html', {'form':form, 'tag':tag})	
		

def tag_search(request, **kwargs):
	slug = kwargs['slug']
	tag = get_object_or_404(Tag,slug=slug)
	notes = tag.notes.all()

	return render(request, 'notes/tagsearch.html', {'notes':notes, 'tag':tag})