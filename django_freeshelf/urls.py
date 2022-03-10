"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from books import views as books_views

urlpatterns = [
    path('', books_views.home, name='home'),
    path('auth/', include('registration.backends.default.urls')),
    path("admin/", admin.site.urls),
    path("books/", books_views.book_list, name='book_list'),
    path('books/<int:pk>/edit/', books_views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', books_views.delete_book, name='delete_book'),
    path('books/<int:pk>/', books_views.book_detail, name='book_detail'),
    path("books/<int:pk>/add_favorite",
            books_views.book_list, name='add_favorite'),
    path('title', books_views.title, name='title'),
    path('newest', books_views.newest, name='newest'),
    path('oldest', books_views.oldest, name='oldest'),
    path('category/<slug:slug>', books_views.category, name="category"),
]
