import flask
from flask import views
from dataflow_pipeline import TestPipeline

views_bp = flask.Blueprint("views", __name__)


class DataflowView(views.MethodView):
    def get(self):
        pipeline = TestPipeline()
        pipeline.start(queue_name="mapreduce")

        redirect_url = "%s/status?root=%s" % (pipeline.base_path, pipeline.pipeline_id)

        return flask.redirect(redirect_url)


views_bp.add_url_rule("/", view_func=DataflowView.as_view("pipeline"))