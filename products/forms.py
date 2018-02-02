from django.forms import ModelForm
from products.models import Product


# class ArticleForm(form.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['pub_date', 'headline', 'content', 'reporter']
#
# # Creating a form to add an article.
# form = ArticleForm()
#
# # Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)
