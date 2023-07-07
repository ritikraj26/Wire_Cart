from django.urls import path
from accounts.views import login, signup, activate_email

urlpatterns = [
    path('login/',login, name="login"),
    path('signup/',signup, name="signup"),
    path('activate/<email_token>/',activate_email, name="activate_email")
]
