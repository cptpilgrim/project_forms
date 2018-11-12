from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Input_forms(Page):
        form_model = 'player'
        form_fields = ['checkbox_option_1', 'checkbox_option_2','checkbox_option_3', 'html_checkbox_1', 'html_checkbox_2', 'html_checkbox_3',
                        'radio', 'html_radio',
                       'slider',
                       'html_slider_vertical', 'html_slider_horizontal',
                        'choice', 'html_choice']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Input_forms,
    Results,
]
