from django.views import View
from blog.models import Article
from .forms import ContactUsForm
from .models import SiteSettings
from django.contrib import messages
from .models import Team, TeamMember
from django.db.models import Prefetch
from project.models import Category, Project
from django.shortcuts import render, redirect
from customer.models import Comment, Newsletter


class HomeView(View):
    def get(self, request):
        comments = Comment.objects.filter(publish=True)[:10]
        team = Team.objects.last()
        site_settings = SiteSettings.objects.first()
        articles = Article.objects.filter(status='published').order_by('-created_at')[:3]
        categories = Category.objects.prefetch_related(Prefetch('projects', queryset=Project.objects.filter(publish=True))).all()
        project = Project.objects.filter(publish=True)
        team_member = TeamMember.objects.all()
        context = {
            'comments': comments,
            'team': team,
            'categories': categories,
            'site_settings': site_settings,
            'articles': articles,
            'project': project,
            'team_member': team_member,
        }
        return render(request, 'core/home.html', context)

    def post(self, request):
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو خبرنامه ما شده اید.')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'ایمیل شما با موفقیت ثبت شد.')
        return render(request, 'core/home.html')


class FaqView(View):
    def get(self, request):
        site_settings = SiteSettings.objects.first()
        return render(request, 'core/faq.html', {'site_settings': site_settings})


class ContactView(View):
    def get(self, request):
        site_settings = SiteSettings.objects.first()
        form = ContactUsForm()
        return render(request, 'core/contact.html', {'site_settings': site_settings, 'form': form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
        messages.error(request, 'مشکلی پیش آمده .لطفا مجدد تلاش کنید.')
        return render(request, 'core/contact.html', {'form': form})
