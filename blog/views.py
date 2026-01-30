from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

# home view
posts: list[dict] = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "First post content!",
        "date_posted": "Jun 24, 2025",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content!",
        "date_posted": "Jul 10, 2025",
    },
]


def home(request) -> HttpResponse:
    posts: QuerySet[Post] = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


# about view
def about(request) -> HttpResponse:
    return render(request, "blog/about.html")
