# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import If, Eval


class AccountTypeTemplate(metaclass=PoolMeta):
    __name__ = 'account.account.type.template'

    @classmethod
    def __setup__(cls):
        super(AccountTypeTemplate, cls).__setup__()

        if hasattr(cls, 'fixed_asset'):
            cls.fixed_asset.domain = [
                If(~Eval('statement').in_(['balance', 'income']),
                   ('fixed_asset', '=', False), ()),
                ]
            cls.fixed_asset.states = {
                'invisible': ((~Eval('statement').in_(['balance', 'income']))
                    | ~Eval('assets', True)),
                }


class AccountType(metaclass=PoolMeta):
    __name__ = 'account.account.type'

    @classmethod
    def __setup__(cls):
        super(AccountType, cls).__setup__()

        if hasattr(cls, 'fixed_asset'):
            cls.fixed_asset.domain = [
                If(~Eval('statement').in_(['balance', 'income']),
                   ('fixed_asset', '=', False), ()),
                ]
            cls.fixed_asset.states = {
                'invisible': ((~Eval('statement').in_(['balance', 'income']))
                    | ~Eval('assets', True)),
                }
