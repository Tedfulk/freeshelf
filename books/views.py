from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    if request.user.is_authenticated:
        return redirect("book_list")
    return render(request, "home.html")


@login_required
def title(request):
    title = Book.objects.order_by('title')
    context = {'books': title}
    return render(request, "book_list.html", context)


@login_required
def newest(request):
    newest = Book.objects.order_by('-created_at')
    context = {'books': newest}
    return render(request, "book_list.html", context)


@login_required
def oldest(request):
    books = Book.objects.order_by('created_at')
    context = {'books': books}
    return render(request, "book_list.html", context)


@login_required
def book_list(request):
    books = Book.objects.all()
    categorys = Category.objects.all()
    return render(request, "book_list.html", {"books": books, "categorys": categorys})


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    return render(
        request,
        "book_detail.html",
        {"book": book, "form": form}
    )


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='book_list')
    return render(request, "delete_book.html",
                  {"book": book})


def check_admin_user(user):
    return user.is_staff


@login_required
@user_passes_test(check_admin_user)
def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='book_list')

    return render(request, "add_book.html", {"form": form})


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='book_list')

    return render(request, "edit_book.html", {
        "form": form,
        "book": book
    })


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()

    return render(request, "category.html", {"category": category, "books": books})


# @login_required
# def add_favorite(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     user = request.user
#     user.favorite_book
