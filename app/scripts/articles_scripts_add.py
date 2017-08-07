from .. import db
from ..models import Article


def create_article(article_list=[]):
    if not article_list:
        return
    for article in article_list:
        article = Article(
            title=article.title,
            content=article.content,
            summary=article.summary,
            source=article.source,
            articleType=article.articleType
        )
        db.session.add(article)
    db.session.commit()
