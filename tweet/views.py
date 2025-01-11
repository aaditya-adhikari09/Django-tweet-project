from django.shortcuts import render ,redirect ,HttpResponse
from .models import Tweet
from .forms import TweetForm 
from django.shortcuts import get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def tweet(request): 
    return render(request ,'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')    
    return render(request ,'tweet_list.html',{'tweets':tweets})
    return HttpResponse('this page is working')

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)  
            tweet.user = request.user 
            form.save()  
            return redirect('tweet_list')  # Redirect to the tweet list after saving
        else:
            return render(request, 'create.html', {'form': form})  # Re-render the form with errors

    else :
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()  # Save the updated tweet
            return redirect('tweet_list')  # Redirect to the tweet list after saving
    else:
        # For a GET request, initialize the form with the current instance
        form = TweetForm(instance=tweet)
    
    return render(request, 'edit_tweet.html', {'form': form, 'tweet': tweet})

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id,user= request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def tweet_post(request):
    return HttpResponse('this is tweetpost') 



def register(request):
    return render(request,'registration/register.html')