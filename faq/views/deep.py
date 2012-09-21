from django.views.generic import DetailView

from faq.models import Topic, Question


class QuestionDetail(DetailView):
    """
    A detail view of a Question.

    Templates:
        :template:`faq/question_detail.html`
    Context:
        question
            A :model:`faq.Question`.
        topic
            The :model:`faq.Topic` object related to ``question``.

    """
    queryset = Question.objects.published()
    template_name = 'faq/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['topic'] = Topic.objects.published().get(slug=self.topic_slug)
        return context
