from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Article, ArticleComment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def get_pages_to_show(current_page, total_pages):
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def article_list(request):
    articles = Article.objects.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 9)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'articles': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    articles.views += 1
    articles.save()
    if request.method == 'POST':
        body = request.POST.get('body')
        ArticleComment.objects.create(body=body, article=articles, author=request.user)
    context = {
        'articles': articles
    }
    return render(request, 'blog/article_detail.html', context)


@login_required
def delete_article_comment(request, comment_id):
    comment = get_object_or_404(ArticleComment, id=comment_id, author=request.user)
    comment.delete()
    return redirect('blog:article_detail', slug=comment.article.slug)


def article_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 9)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'category': category,
        'articles': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'blog/article_category.html', context)
