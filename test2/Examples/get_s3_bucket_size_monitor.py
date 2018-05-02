
import boto3
import datetime

"""
(Delete this comment when added to git (as git documents has this): mgeiser - 18 Apr 2018)

This script will 
    For both the Picwell AWS "Sandbox" and "Production" Accounts
    Get the list of S3 Buckets in the Account
    Get the Cloudwatch Stats for each bucket
    Iterate over the stats for each bucket
        keep a running total of the size of all buckets
        keep a running total of the size of all buckets > 1Tb
        Print out the S3 Bucket name and size of all buckets > 1Tb
"""

# needed for cloudwatch API call for date range for average size
# This will be used for a very short interval to the size now 
now = datetime.datetime.now()

# Credentials for Profiles
# DO NOT COMMIT TO SOURCE CONTROL WITH ACCESS KEYS AND SECRET KEYS (DUH!)
# TODO Externalize these to a yaml file that is NOT commited to git
access_key_sandbox = 'AKIAIZXA3XCC5QGMENNQ'
secret_key_sandbox = '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'

access_key_production = 'AKIAJ3RWHNGJCN5NU5PA'
secret_key_production = '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'

s3_host = 's3.us-east-1.amazonaws.com'


# Scalars for formating the size of the buckets
gigabyte = 1000000000
terabyte = gigabyte*1000

# Function that 
def getBucketSizesForAccount(account_name, access_key, secret_key):
    
    # TODO check the input parameters (not a production script so I'm skipping this for now - sue me!)
        # all are ! None
        # minimum lengths?
        # other?

    total_bucket_size = 0
    big_bucket_size = 0

    # create connections to Cloudwatch and S3
    cw = boto3.client('cloudwatch', aws_access_key_id = access_key, aws_secret_access_key = secret_key)
    s3client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_key)
    
    # Get a list of all buckets in this account
    allbuckets = s3client.list_buckets()

    # create output
    # Header Line for the output going to standard out
    print ("\n\n")
    print ("Account: " + account_name + "\n")
    print('Bucket'.ljust(60) + 'Size in Bytes'.rjust(25))

    # Iterate through each bucket in the account
    for bucket in allbuckets['Buckets']:
        # For each bucket item, look up the cooresponding metrics from CloudWatch
        # No other Statistics are of interest in this function
        response = cw.get_metric_statistics(Namespace='AWS/S3',
                                            MetricName='BucketSizeBytes',
                                            Dimensions=[
                                                {'Name': 'BucketName', 'Value': bucket['Name']},
                                                {'Name': 'StorageType', 'Value': 'StandardStorage'}
                                            ],
                                            Statistics=['Average'],
                                            Period=3600,
                                            StartTime=(now-datetime.timedelta(days=1)).isoformat(),
                                            EndTime=now.isoformat()
                                            )
        # The cloudwatch metrics will have the single datapoint, so just report on it.
        for item in response["Datapoints"]:
            this_bucket_size = int(item["Average"])
            total_bucket_size += this_bucket_size
    
            if (this_bucket_size > terabyte):
                print(bucket["Name"].ljust(60) + str("{:,}".format(this_bucket_size/gigabyte)).rjust(25)) + " Gb"
                big_bucket_size += this_bucket_size
    
    print ("\n")
    print ("Total sandbox 'Big bucket' (> 1TB) size: " + str("{:,}".format(big_bucket_size/gigabyte)))+ " Gb"
    print ("Total sandbox size: " + str("{:,}".format(total_bucket_size/gigabyte)))+ " Gb"
    print ("\n\n")


# Call the function for Sandox and Production
getBucketSizesForAccount("Sandbox", access_key_sandbox, secret_key_sandbox)
getBucketSizesForAccount("Production", access_key_production, secret_key_production)
