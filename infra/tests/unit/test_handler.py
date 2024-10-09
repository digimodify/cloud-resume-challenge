import os
import re
import json
from unittest import mock

from hello_world import app # import the lambda handler function

# Read the DynamoDB table name from the CloudFormation template
with open('infra/template.yaml', 'r') as f:
    TABLENAME = re.search(r'TableName: (.*)?', f.read()).group(1)

@mock.patch.dict(os.environ, {"TABLENAME": TABLENAME})
def test_lambda_handler():
    # Check if AWS credentials and environment variables are set
    assert "AWS_ACCESS_KEY_ID" in os.environ
    assert "AWS_SECRET_ACCESS_KEY" in os.environ
    assert "AWS_SAM_STACK_NAME" in os.environ
    assert "AWS_REGION" in os.environ

    # Call the lambda handler function
    ret = app.lambda_handler("", "")

    # Assert that the response contains the necessary keys
    assert "statusCode" in ret
    assert "headers" in ret
    assert "body" in ret

    # Check for CORS headers in the response
    assert "Access-Control-Allow-Origin"  in ret["headers"]
    assert "Access-Control-Allow-Methods" in ret["headers"]
    assert "Access-Control-Allow-Headers" in ret["headers"]

    # Check the status code and validate the response body accordingly
    if ret["statusCode"] == 200:
        assert "counter" in ret["body"]
        assert isinstance(json.loads(ret["body"])["counter"], int)  # Check if 'counter' is an integer
    else:
        assert json.loads(ret["body"])["counter"] == -1
    return