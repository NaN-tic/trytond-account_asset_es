from trytond.pool import Pool
from. import account


def register():
    Pool.register(
        account.AccountType,
        account.AccountTypeTemplate,
        module='account_asset_es', type_='model')
