import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountAssetEsTestCase(ModuleTestCase):
    'Test Account Asset Es module'
    module = 'account_asset_es'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountAssetEsTestCase))
    return suite
