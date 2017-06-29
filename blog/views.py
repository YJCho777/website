from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
import matplotlib.pyplot as plt
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.#



def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def about(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/about.html', {'posts':posts})

def contact(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/contact.html', {'posts':posts})

def useful_sites(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/useful_sites.html', {'posts':posts})

def finance_econ(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/finance_econ.html', {'posts':posts})

def statistics(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/statistics.html', {'posts':posts})

def computing(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/computing.html', {'posts':posts})

def django_css(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/django_css.html', {'posts':posts})

def stock_market(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/stock_market.html', {'posts':posts})

def simulation(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/simulation.html', {'posts':posts})


#import for ChartData
#views for chartjs 
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas_datareader.data as web
from pandas import Series, DataFrame
from datetime import date
import numpy as np
import datetime 

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        start = datetime.datetime(2010, 1, 1)
        end = date.today()
     
        google = web.DataReader("GOOG", "google", start, end)
        microsoft = web.DataReader("MSFT", "google", start, end)
        amazon = web.DataReader("AMZN ", "google", start, end)
        walmart = web.DataReader("WMT", "google", start, end)
        costco = web.DataReader("COST", "google", start, end)
                
      
        google_close = DataFrame(google, columns = ['Close'])
        microsoft_close = DataFrame(microsoft, columns = ['Close'])
        amazon_close = DataFrame(amazon, columns = ['Close'])
        walmart_close = DataFrame(walmart, columns = ['Close'])
        costco_close = DataFrame(costco, columns = ['Close'])

        
        google_today = DataFrame(google.iloc[[-1]], columns = ['Close'])
        microsoft_today = DataFrame(microsoft.iloc[[-1]], columns = ['Close'])
        amazon_today = DataFrame(amazon.iloc[[-1]], columns = ['Close'])
        walmart_today = DataFrame(walmart.iloc[[-1]], columns = ['Close'])
        costco_today = DataFrame(costco.iloc[[-1]], columns = ['Close'])
        
            
        labels = google.index
        default_items = google_close
        stock_list = ["Google", "Microsoft", "Amazon", "Walmart", "Costco"]
      
        
        data = {
                "stock_list" : stock_list,
                "labels": labels,
                "stock1": google_close,
                "stock2": microsoft_close,
                "stock3": amazon_close,
                "stock4": walmart_close,
                "stock5": costco_close,
                "stock_list" : stock_list,
                "stock_list_price1" : google_today.get_values(),
                "stock_list_price2" : microsoft_today.get_values(),
                "stock_list_price3" : amazon_today.get_values(),
                "stock_list_price4" : walmart_today.get_values(),
                "stock_list_price5" : costco_today.get_values(),      
                "today" : end,                                  
              #  "amazon" : amazon_close,
              #  "walmart" : walmart_close,
              #  "costco" : costco_close,
            }
        return Response(data)
       


