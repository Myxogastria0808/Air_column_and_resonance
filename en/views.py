from django.views.generic import TemplateView

class TitleView(TemplateView):
    template_name = "title.html"

class PurposeView(TemplateView):
    template_name = "purpose.html"

class PreparationView(TemplateView):
    template_name = "preparation.html"

class MethodView(TemplateView):
    template_name = "method.html"

class ResultView(TemplateView):
    template_name = "result.html"

class DiscussionView(TemplateView):
    template_name = "discussion.html"

class ReferenceView(TemplateView):
    template_name = "Reference.html"