from django.urls import path

from .views import EditReview, DeleteReview, add_review

app_name = 'review'
urlpatterns = [
    path('review_add/<int:book_pk>', add_review, name='review_add'),
    path('review_edit/<int:pk>', EditReview.as_view(), name='review_edit'),
    path('review_delete/<int:pk>', DeleteReview.as_view(), name='review_delete'),
]
