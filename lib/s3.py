import os
import boto3
import lib.certificate as certificate

def s3_upload(certificate = certificate.Certificate):
  file_name = certificate.local_path.replace("/tmp/", "")

  S3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("S3_AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("S3_AWS_SECRET_ACCESS_KEY")
    )
  
  try:
    S3.upload_file(certificate.local_path, 'ocean-alliance', 'adoption-material/' + file_name)
    S3.put_object_acl(ACL="public-read", Bucket='ocean-alliance', Key='adoption-material/' + file_name)
  except Exception as e:
    print(e)

  print("Successfully uploaded {} to S3".format(file_name))
  return True