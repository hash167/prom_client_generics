
from prometheus_flask_exporter import PrometheusMetrics, Flask
from prom_client.default_labels import set_default_labels, get_default_labels

def instrument_flask(app: Flask, service: str) -> Flask:
    set_default_labels()
    env_labels = get_default_labels()
    env_labels['service'] = service
    return PrometheusMetrics(
        app=app,
        default_labels=env_labels,
    )
