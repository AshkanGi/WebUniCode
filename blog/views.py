from django.db.models import F
from core.models import SiteSettings
from django.http import JsonResponse
from .models import Category, Tag, Article, Profile
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import truncatewords


def article_list(request):
    site_settings = SiteSettings.objects.first()
    page = int(request.GET.get('page', 1))
    per_page = 6
    start = (page - 1) * per_page
    end = start + per_page
    articles = Article.objects.filter(status='published').order_by('-created_at')
    total_count = articles.count()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        articles_page = articles[start:end]
        data = []
        for article in articles_page:
            truncated_description = truncatewords(article.description, 20)
            data.append({
                'title': article.title,
                'description': truncated_description,
                'thumbnail_url': article.thumbnail.url if article.thumbnail else '',
                'url': article.get_absolute_url(),
                'created_at': article.created_at.strftime('%Y-%m-%d')
            })
        return JsonResponse({
            'articles': data,
            'has_more': total_count > end
        })
    articles_page = articles[start:end]
    context = {
        'site_settings': site_settings,
        'articles': articles_page,
        'has_more': total_count > end
    }
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    Article.objects.filter(slug=slug).update(views=F('views') + 1)
    categories = Category.objects.all()
    latest_articles = Article.objects.filter(status='published').exclude(slug=article.slug).order_by('-created_at')[:3]
    popular_tags = Tag.objects.all().order_by('-views')[:8]
    site_settings = SiteSettings.objects.first()
    try:
        author_profile = Profile.objects.get(user=article.author)
    except Profile.DoesNotExist:
        author_profile = None
    contact = article.content if article.content else None
    context = {
        'article': article,
        'categories': categories,
        'latest_articles': latest_articles,
        'popular_tags': popular_tags,
        'author_profile': author_profile,
        'site_settings': site_settings,
        'contact': contact,
    }
    return render(request, 'blog/article_detail.html', context)


def category_article(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)
    site_settings = SiteSettings.objects.first()
    context = {
        'category': category,
        'articles': articles,
        'site_settings': site_settings
    }
    return render(request, 'blog/category_article.html', context)


def tag_article(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    articles = tag.articles.all()
    site_settings = SiteSettings.objects.first()
    context = {
        'tag': tag,
        'articles': articles,
        'site_settings': site_settings
    }
    return render(request, 'blog/tag_article.html', context)


def search(request):
    articles_search = request.GET.get('search')
    articles = Article.objects.filter(status='published', title__icontains=articles_search)
    context = {
        'articles': articles
    }
    return render(request, 'blog/article_list.html', context)
