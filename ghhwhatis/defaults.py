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
        "ACCOUNTS_ENABLED", "ADMIN_MEDIA_PREFIX", "SHOW_ADS",
        "BLOG_BITLY_USER", "BLOG_BITLY_KEY",
        "COMMENTS_DISQUS_SHORTNAME", "COMMENTS_NUM_LATEST",
        "COMMENTS_DISQUS_API_PUBLIC_KEY", "COMMENTS_DISQUS_API_SECRET_KEY",
        "DEV_SERVER", "FORMS_USE_HTML5", "GRAPPELLI_INSTALLED",
        "GOOGLE_ANALYTICS_ID", "JQUERY_FILENAME", "LOGIN_URL", "LOGOUT_URL",
        "PAGES_MENU_SHOW_ALL", "SITE_TITLE", "SITE_TAGLINE", "RATINGS_MAX",
    ),
)