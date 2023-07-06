from django.urls import path
from accounts.views import login, signup

urlpatterns = [
    path('login/',login, name="login"),
    path('signup/',signup, name="signup")
]
