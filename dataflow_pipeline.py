import json
import logging
from mapreduce import base_handler
from mapreduce import mapreduce_pipeline

logger = logging.getLogger(__name__)


def mapper(item):
    yield "token", json.dumps(item)


def reducer(key, value):

    yield "OK"


class TestPipeline(base_handler.PipelineBase):
    """
    Collects the info about a specific item - one instance for each space

    """
    def run(self):
        yield mapreduce_pipeline.MapreducePipeline(
            "items_job",
            "dataflow_pipeline.mapper",
            "dataflow_pipeline.reducer",
            "mapreduce.input_readers.DatastoreInputReader",
            mapper_params={
                "input_reader": {
                    "entity_kind": "models.Transaction"
                }
            },
            shards=1
        )

