
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


default_app_config = 'leonardo_horizon_dashboards.Config'


LEONARDO_APPS = ['leonardo_horizon_dashboards']

LEONARDO_PLUGINS = [
    ('leonardo_horizon_dashboards.apps.horizon', _('Horizon'))
]

LEONARDO_REQUIREMENTS = [
    'https://github.com/michaelkuty/horizon/archive/'
    'master.zip#openstack-dashboard'
]


class Config(AppConfig):
    name = 'leonardo_horizon_dashboards'
    verbose_name = "leonardo-horizon-dashboards"

    def ready(self):

        from django.conf import settings
        import openstack_dashboard.enabled
        import openstack_dashboard.local.enabled
        from openstack_dashboard.utils import settings as settings_utils

        settings_utils.update_dashboards(
            [
                openstack_dashboard.enabled,
                openstack_dashboard.local.enabled,
            ],
            settings.HORIZON_CONFIG,
            settings.INSTALLED_APPS,
        )
