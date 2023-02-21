# Workshop 4

## Agenda

- Configure AWS CLI (15min)
- Running ETL using the AWS Glue Studio (Covid 19 and Bitcoin dataset) (2hrs)
- Visualise on Quicksight (15min)

## Task 1: Setup the AWS CLI (Command Line Interface)

Besides the user interface that we have used so far, we can also issue commands that modify AWS resources from a command line interface. We are going to run some commands directly from the CLI, so let's set this up now. 

For this we need to configure our credentials. This process will create long term credentials access to your AWS account. This is not the most recommended action (a more secure way would be to only have temporary credentials), but it is still a very popular setup.

In the command line run the following command and paste the information from your IAM user. It will ask for the following information:

```
AWS Access Key ID = grab this from the IAM console 
AWS Secret Access Key = grab this from the IAM console 
Default region name = ap-southeast-2
Default output format = leave it blank
```

In your preferred shell editor run the following command and follow the prompt.
```
aws configure
```
 
If you got an error saying you don't have the aws cli in your computer, go to this [page](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to install it.

## Task 2: ETL using Glue Studio

For this task we will closely follow this [AWS Glue Studio Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/71b5bdcf-7eb1-4549-b851-66adc860cd04/en-US/0-introduction).

This is a screenshot of the final glue job (./images/glue-job-final.png).

### 2a. Copy files using the CLI
1) First we need to copy the required file to our personal S3 bucket. Run the following commands in your CLI. 

```
# this creates a temporary variable in the current shell called BUCKET_NAME. 

# for Mac and Linux OS
export BUCKET_NAME=name_of_bucket 
# for Windows OS
set BUCKET_NAME=name_of_bucket 
# for PowerShell
$Env:BUCKET_NAME=name_of_bucket 

# this creates a folder in your S3 bucket
aws s3api put-object --bucket $BUCKET_NAME --key raw/covid_csv/
aws s3api put-object --bucket $BUCKET_NAME --key raw/btcusd_csv/
aws s3api put-object --bucket $BUCKET_NAME --key curated/

# this copies the file from a different S3 bucket to your own bucket
aws s3 cp s3://covid19-lake/enigma-jhu-timeseries/csv/ s3://$BUCKET_NAME/raw/covid_csv/ --recursive --copy-props none
aws s3 cp s3://blacktea/raw/btcusd_csv/ s3://$BUCKET_NAME/raw/covid_csv/ --recursive --copy-props none
```

### 2a.(alternative) Copy files using the AWS Console

1) Create three subfolders in the bucket:
    a) raw/covid_csv
    b) raw/btcusd_csv
    c) curated

2) Download these two files to your local and upload to S3 under the specific folder.

    a) [Covid dataset](/files/jhu_csse_covid_19_timeseries_merged.csv) to `raw/covid_csv/`

    b) [Bitcoin Marketprice](/files/btcusd_raw.csv) to `raw/btcusd_csv/`


## Task 3: Visualise on Quicksight

We can now jump in the Quicksight console and create a dashboard for these data.

We will create a new Athena Dataset selecting the joined-curated dataset.

This is a screenshot of the final results(./images/quicksight-final.png)
