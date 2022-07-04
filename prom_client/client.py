from prometheus_client import Counter as _PromCounter
from typing import Generic, TypeVar, Iterable, Dict, cast, Optional
from prom_client.default_labels import get_default_labels

_MetricsTypeT = TypeVar('_MetricsTypeT', bound=[_PromCounter])

class _MetricsBase(Generic[_MetricsTypeT]):
    def __init__(self, label_names: Iterable[str]):
        self.default_labels: Dict[str] = get_default_labels()
        self.all_label_names: list = list(label_names) + list(self.default_labels.keys())
        self._parent_metric: _MetricsTypeT = None

    # Provides the label functionality
    def labels(self, *labelargs, **labelkwargs) -> _MetricsTypeT:            
        if labelargs:
            labelargs += tuple(self.default_labels.values())
            return cast(_MetricsTypeT, self._parent_metric.labels(*labelargs))
        labelkwargs.update(self.default_labels)
        return cast(_MetricsTypeT, self._parent_metric.labels(**labelkwargs))


class Counter(_MetricsBase[_PromCounter]):
    def __init__(self, name, documentation, labelnames=()):
        super().__init__(label_names=labelnames)
        print(self.all_label_names)
        self._parent_metric = _PromCounter(
            name=name, documentation=documentation,
            labelnames=self.all_label_names)

    def inc(self, amt: float = 1.0, labels: Optional[Dict[str, str]]=None):
        if not labels:
            labels = {}
        self.labels(**labels).inc(amt)
