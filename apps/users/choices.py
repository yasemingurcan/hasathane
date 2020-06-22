from django.utils.translation import gettext_lazy as _

CUSTOMER_STATE = (
    (0, _("Unrecognized")),
    (1, _("Guest")),
    (2, ("Registered"))
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
