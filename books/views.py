from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def book_list(request):
    book = Book.objects.all()
    return render(request, "book_list.html", {"books": book})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    return render(
        request,
        "book_detail.html",
        {"book": book, "form": form}
    )


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='book_list')
    return render(request, "delete_book.html",
                  {"book": book})


def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='book_list')

    return render(request, "add_book.html", {"form": form})


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
