from mezzanine.conf import register_setting
from django.utils.translation import ugettext as _


register_setting(
    name="SHOW_ADS",
    label='Show ADs',
    description="Show ADs served from networks like adsense.",
    editable=True,
    default=True,
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("Sequence of setting names available within templates."),
    editable=False,
    default=(
        "SHOW_ADS",
    ),
)