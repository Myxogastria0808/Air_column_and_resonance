from django.urls import path
from .views import TitleView, PurposeView, PreparationView, MethodView, ResultView, DiscussionView, ReferenceView

urlpatterns = [
    path('', TitleView.as_view()),
    path('purpose/', PurposeView.as_view()),
    path('purpose/preparation/', PreparationView.as_view()),
    path('purpose/preparation/method/', MethodView.as_view()),
    path('purpose/preparation/method/result/', ResultView.as_view()),
    path('purpose/preparation/method/result/discussion/', DiscussionView.as_view()),
    path('purpose/preparation/method/result/discussion/reference/', ReferenceView.as_view()),
]

#You must connect other pages