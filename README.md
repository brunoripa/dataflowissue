'dataflowissue' description
============================

To prepare the environment:

    mkvirtualenv google
    pip install -r requirements.txt -t lib

Launch appserver:

    dev_appserver.py .

Navigate `http://localhost:8080`

Error:

    INFO     2016-10-26 11:45:28,427 devappserver2.py:769] Skipping SDK update check.
    INFO     2016-10-26 11:45:28,465 api_server.py:205] Starting API server at: http://localhost:63824
    INFO     2016-10-26 11:45:28,470 dispatcher.py:197] Starting module "default" running at: http://localhost:8080
    INFO     2016-10-26 11:45:28,471 admin_server.py:116] Starting admin server at: http://localhost:8000
    ERROR    2016-10-26 11:45:31,687 app.py:1423] Exception on / [GET]
    Traceback (most recent call last):
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/flask/app.py", line 1817, in wsgi_app
        response = self.full_dispatch_request()
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/flask/app.py", line 1477, in full_dispatch_request
        rv = self.handle_user_exception(e)
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/flask/app.py", line 1381, in handle_user_exception
        reraise(exc_type, exc_value, tb)
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/flask/app.py", line 1475, in full_dispatch_request
        rv = self.dispatch_request()
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/flask/app.py", line 1461, in dispatch_request
        return self.view_functions[rule.endpoint](**req.view_args)
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/flask/views.py", line 84, in view
        return self.dispatch_request(*args, **kwargs)
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/flask/views.py", line 149, in dispatch_request
        return meth(*args, **kwargs)
      File "/Users/bruno.ripa/development/google/dataflowissue/views.py", line 11, in get
        pipeline.start(queue_name="mapreduce")
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/mapreduce/pipeline_base.py", line 21, in start
        return pipeline.Pipeline.start(self, **kwargs)
      File "/Users/bruno.ripa/development/google/dataflowissue/lib/pipeline/pipeline.py", line 673, in start
        self, idempotence_key, str(e)))
    PipelineSetupError: Error starting dataflow_pipeline.TestPipeline(*(), **{})#cb365bac528245f394b256b1d1ea8d57:
    INFO     2016-10-26 11:45:31,702 module.py:788] default: "GET / HTTP/1.1" 500 291

