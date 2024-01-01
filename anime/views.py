from django.shortcuts import render, redirect
from .models import Anime
from .forms import SearchForm
from django.views.generic.detail import DetailView

# Create your views here.

# Page Home
def home(request):
    anime_list = Anime.objects.all()[:25]
    return render(request, 'home.html', {'anime_list' : anime_list,})


# Page On-Going Anime
def on_going(request):
    anime_list = Anime.objects.all()[:25]
    return render(request, 'on-going-anime.html', {'anime_list' : anime_list,})

# Page Detail Anime
def anime_detail(request, anime_id):
    anime = Anime.objects.get(pk=anime_id)
    return render(request, 'anime_detail.html', {'anime': anime})

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime_detail.html'
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Ambil anime dari URL
        anime = self.object

        # Ambil daftar anime, tanpa memasukkan anime yang sedang ditampilkan ke dalamnya
        anime_list = Anime.objects.exclude(pk=anime.pk)[:6]

        context['anime_list'] = anime_list
        return context

# Page List Anime
def anime_list(request):
    anime_data = Anime.objects.order_by('title')
    alphabetically_grouped = {}

    for anime in anime_data:
        first_letter = anime.title[0].upper()
        if first_letter not in alphabetically_grouped:
            alphabetically_grouped[first_letter] = []
        alphabetically_grouped[first_letter].append(anime)

    # Menentukan urutan huruf dan karakter '#'
    order = ['#'] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    # Membuat daftar huruf dan karakter '#' sesuai dengan urutan yang ditentukan
    all_letters = [char for char in order]

    # Menambahkan pesan "Anime tidak tersedia" untuk huruf yang tidak memiliki anime
    for letter in all_letters:
        if letter not in alphabetically_grouped:
            alphabetically_grouped[letter] = []

    # Menambahkan daftar '#' untuk anime dengan awalan berbeda
    alphabetically_grouped['#'] = []

    # Memindahkan anime dengan awalan angka atau simbol ke daftar '#'
    for anime in list(alphabetically_grouped.keys()):
        if anime not in all_letters and anime != '#':
            alphabetically_grouped['#'] += alphabetically_grouped[anime]
            del alphabetically_grouped[anime]

    # Mengumpulkan hasil ke dalam list berurutan
    sorted_anime_list = []
    for letter in all_letters:
        sorted_anime_list.append((letter, alphabetically_grouped[letter]))

    return render(request, 'anime_list.html', {'sorted_anime_list': sorted_anime_list})

# Search Engine
def search_anime(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            return redirect('search_results', query=query)
    else:
        form = SearchForm()

    context = {'form': form}
    return render(request, 'home.html', context)

# Hasil Search Engine
def search_results(request, query):
    results = Anime.objects.filter(title__icontains=query)
    context = {'query': query, 'results': results}
    return render(request, 'search_results.html', context)


