# movie views.py

from django.shortcuts import render, HttpResponse, redirect
from apps.movie.models import Movie
from apps.user.models import User


def dashboard(request):
    # if 'userid' not in request.session:
    #     return redirect('/')
    # experimenting to see if I can use a variable
    # for the 'get all' function
    all_movies = Movie.objects.all()
    
    user_id = request.session['userid']
    user_data = User.objects.get(id = user_id)
    print(user_id)

    
    context = {
        'all_movies' : all_movies,
        'one_user' : user_data
    }
    return render(request, "dash.html", context)



def add_movie(request):
    if request.method == "GET":
        return render(request, "create.html")
    if request.method == "POST":
        # this var is to get the user id from post
        # assuming this is the user in session...
        created_by_id = request.session.get('userid')
        
        this_movie = Movie.objects.create(
            title = request.POST['title'],
            duration = request.POST['duration'],
            description = request.POST['description'],
            released_date = request.POST['released_date'],
            rated = request.POST['rated'],
            created_by = User.objects.get(id = created_by_id),
        )
        print(this_movie)
        return redirect('movies:dashboard')




def display(request, movie_id):
    
    context = {
        'movie': Movie.objects.get(id = movie_id)
    }
    return render(request, 'display.html', context)

def update(request, movie_id):

    this_movie =  Movie.objects.get(id = movie_id)
    # print(this_movie)

    if request.method == 'POST':
        created_by_id = request.session.get('userid')

        this_movie.title = request.POST['title']
        this_movie.duration = request.POST['duration']
        this_movie.description = request.POST['description']
        this_movie.released_date = request.POST['released_date']
        this_movie.rated = request.POST['rated']
        this_movie.created_by = User.objects.get(id = created_by_id)
        this_movie.save()
        print(this_movie)
        return redirect('movies:dashboard')

    context = {
        'movie' : this_movie
    }
    return render(request, 'edit.html', context)


def delete(request, movie_id):
    Movie.objects.get(id = movie_id).delete()
    return redirect('movies:dashboard')





def not_found(request, exception= None):
    return render(request, '404.html', status= 404)