from django.shortcuts import render
from django.views.generic import TemplateView

from .workshop import accordion_data, card_data, cards_data, markdown_file_data, table_data, tabs_data


class HomeView(TemplateView):
    template_name = 'workshop.html'

    
class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return dict(card=card_data())


class CardsView(TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())

class DocumentView(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        doc = kwargs.get('doc', "README.md")
        return markdown_file_data(doc)

class TableView(TemplateView):
    template_name = 'table.html'
    
    def get_context_data(self, **kwargs):
        return dict(title='Random Show Episode Release Schedule', 
                    table=table_data('Documents/seasons.csv'))
    
    
class TabsView(TemplateView):
    template_name = 'tabs.html'
    
    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)

class SuperView(TemplateView):
    template_name = 'superview.html'
    
    def get_context_data(self, **kwargs):
        card=card_data()
        cards=cards_data()
        table=table_data('Documents/seasons.csv')
        accordion = accordion=accordion_data()
        tabs = tabs_data()
        carousel = carousel_data()
        return dict(title='Table View', cards=cards, table=table, tabs=tabs, accordion=accordion, carousel=carousel) 
    
class CarouselView(TemplateView):
    template_name = 'carousel.html'
    
    def get_context_data(self, **kwargs):
        carousel = carousel_data()
        return dict(title='Carousel View', carousel=carousel)    

def carousel_data():
    return [["https://source.unsplash.com/random/1200x800?technology", "active"],
            ["https://source.unsplash.com/random/1200x800?lion", ''], 
            ["https://source.unsplash.com/random/1200x800?plant"],
            ["https://source.unsplash.com/random/1200x800?Light"],
            ["https://source.unsplash.com/random/1200x800?sky"]]

    
class AccordionView(TemplateView):
    template_name = 'accordion.html'
    
    def get_context_data(self, **kwargs):
        return dict(title='Accordion View', accordion=accordion_data())