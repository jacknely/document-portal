import boto3
import pytest
from app import create_app
from moto import mock_s3

test_bucket = "testbucket2345678"


@pytest.fixture(scope="session")
def client():
    app = create_app("config.TestConfig")
    test_client = app.test_client()
    yield test_client


@pytest.fixture(autouse=True)
def moto_boto():
    mock = mock_s3()
    mock.start()
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=test_bucket)
    yield conn
    mock.stop()


class TestViews:
    def test_home(self, client, moto_boto):
        response = client.get("/")

        assert response.status_code == 200
        assert b"Submission Portal" in response.data
