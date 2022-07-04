
from prometheus_flask_exporter import PrometheusMetrics, Flask

def instrument_flask(app: Flask, service: str) -> Flask:
    return PrometheusMetrics(
        app=app,
        default_labels={"service": service}
    )
