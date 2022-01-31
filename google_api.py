import requests

BASE_URL = "https://www.googleapis.com/books/v1/volumes?q="

book = input("Name book: ")
request_url = f"{BASE_URL}{book}"
response = requests.get(request_url)

if response.status_code != 200:
    print("error")

else:
    data = response.json()
    for item in data['items']:

        if 'pageCount' in item['volumeInfo']:
            page_count = item['volumeInfo']['pageCount']
            print(page_count)


# class GetBookData:
#     def
#
# class GoogleApiView(View):
#     """
#     Google api View for collect data
#     """
#     template_name = "book_api.html"
#
#     def get(self, request):
#         form = BookApiForm()
#         return render(request, "book_api.html", {'form': form})
#
#     def post(self, request):
#         form = BookApiForm(request.POST)
#         if form.is_valid():
#             key_words = request.POST['key_words']
#             key_words = key_words.replace(' ', '+')
#             google_url = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={key_words}')
#             if google_url.status_code == 200:
#                 result = google_url.json()
#
#                 for item in result['items']:  # check space in db
#                     if Book.objects.filter(
#                             title=item['volumeInfo']['title']):
#                         messages.warning(
#                             request, f"Książka '{key_words}' znajduje się już w bazie danych")
#                         return render('book_api.html', {'form': form})
#                     else:
#                         if 'authors' in item['volumeInfo']:
#                             book = Book()
#                             book.title = item['volumeInfo']['title']
#
#                             if 'publishedDate' in item['volumeInfo']:
#                                 book.publication_date = item['volumeInfo']['publishedDate']
#                             for author in item['volumeInfo']['authors']:
#                                 author_create = Book.objects.get_or_create(
#                                     name=author)[0]
#                                 book.objects.create(author_create=author_create)
#                             for item['type'] in item['volumeInfo']['industryIdentifiers']:
#                                 if item['type'] == 'ISBN_13':
#                                     isbn = item['industryIdentifiers']['identifier']
#                                 else:
#                                     isbn = None
#                                 book.objects.create(isbn=isbn)
#                             if 'pageCount' in item['volumeInfo']:
#                                 page_count = item['volumeInfo']['pageCount']
#                                 book.objects.create(page_count=page_count)
#                             if 'thumbnail' in item['volumeInfo']['imageLinks']:
#                                 thumbnail = item['volumeInfo']['thumbnail']
#                                 book.objects.create(thumbnail=thumbnail)
#                             if 'language' in item['volumeInfo']['language']:
#                                 publication_language = item['volumeInfo']['language']
#                                 book.objects.create(publication_language=publication_language)
#                             book.save()
#                 messages.success(request, 'Dodano nową pozycję')
#                 return redirect('book-list')
#             errors = ('Coś poszło nie tak')
#             return render(request, 'book_api.html', {'form': form, 'messages': errors})