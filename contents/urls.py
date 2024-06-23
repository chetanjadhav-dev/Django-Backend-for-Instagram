from django.urls import path
from .views import user

app_name = 'contents'

urlpatterns = [
    path('user/create/', user.CreatUser.as_view()),
    path('user/list/', user.UserList.as_view()),
    path('user/login/', user.LoginUserView.as_view()),
    path('user/<int:pk>/', user.RetriveUser.as_view()),
    path('user/update/', user.UpdateUser.as_view()),
    path('user/delete/<int:pk>/', user.DeleteUser.as_view()),
]
