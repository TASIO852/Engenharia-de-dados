import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
    
data = open('C:/Users/Pcyes_User/Documents/Data Science/aws/S3/Data/iris.json', 'rb')
s3.Bucket('bucket-ga4').put_object(Key='iris.json', Body=data)