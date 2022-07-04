from typing import Optional
import os
from collections import OrderedDict

_DEFAULT_LABELS: Optional[OrderedDict] = None


def set_default_labels():
    env_vars = os.environ
    res: OrderedDict = OrderedDict()
    for k, v in env_vars.items():
        if k.startswith('O11Y_'):
            res[k[len('O11Y_'):].lower()] = v
    global _DEFAULT_LABELS
    _DEFAULT_LABELS = res

def get_default_labels() -> OrderedDict:
    if not _DEFAULT_LABELS:
        raise RuntimeError('Default Labels not set')
    return _DEFAULT_LABELS



