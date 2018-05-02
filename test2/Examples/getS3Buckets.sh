#!/bin/bash
aws_profile=('sandbox' 'sandbox');

#loop AWS profiles
for i in "${aws_profile[@]}"; do
  echo "${i}"
  buckets=($(aws --profile "${i}" --region us-east-1n s3 ls s3:// --recursive | awk '{print $3}'))

  #loop S3 buckets
  for j in "${buckets[@]}"; do
  echo "${j}"
  aws --profile "${i}" --region us-east-1n s3 ls s3://"${j}" --recursive --human-readable --summarize | awk END'{print}'
  done

done
