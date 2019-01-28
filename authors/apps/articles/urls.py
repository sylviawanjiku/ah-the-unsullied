from django.urls import path

from authors.apps.articles.models import LikeDislike
from authors.apps.articles.views.comments import (
    CommentsListView, CommentsRetrieveUpdateDestroy
)

from authors.apps.articles.views.articles import (GetUpdateDeleteArticle,
                                                  CreateArticleView,
                                                  LikeDislikeArticleView)
from authors.apps.articles.views.favorite import FavouriteArticle, \
    GetFavouriteArticles


"""
Django 2.0 requires the app_name variable set when using include namespace
"""
app_name = 'articles'

urlpatterns = [
    path('', CreateArticleView.as_view(),
         name='article_create'),
    path('/<slug:slug>', GetUpdateDeleteArticle.as_view(),
         name='detail_article'),

    path('/<slug>/comments', CommentsListView.as_view(), name='comment'),

    path('/<slug>/comments/<int:id>',
         CommentsRetrieveUpdateDestroy.as_view(), name='thread'
         ),
    path('/<slug>/like',
         LikeDislikeArticleView.as_view(vote_type=LikeDislike.LIKE),
         name='article-like-like'),
    path('/<slug>/dislike',
         LikeDislikeArticleView.as_view(vote_type=LikeDislike.DISLIKE),
         name='article-like-dislike'),

    path('/<slug>/favorite', FavouriteArticle.as_view(),
         name='favorite_article'),
    path('/favorite/', GetFavouriteArticles.as_view(),
         name='all_favourite_article'),
]
