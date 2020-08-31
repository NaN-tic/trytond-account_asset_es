try:
    from trytond.modules.account_asset_es.tests.test_account_asset_es import suite  # noqa: E501
except ImportError:
    from .test_account_asset_es import suite

__all__ = ['suite']
