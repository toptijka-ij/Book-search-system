from django.urls import path

from .views import EditComment, DeleteComment, AddComment

app_name = 'comment'
urlpatterns = [
    path('add_comment/<int:book_pk>/', AddComment.as_view(), name='add_comment'),
    path('comment_edit/<int:pk>', EditComment.as_view(), name='comment_edit'),
    path('comment_delete/<int:pk>', DeleteComment.as_view(), name='comment_delete'),
]
