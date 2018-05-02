# http://docs.ceph.com/docs/master/radosgw/s3/python/

        #https://www.programcreek.com/python/example/3377/boto.connect_s3


"""

s3.amazonaws.com
s3.us-east-1.amazonaws.com
s3-external-1.amazonaws.com
s3.dualstack.us-east-1.amazonaws.com**

"""


import boto3
import logging
access_key = 'AKIAIZXA3XCC5QGMENNQ'
secret_key = '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'
s3_host = 's3.us-east-1.amazonaws.com'


s3client = boto3.client('s3', aws_access_key_id = access_key,aws_secret_access_key = secret_key)

"""
conn = boto3.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = s3_host,
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto3.s3.connection.OrdinaryCallingFormat(),
        )
"""

for bucket in s3client.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date
        )

