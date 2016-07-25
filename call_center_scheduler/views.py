from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.base import TemplateView, TemplateResponseMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class DefaultMixin(LoginRequiredMixin, TemplateResponseMixin):
    pass


class HomePageView(DefaultMixin, TemplateView):
    template_name = "index.html"


class RequestSlotView(DefaultMixin, CreateView):
    pass

