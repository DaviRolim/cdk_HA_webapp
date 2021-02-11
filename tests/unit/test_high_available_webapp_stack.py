import json
import pytest

from aws_cdk import core
from high-available-webapp.high_available_webapp_stack import HighAvailableWebappStack


def get_template():
    app = core.App()
    HighAvailableWebappStack(app, "high-available-webapp")
    return json.dumps(app.synth().get_stack("high-available-webapp").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
