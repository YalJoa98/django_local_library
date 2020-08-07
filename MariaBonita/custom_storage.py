from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'mariabonita'
    custom_domain = '{}.s3.us-east-2.amazonaws.com'.format(bucket_name)
    location = 'media'

class StaticStorage(S3Boto3Storage):
    bucket_name = 'mariabonita'
    custom_domain = '{}.s3.us-east-2.amazonaws.com'.format(bucket_name)
    location = 'static'