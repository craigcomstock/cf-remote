aws_defaults = {
    "sizes": {
        "x86_64": {
            "size": "t2.micro",
            "xlsize": "t2.xlarge",
        },
        "arm64": {
            "size": "t4g.micro",
            "xlsize": "t4g.xlarge",
        }
    },
    "user": "ec2-user"
}
aws_image_criteria = {
    "debian-9": {
        "owner_id": "379101102735",
        "name_pattern": "debian-stretch-hvm-x86_64*",
        "user": "admin",
    },
    "debian": {
        "owner_id": "136693071363",
        "name_pattern": "debian-{version}*",
        "user": "admin",
    },
    "ubuntu-16": {
        "owner_id": "099720109477",
        "name_pattern": "ubuntu-pro-server/images/hvm-ssd/ubuntu-xenial-16.04-amd64-pro-server*",
        "user": "ubuntu"
    },
    "ubuntu": {
        "owner_id": "099720109477",
        "name_pattern": "ubuntu/images/hvm-ssd/ubuntu-*-{version}*",
        "user": "ubuntu",
    },
    "centos": {
        "meta": "This owner is our nt-dev account in AWS so these are private custom images.",
        "owner_id":"304194462000",
        "name_pattern": "centos-{version}-x64"
    },
    "rhel": {
        "owner_id": "309956199498",
        "name_pattern": "RHEL-{version}*",
    },
    "windows-2012-x64": {
        "ami": "ami-045768fc2ae3fa829",
        "user": "Administrator",
        "sizes": {
            "x86_64": {
                "size": "m1.small",
                "xlsize": "m3.xlarge",
            }
        }
    },
    "windows-2016": {
        "owner_id": "801119661308",
        "name_pattern": "Windows_Server-{version}*",
        "sizes": {
            "x86_64": {
                "size": "m1.small",
                "xlsize": "m3.xlarge",
            }
        },
        "user": "Administrator"
    },
    "windows": {
        "owner_id": "801119661308",
        "name_pattern": "Windows_Server-{version}*",
        "user": "Administrator"
    },
    "suse": {
        "owner_id":"013907871322",
        "name_pattern": "suse-sles-{version}*"
    },
    "macos": {
        "owner_id": "634519214787",
        "name_pattern":"amxn-ec2-macos-{version}*"
    },
}
