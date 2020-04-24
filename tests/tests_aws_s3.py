import boto3
import os
import pytest
from moto import mock_s3
from werkzeug.datastructures import FileStorage

from app.aws_s3 import AwsS3

test_bucket = "testbucket2345678"


@pytest.fixture(autouse=True)
def moto_boto():
    mock = mock_s3()
    mock.start()
    os.environ['AWS_ACCESS_KEY_ID'] = 'foo'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'bar'
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=test_bucket)
    yield conn
    mock.stop()


class TestAwsS3:
    def setup_method(self):
        self.test_s3 = AwsS3(test_bucket)

    def test_upload_file(self, moto_boto):
        with open("test-image.jpg", "rb") as fp:
            file = FileStorage(fp)
            self.test_s3.upload_file(file, "test", "test", "test")
        exp_result = moto_boto.meta.client.list_objects(Bucket=test_bucket)

        assert len(exp_result["Contents"]) == 1

    def test_delete_file(self, moto_boto):
        with open("test-image.jpg", "rb") as f:
            file = FileStorage(f)
            self.test_s3.upload_file(file, "test", "test", "test")
        add_result = moto_boto.meta.client.list_objects(Bucket=test_bucket)

        assert ("Contents" in add_result.keys()) is True

        self.test_s3.delete_file("test-image.jpg")
        del_result = moto_boto.meta.client.list_objects(Bucket=test_bucket)

        assert ("Contents" in del_result.keys()) is False

    def test_get_s3_files(self, moto_boto):
        with open("test-image.jpg", "rb") as fp:
            file = FileStorage(fp)
            self.test_s3.upload_file(file, "test", "test", "test")
        exp_result = moto_boto.meta.client.list_objects(Bucket=test_bucket)

        assert len(exp_result["Contents"]) == 1

        test_files = self.test_s3.get_s3_files()

        assert test_files[0]["key"] == "test-image.jpg"

    def test_download(self, moto_boto):
        with open("test-image.jpg", "rb") as fp:
            file = FileStorage(fp)
            self.test_s3.upload_file(file, "test", "test", "test")
        exp_result = moto_boto.meta.client.list_objects(Bucket=test_bucket)

        assert len(exp_result["Contents"]) == 1

        download = self.test_s3.download_file("test-image.jpg")

        assert download["ResponseMetadata"]["HTTPStatusCode"] == 200
