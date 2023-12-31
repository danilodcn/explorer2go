from django.test import SimpleTestCase

from explorer2go.apps.web.functools.list_gradients import get_list_gradients
from explorer2go.apps.web.models.site import GradientSiteTheme, Site
from explorer2go.apps.web.tests.factories.site_factories import SiteFactory


class TestCreateContact(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.site: Site = SiteFactory.create()

    def test_list_gradients(self):
        processed_gradients = get_list_gradients(self.site.site_theme)
        gradients = GradientSiteTheme.objects.filter(
            site_theme__site=self.site
        )

        self.assertEqual(
            len(processed_gradients[GradientSiteTheme.Type.primary]),
            gradients.filter(type=GradientSiteTheme.Type.primary).count(),
        )
