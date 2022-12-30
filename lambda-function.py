import boto3
import sys 
s3_rsc = boto3.resource('s3')
bucket_obj=s3_rsc.Bucket('mybucket123-output')


def lambda_handler(event, context):
    records=event['Records']
    for r in records:
        key=r['s3']['object']['key']
        bucket=r['s3']['bucket']['name']
        
        input_location={
        'Bucket': bucket,
        'Key': key
        }
        
        if key[-4:] == '.txt':
            output_file=f"txt/{key}"
        elif key[-4:] == '.pdf':
            output_file=f"pdf/{key}"
        elif key[-4:] == '.csv':
            output_file=f"csv/{key}"
        else:
            sys.exit()
        bucket_obj.copy(input_location,output_file)
    
