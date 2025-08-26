import lambda_function

def test_lambda_handler():
    event = {
        "Records": [{
            "s3": {"bucket": {"name": "test-bucket"}, "object": {"key": "file.txt"}}
        }]
    }
    response = lambda_function.lambda_handler(event, None)
    assert "statusCode" in response
    assert response["statusCode"] == 200
