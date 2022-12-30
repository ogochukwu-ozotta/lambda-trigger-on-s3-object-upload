# lambda-trigger-on-s3-object-upload

# Lambda trigger on s3 object upload (AWS Automation in Python)

## Create s3 bucket for the input file and the output file

### To create an S3 bucket on the AWS Management Console, follow these steps:

1.  Sign in to the AWS Management Console and open the Amazon S3 console.
2.  Click on the "Create bucket" button.
3.  Enter a unique bucket name; "mybucket123-input" in the "Bucket name" field. 
5.  Click on the "Next" button to proceed to the next step.
6.  In the "Set properties" step, you can leave the default settings or customize them as needed.
7.  In the "Set permissions" step, you can leave the default settings or customize them as needed.
8.  Click on the "Create bucket" button to create the bucket.
It may take a few minutes for the bucket to be created and become available. 
Repeat the same steps above to create the second bucket for output file name; "mybucket123-output"

<img width="652" alt="image" src="https://user-images.githubusercontent.com/88560609/210115376-2deb4629-0314-4cd3-93c9-593b4d2bca87.png">


## Create Lambda Function 

### Here are the steps for setting up a Lambda trigger on an S3 object upload:

1. Open the AWS Lambda console.
2. Click on the "Create function" button. Author from scratch
3. Give your function a name ("lambda-trigger-test"), select "Python 3.x" as the runtime, and choose "Create a new role with basic Lambda permissions".
4. In the "Trigger" section, click on the "Add trigger" button.
5. In the "Trigger configuration" window, select "S3" as the trigger type.
6. Select the bucket you want to use as the trigger, and specify the events that should trigger the function. For example, you might want to trigger the function when a new object is created or when an existing object is deleted.
7. Optional: you can also specify a prefix or suffix for the trigger to apply only to objects with a certain name pattern.
8. Click on the "Add" button to save the trigger.
9. Scroll down to the "Function code" section and enter your code in the inline code editor or upload a file from your local system.
10. Scroll down to the "Basic settings" section and specify the amount of memory and timeout settings for your function.
11. Click on the "Save" button at the top of the page to save your function.
12. Now, whenever the specified events occur on the specified S3 bucket, the Lambda function will be triggered and your code will be executed.



```
import boto3
import sys 
s3_rsc = boto3.resources('s3')
bucket_obj=s3_rsc.Bucket('mybucket123-output')

def lambda_handler(event, context):
    records=event['Record']
    for r in records:
        key=r['s3']['object']['key']
        bucket=r['s3']['bucket']['name']
        
        input_location={
        'Bucket': bucket,
        'key': key
        }
        if key[-4:]== '.txt':
            output_file=f"txt/{key}"
        elif key [-4:]== '.pdf':
            output_file=f"pdf/{key}"
        elif key [-4:]== '.csv':
            output_file=f"csv/{key}"
        else:
            sys.exit()
        bucket_obj.copy(input_location,output_file)
        
        
```

