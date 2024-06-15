from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Tag, Quote
from .utils import get_mongodb
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm

# Create your views here.

def main(request, page=1):
    quotes = Quote.objects.order_by('-created_at').all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_on_page})

def author(request, fullname):
    author = get_object_or_404(Author, fullname=fullname)
    born_date = author.born_date[:11]
    return render(request, 'quotes/author.html', context={'author': author,
                                                               'born_date_formatted': born_date})
@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='quotes:root')
    return render(request, 'quotes/add_author.html', context={'form': AuthorForm()})

@login_required
def add_quote(request):
    if request.method == "POST":
        raw_tags = request.POST.get('tags')
        tags = []
        for t in raw_tags.split(','):
            tag, _ = Tag.objects.get_or_create(name=t.strip())
            tags.append(tag)
        author_name = request.POST.get('author')
        author, _ = Author.objects.get_or_create(fullname=author_name.strip())
        quote_text = request.POST.get('quote')
        quote = Quote.objects.create(quote=quote_text, author=author)
        quote.tags.set(tags)
        return redirect(to='quotes:root')
    return render(request, 'quotes/add_quote.html')

"""@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})"""