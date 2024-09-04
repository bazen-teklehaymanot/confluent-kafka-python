from typing import Dict

from superstream import SuperstreamProducerInterceptor

from confluent_kafka.cimpl import Producer as _ProducerImpl


class SuperstreamProducer(_ProducerImpl):
    def __init__(self, config: Dict):
        self._interceptor = SuperstreamProducerInterceptor(config)
        config = self._interceptor.superstream.wait_for_superstream_configs_sync(config)
        super().__init__(config)

        self._interceptor.set_producer_handler(super().produce)

    def produce(self, *args, **kwargs):
        self._interceptor.produce(*args, **kwargs)
