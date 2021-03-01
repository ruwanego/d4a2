from django.urls import path


from .views import BookListView

# configure BookListView at the empty string '',
# and add a named URL home as a best practice
urlpatterns = [
    path('', BookListView.as_view(), name='home')
]
