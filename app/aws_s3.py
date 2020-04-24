import os

import boto3


class AwsS3:
    def __init__(self, bucket):
        self.S3_KEY = os.environ.get("S3_KEY")
        self.S3_SECRET = os.environ.get("S3_SECRET")
        self.s3_resource = boto3.resource("s3")
        self.S3 = boto3.client(
            "s3",
            aws_access_key_id=self.S3_KEY,
            aws_secret_access_key=self.S3_SECRET,
        )
        self.S3_BUCKET = bucket

    def get_s3_files(self):
        my_bucket = self.s3_resource.Bucket(self.S3_BUCKET)
        summaries = my_bucket.objects.all()

        files = []
        for object in summaries:
            bucket = object.bucket_name
            key = object.key
            response = self.S3.head_object(Bucket=bucket, Key=key)

            file = {
                "key": key,
                "part_number": response["Metadata"]["part_number"],
                "build_phase": response["Metadata"]["build_phase"],
                "supplier": response["Metadata"]["supplier"],
                "last_modified": object.last_modified,
            }
            files.append(file)

        return files

    def upload_file(self, file, part_number, build_phase, supplier):
        my_bucket = self.s3_resource.Bucket(self.S3_BUCKET)
        my_bucket.Object(file.filename).put(
            Body=file,
            Metadata={
                "part_number": part_number,
                "build_phase": build_phase,
                "supplier": supplier,
            },
        )

        return True

    def delete_file(self, file):
        my_bucket = self.s3_resource.Bucket(self.S3_BUCKET)
        my_bucket.Object(file).delete()

        return True

    def download_file(self, file):
        my_bucket = self.s3_resource.Bucket(self.S3_BUCKET)
        file_object = my_bucket.Object(file).get()

        return file_object
