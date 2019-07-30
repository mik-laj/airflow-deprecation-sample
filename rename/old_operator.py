from rename.new_operator import NewOperator
import warnings


class OldOperator(NewOperator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn("TEXT_MESSAGE", DeprecationWarning)

__all__ = [
    'OldOperator'
]