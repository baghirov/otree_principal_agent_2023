from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from datetime import date




class PaymentInfo(Page):
    def before_next_page(self):
        self.group.setkazanc()  
    
    form_model = 'player'
    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
            'id': participant.id_in_session,
            'date': str(date.today()),
            'final_payoff_with_showup': self.participant.payoff_plus_participation_fee()
        }
         
  

page_sequence = [PaymentInfo]

        