from django.shortcuts import render, HttpResponse
from movies.models import Movie, MovieManager
from user.models import User




# gets all movies with owner
def dashboard(request):
    if request.method == "GET":
        # shows all the data from a table
        context = {
            'all_movies': Movie.objects.all()
        }
        return render(request, "dashb.html", context)

# creates one new movie assoc. with one owner
def add_movie(request):
    if request.method == "GET":
        return render(request, "create.html")

    elif request.method == "POST":
        print(request.POST)
        
        user_id = request.user.id

        new_movie = Movie.objects.create(
            title=request.POST['title'],
            release_date=request.POST['release_date'],
            duration=request.POST['duration'],
            description=request.POST['description'],
            owner=User.objects.get(id=user_id)
        )
        return redirect(f'/{new_movie.id}')

# retrieves one movie
def display(request, movie_id):
    context = {
        'movie' : Movie.objects.get(id=movie_id)
    }
    return render(request, "display.html", context)

# updates one movie 
def update_movie(request, movie_id):
    return render(request, "edit.html")

# deletes the movie that is assoc. with one owner
def delete_movie(request):
    pass