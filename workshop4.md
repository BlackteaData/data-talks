# Workshop 4

## Agenda

- Running ETL using the AWS Glue Studio (Covid 19 dataset) (1hr)
- Pull data from external API into our data warehouse (30min)
- Amazon Aurora zero-ETL integration with Amazon Redshift lab (1hr)



## ETL using Glue Studio

For this task we will closely follow this [AWS Glue Studio Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/71b5bdcf-7eb1-4549-b851-66adc860cd04/en-US/0-introduction).


1) First we need to copy the required file to our personal S3 bucket. Run the following commands in your CLI. 

```
# this creates a variable in the CLI called BUCKET_NAME
export BUCKET_NAME=blacktea

# this copies the file from an AWS owner S3 bucket to your own bucket
aws s3api put-object --bucket $BUCKET_NAME --key raw/covid_csv/
aws s3 cp s3://covid19-lake/enigma-jhu-timeseries/csv/ s3://$BUCKET_NAME/raw/covid_csv/ --recursive --copy-props none
```

