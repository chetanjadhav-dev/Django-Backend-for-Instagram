from django.urls import path
from .views import user,post

app_name = 'contents'

urlpatterns = [
    path('user/create/', user.CreatUser.as_view()),
    path('user/list/', user.UserList.as_view()),
    path('user/login/', user.LoginUserView.as_view()),
    path('user/<int:pk>/', user.RetriveUser.as_view()),
    path('user/update/', user.UpdateUser.as_view()),
    path('user/delete/<int:pk>/', user.DeleteUser.as_view()),

    path('post/create/', post.CreatPost.as_view()),
    path('post/list/', post.PostList.as_view()),
    path('post/<int:pk>/', post.RetrivePost.as_view()),
    path('post/update/<int:pk>/', post.UpdatePost.as_view()),
    path('post/delete/<int:pk>/', post.DeletePost.as_view()),
]
