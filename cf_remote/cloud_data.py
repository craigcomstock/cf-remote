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
    "centos-7": {
        "owner_id":"304194462000",
        "name_pattern": "centos-{version}-x64"
    },
    "rhel": {
        "owner_id": "309956199498",
        "name_pattern": "RHEL-{version}*",
    },
    "windows": {
        "owner_id": "801119661308",
        "name_pattern": "Windows_Server-{version}*"
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

aws_platforms = {
    "ubuntu-18-04-x64": {
        "ami": "ami-0ee3436f275c4f2e8",
        "user": "ubuntu",
        "size": "m1.small",
        "xlsize": "m3.xlarge",
    },
    "ubuntu-14-04-x32": {
        "ami": "ami-07a1e6256cb43b99c",
        "user": "ubuntu",
        "size": "m1.small",
    },
    "debian-8-x64": {
        "ami": "ami-402f1a33",
        "user": "admin",
        "size": "t1.micro",
        "xlsize": "m3.xlarge",
    },
    "debian-7-x64": {
        "ami": "ami-61e56916",
        "user": "admin",
        "size": "t1.micro",
        "xlsize": "m3.xlarge",
    },
    "centos-6-x64": {
        "ami": "ami-05bd23226cb7c2896",
        "user": "centos",
        "size": "t2.micro",
        "xlsize": "m3.xlarge",
    },
    "centos-7-x64": {
        "ami": "ami-0f4775c518fa29365",
        "user": "centos",
        "size": "t2.micro",
        "xlsize": "m3.xlarge",
    },
    "rhel-5-x64": {
        "ami": "ami-ea94369d",
        "size": "t1.micro",
        "user": "root",
        "xlsize": "t1.micro",
    },
    "rhel-6-x64": {
        "ami": "ami-c1bb06b2",
        "size": "t2.micro",
        "user": "ec2-user",
        "xlsize": "t2.large",
    },
    "rhel-7-x64": {
        "ami": "ami-065ec1e661d619058",
        "size": "t2.micro",
        "user": "ec2-user",
        "xlsize": "t2.large",
    },
    "rhel-8-x64": {
        "ami": "ami-08f4717d06813bf00",
        "size": "t3a.micro",
        "user": "ec2-user",
        "xlsize": "m3.xlarge",
    },
    "rhel-9-x64": {
        "ami": "ami-049b0abf844cab8d7",
        "size": "t3a.micro",
        "user": "ec2-user",
        "xlsize": "m3.xlarge"
   },
    "centos-5-x32": {"ami": "ami-fe11398a", "user": "root", "size": "m1.small"},
    "debian-6-x64": {"ami": "ami-879e4ff0", "user": "admin", "size": "t1.micro"},
    "debian-5-x32": {"ami": "ami-8398b3f7", "user": "root", "size": "m1.small"},
    "debian-7-x32": {"ami": "ami-1be06c6c", "user": "admin", "size": "t1.micro"},
    "debian-4-x32": {"ami": "ami-8198b3f5", "user": "root", "size": "m1.small"},
    "ubuntu-12-04-x64": {
        "ami": "ami-d1767bb7",
        "user": "ubuntu",
        "size": "m1.small",
        "xlsize": "m3.xlarge",
    },
    "debian-6-x32": {"ami": "ami-8d9e4ffa", "user": "admin", "size": "t1.micro"},
    "ubuntu-16-04-x64": {
        "ami": "ami-0d47c52ffe8fef155",
        "user": "ubuntu",
    },
    "debian-5-x64": {"ami": "ami-8f98b3fb", "user": "root", "size": "m1.small"},
    "debian-4-x64": {"ami": "ami-8d98b3f9", "user": "root", "size": "m1.small"},
    "ubuntu-14-04-x64": {
        "ami": "ami-0c68b4b8bbbdc39de",
        "user": "ubuntu",
        "size": "m1.small",
        "xlsize": "m3.xlarge",
    },
    "ubuntu-12-04-x32": {"ami": "ami-5c78753a", "user": "ubuntu", "size": "m1.small"},
    "centos-5-x64": {"ami": "ami-f2113986", "user": "root", "size": "m1.small"},
    "windows-2012-x64": {
        "ami": "ami-045768fc2ae3fa829",
        "user": "Administrator",
        "size": "m1.small",
        "xlsize": "m3.xlarge",
    },
    "windows-2016-x64": {
        "ami": "ami-08f68fefe026532ea",
        "user": "Administrator",
        "size": "m1.small",
        "xlsize": "m3.xlarge",
    },
    "windows-2019-x64": {
        "ami": "ami-0311c2819c6a29312",
        "user": "Administrator",
        "size": "t2.small",
        "xlsize": "t2.xlarge",
    },
}
