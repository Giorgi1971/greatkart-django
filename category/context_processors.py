from .models import Category

def menu_links(requesrts):
    links = Category.objects.all()
    return dict(links=links)