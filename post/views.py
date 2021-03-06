from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Tweet
from cloudinary.forms import cl_init_js_callbacks;

def index(request,):
    all_Tweet = Tweet.objects.order_by('-created_at').filter(parent_tweet_id=None)
    for tweet in all_Tweet:
        tweet.replycount = Tweet.objects.filter(parent_tweet_id=tweet.id).count()

    content = {
        'tweets': all_Tweet,
    }

    return render(request, 'tweet/home.html', content)

def reply(request, id):
    if request.POST:
        name = request.POST.get('name')
        text = request.POST.get('text')
        image = request.FILES.get('image_upload')

        t = Tweet(name=name, content=text, image_path=image, parent_tweet_id=id)
        t.save()
        return HttpResponseRedirect(reverse('home'))
    tweetcontent = Tweet.objects.get(id=id)
    tweetreply = Tweet.objects.filter(parent_tweet_id=id)
    tweetreplycount = Tweet.objects.filter(parent_tweet_id=id).count()
    content = {
        'tweetcontent': tweetcontent,
        'replycomment': tweetreply,
        'replycount': tweetreplycount
    }
    return render(request, 'tweet/reply.html', content)

def post(request):
    if request.POST:
        name = request.POST.get('name')
        text = request.POST.get('text')
        image = request.FILES.get('image_upload')

        t = Tweet(name=name, content=text, image_path=image )
        t.save()
        return HttpResponseRedirect(reverse('home'))


def detail(request, id):
    if request.POST:
        name = request.POST.get('name')
        text = request.POST.get('text')
        image = request.FILES.get('image_upload')
        if image:
            with open('images' + str(image), 'wb+') as destination:
                for chunk in image.chunk():
                    destination.write(chunk)
            imageurl = 'images/' + str(image)
        else:
            imageurl = None
        t = Tweet(name=name, content=text, image_path=imageurl)
        t.save()

    tweetcontent = Tweet.objects.get(id=id)
    tweetreply = Tweet.objects.filter(parent_tweet_id=id)
    tweetreplycount = Tweet.objects.filter(parent_tweet_id=id).count()

    content = {
        'tweetcontent' : tweetcontent,
        'replycomment' : tweetreply,
        'replycount' : tweetreplycount,

    }
    return render(request, 'tweet/tweet-detail.html', content)

def tweet_delete(request, id):
    tweets = get_object_or_404(Tweet, id=id)
    if request.method == 'POST':
        tweets.delete()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'tweet/home.html')


