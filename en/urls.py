from django.urls import path
from .views import TitleView, PurposeView, PreparationView, MethodView, ResultView, DiscussionView

urlpatterns = [
    path('', TitleView.as_view()),
    path('purpose/', PurposeView.as_view()),
    path('preparation/', PreparationView.as_view()),
    path('method/', MethodView.as_view()),
    path('result/', ResultView.as_view()),
    path('discussion/', DiscussionView.as_view()),
]
#leave these links
