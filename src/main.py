import os
import time
import requests
import logging
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace import config_integration
from opencensus.trace.tracer import Tracer

REQUEST_URL = str(os.environ.get('REQUEST_URL'))
REQUEST_INTERVAL_SEC = int(os.environ.get('REQUEST_INTERVAL_SEC', 10))

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('').addHandler(AzureLogHandler())
logger = logging.getLogger(__name__)
config_integration.trace_integrations(['requests'])
tracer = Tracer(exporter=AzureExporter(), sampler=ProbabilitySampler(1.0))

def main() -> None:
    logger.info(f'Request URL: {REQUEST_URL}')
    logger.info(f'Interval: {REQUEST_INTERVAL_SEC} sec')
    s = requests.Session()
    while True:
        with tracer.span(name='main'):
            res = s.get(url=REQUEST_URL)
            logger.info(f'{res.status_code}')
        time.sleep(REQUEST_INTERVAL_SEC) 

if __name__ == "__main__":
    main()
