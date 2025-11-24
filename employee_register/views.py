from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_create(request):
	if(request.method == "POST"):
		title = request.POST.get("title")
		author = request.POST.get("author")
		Book.objects.creatte(title=title, author=author)
		return redirect("book_list")
	return render(request, "books/book_create.html")

def book_list(request):
	books = Book.objects.all()
	return render(request, "books/book_list.html", {"books" : books})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "books/book_update.html", {"book": book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/book_delete.html", {"book": book})

