# Prometheus Client Extension

Simple library to extend the prometheus client library by adding default labels via the environment variables(Prepend with O11Y)

Example: `O11Y_SERVICE` adds the `service` label

## How to use

- Setup a virtualenv with python 3.7 or above
- clone the repo
- From root of repo `pip install -e .` or `python setup.py install`
- Setup default label in environment `export O11Y_SERVICE=test`
- Open the python3 interpretor
```
from prom_client.client import Counter
from prom_client.default_labels import set_default_labels()

set_default_labels()  # Method to set the default labels from environment
counter = Counter('test_counter', 'some doc')
counter.inc()
```


To check value in registry

```
from prometheus_client import REGISTRY

value = REGISTRY.get_sample_value('test_counter_total', {'service': 'test})

```

## Flask Apps

Flask applications can be instrumented with default requests counts, latencies and exceptions as well using the `prom_client.flask.instrument_flask` module. Dockefile included for testing

- `docker build -t flask_app`
- `docker run -dp 8080:8080 flask_app`
- Don't forget to kill the app from docker desktop or the docker cli tool

