# from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from whitenoise.storage import CompressedManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False


class ProtectedStorage(S3Boto3Storage):
    # location = settings.STATICFILES_LOCATION

    def __init__(self, *args, **kwargs):
        # kwargs['custom_domain'] = settings.AWS_S3_CUSTOM_DOMAIN
        super().__init__(*args, **kwargs)
