from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'oTree Hackathon, Franziska, Max, Thibaud, Michel'

doc = """
This app is supposed to offer different forms of data input. 
The functions are supposed to be customizable and easily implemented. 
Ths offers great advantage over z-Tree (yay!). 
"""


class Constants(BaseConstants):
    name_in_url = 'project_forms'
    players_per_group = None
    num_rounds = 1
    html_radio_choices = ['A', 'B', 'C'] # These are the choices for the html radio


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # This part is for the default django widget. The blank option is necessary to have empty boxes
    checkbox_option_1 = models.BooleanField(
        widget=widgets.CheckboxInput, blank=True)
    checkbox_option_2 = models.BooleanField(
        widget=widgets.CheckboxInput, blank=True)
    checkbox_option_3 = models.BooleanField(
        widget=widgets.CheckboxInput, blank=True)
    # The following part is just the basis for the following html code
    html_checkbox_1 = models.LongStringField()
    html_checkbox_2 = models.LongStringField()
    html_checkbox_3 = models.LongStringField()



    # This part is for the default django widget.
    # Define input variables (in this case as characters)
    radio = models.StringField(
        choices=['A', 'B', 'C'],
        widget=widgets.RadioSelect,
        )

    html_radio = models.StringField()
    
    slider = models.IntegerField(min=0, max=100, widget=widgets.Slider)
    
    html_slider_vertical = models.PositiveIntegerField()
    html_slider_horizontal = models.PositiveIntegerField()

    choice = models.StringField(choices=['A','B','C'])
    html_choice = models.StringField(choices=['A','B','C'], widget=widgets.RadioSelect)
    


