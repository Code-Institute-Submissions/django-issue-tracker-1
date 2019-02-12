from django.test import TestCase
from .forms import MakePaymentForm

# Create your tests here.
class TestToDoItemForm(TestCase):

    def test_make_payment_without_all_info(self):
        form = MakePaymentForm({'credit_card_number': 'Create Tests'}, {'cvv': 'Create Tests'}, {'expiry_month': 'Create Tests'}, {'expiry_year': 'Create Tests'})
        self.assertFalse(form.is_valid())
    