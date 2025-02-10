from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.

# STORE VIEWS

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    queryset = Post.objects.all()
    template_name = "store/index.html"
    paginate_by = 6

def store(request):
    return render(
        request,
        "store/index.html",
    )

# GAMES VIEWS

class GamesList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    queryset = Post.objects.all()
    template_name = "store/games.html"
    paginate_by = 6

def games(request):
    return render(
        request,
        "store/games.html",
    )

# GAMES SEARCHED VIEWS

class GamesSearchedList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    queryset = Post.objects.all()
    template_name = "store/games_searched.html"
    paginate_by = 6

def games_searched(request):
    if request.method == "POST":
        # searched = request.POST['searched']

        return render(request,
            "store/games_searched.html",
            # {"searched": searched}
        )
    else:
        return render(
            request,
            "store/games_searched.html",
        )

# def search_view(request):
#     query = request.GET.get('query', '')
#     results = []

#     if query:
#         results = Post.objects.filter(name__icontains=query)  # Case-insensitive search

#     return render(request, 'search_results.html', {'results': results, 'query': query})

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )

    comment_form = CommentForm()

    return render(
        request,
        "store/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },  
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(request, slug, sender, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created == request.user:
#         messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
#     else:
#         messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

#     return HttpResponseRedirect(reverse('post_detail', args=[slug]))