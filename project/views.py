from .models import Project
from core.models import SiteSettings
from django.views.generic import DetailView


class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        return context
