from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from .forms import *
from .models import *
from .functions import *

@login_required
def home(request):
    context = {}
    return render(request, 'dashboard/home.html', context)

@login_required
def profile(request):

    context = {}
    
    if request.method == 'GET':
        form = ProfileForm(instance=request.user.profile)
        context['form'] = form
        return render(request, 'dashboard/profile.html', context)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
             
    return render(request, 'dashboard/profile.html', context)

def blogTopic(request):
    context = {}

    if request.method == 'POST':
        blogidea = request.POST['blogidea']
        keywords = request.POST['keywords']

        blogTopics = generateBlogTopicIdeas(blogidea, keywords)
        if len(blogTopics) > 0:
            request.session['blogTopics'] = blogTopics
            return redirect('blog-sections')
        else:
            messages.error(request, "Try again we coundn't get any topics for you")
            return redirect('blog-topic')


    return render(request, 'dashboard/blog_topic.html', context)



def blogSections(request):
    if 'blogTopics' in request.session:
        pass
    else:
        messages.error(request, "Start by entering a blog idea and keywords")
        return redirect('blog-sections')
    
    context = {}
    context['blogTopics'] = request.session['blogTopics']

    return render(request, 'dashboard/blog_section.html', context)



def ieltsAssistant(request):
    context = {}

    if request.method == 'POST':
        blogidea = request.POST['blogidea']
        keywords = request.POST['keywords']

        blogTopics = ieltsWritingEvaluation(blogidea, keywords)
        if len(blogTopics) > 0:
            request.session['blogTopics'] = blogTopics
            return redirect('ielts-writing')
        else:
            messages.error(request, "Try again we coundn't get any topics for you")
            return redirect('blog-topic')


    return render(request, 'dashboard/ielts_assistant.html', context)



def ieltsWriting(request):
    if 'blogTopics' in request.session:
        pass
    else:
        messages.error(request, "Start by entering a blog idea and keywords")
        return redirect('ielts-writing')
    
    context = {}
    context['blogTopics'] = request.session['blogTopics']

    return render(request, 'dashboard/ielts_writing.html', context)


