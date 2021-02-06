from django.urls import path

from .views import index, signup, user_login, user_logout, download_file, read_text

urlpatterns = [
    path('', index),
    # path('signup/', signup),
    # path('login/', user_login, name='user_login'),
    # path('logout/', user_logout),
    path('download/', download_file),
    path('text/',read_text)
]
