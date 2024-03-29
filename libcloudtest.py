#!/usr/bin/env python3
# https://libcloud.readthedocs.io/en/stable/compute/drivers/ec2.html
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import os

cls = get_driver(Provider.EC2)
print(os.environ['AWS_ACCESS_KEY_ID'])
print(    os.environ["AWS_SECRET_ACCESS_KEY"])
print(os.environ['AWS_SESSION_TOKEN'])
#exit(0)
driver = cls(
    os.environ["AWS_ACCESS_KEY_ID"],
    os.environ["AWS_SECRET_ACCESS_KEY"],
    token=os.environ.get("AWS_SESSION_TOKEN", ""),
    region="us-east-2"
)
#exit(0)

#volume = driver.create_volume(size=100, name="Test GP volume", ex_volume_type="gp2")
#print(volume)


#print('len(list_sizes)=' + repr(len(driver.list_sizes()))) # works
#      'name':'suse-sle-micro-5-3-byos-v20231030-hvm-ssd-x86_64',

images = driver.list_images(
    ex_owner='013907871322',
    ex_filters = {
        'name': 'suse-sles-15*',
      'virtualization-type':'hvm',
      'architecture':'x86_64'
    }
)
#image = images[0]
#print(type(image))
#print(vars(image))

# and now query with python magic :)
# sort by images creationdate reverse
print(images[0].extra['creation_date'])

# Sort images by creation date in reverse order
selected = sorted(images, key=lambda x: x.extra['creation_date'], reverse=True)[0]
print(selected)
