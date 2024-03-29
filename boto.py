#!/usr/bin/env python3
# https://libcloud.readthedocs.io/en/stable/compute/drivers/ec2.html
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-2'
)
ec2 = boto3.client('ec2',config=my_config)
response = ec2.describe_images()
print(response)
# works! hmm...
# 304194462000 is nt-dev owner
#
#driver.list_images(ex_owner=304194462000)
