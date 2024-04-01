#!/usr/bin/env bash
set -ex
#cf-remote spawn --platform debian-12-x64 --count 1 --role client --name deb12
#cf-remote spawn --platform suse-15-x64 --count 1 --role client --name test
#cf-remote spawn --platform debian-9-x64 --count 1 --role client --name deb9

# 16 works :+1:
#for version in 18 20 22; do
#  cf-remote spawn --platform ubuntu-$version-04-x64 --count 1 --role client --name ubu$version
#done

#for version in 6 7 8 9; do
#  cf-remote spawn --platform rhel-$version-x64 --count 1 --role client --name rhel$version
#done

# windows
# (venv) cfengine-qa-cfe-4322-cf-remote-dynamic-ami: sort windows.list | cut -d- -f1,2 | sort -u
# EC2LaunchV2-Windows_Server
# TPM-Windows_Server
# Windows_Server-2016
# Windows_Server-2019
# Windows_Server-2022
#plat=windows
#for version in 2012 2016 2019 2022; do
#  cf-remote spawn --platform $plat-$version-x64 --count 1 --role client --name $plat$version
#done
# Error: Failed to spawn VMs - Problem spawning 'windows-2016-x64' VM in AWS (AMI: ami-0cea6c34c3dafdcaf, size=t2.micro). Error: UnsupportedOperation: Microsoft SQL Server is not supported for the instance type 't2.micro'.
# oops! I need to adjust my name_pattern! this gets me Amazon Machine Image (AMI)Windows_Server-2016-Japanese-Full-SQL_2017_Standard-2024.03.13
# ^^^ I do NOT want Japanese Full SQL

# make it easy to see the list of possibilities?!
# todo
# Error: Failed to spawn VMs - No images found for criteria: {'owner_id': '801119661308', 'name_pattern': 'Windows_Server-{version}*', 'user': 'Administrator', 'architecture': 'x86_64', 'version': '2012'}
# that should just come DIRECTLY from criteria with hard-coded ami? or maybe that ami is gone?
#
# Error: Failed to spawn VMs - Problem spawning 'windows-2016-x64' VM in AWS (AMI: ami-0cea6c34c3dafdcaf, size=m1.small). Error: Unsupported: The requested configuration is currently not supported. Please check the documentation for supported configurations.
plat=macos
for version in 10 11 12 13 14; do
  cf-remote spawn --platform $plat-$version-x64 --count 1 --role client --name $plat$version
done
aws ec2 --region eu-west-1 describe-images --owner 100343932686
#             "Architecture": "x86_64_mac",

