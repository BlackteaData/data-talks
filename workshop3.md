# Workshop 3

## Agenda

- Review last week and move data using DMS (1hr)
- General overview of Glue (15min)
- Create a Glue Crawler (20min)
- Read data using Athena (30min)
- Visualise data using Quicksight (30min)
- Configure AWS CLI (15min)


In this workshop, we will cover AWS native Analytical and Visualisation tools.

## Task: Query a table stored in S3 from Athena

We will query a CSV file from Athena

1) Upload any CSV file to the S3 bucket. Here is an example: [Flight dataset](/files/flights.csv).
2) Create a crawler in AWS Glue
3) Use SQL to query the dataset in Athena

This [page](https://awstip.com/querying-data-from-s3-using-aws-athena-18a41d061d94) provides a good walkthrough of the steps required.

## Task: Create dashboards in Quicksight

Quicksight is the native AWS solution to build and share Business Inteligence (BI) dashboards.

1) Enrol in the free trial for Quicksight.
2) Create two datasources for Quicksight
    a) Athena
    b) RDS Postgres (data warehouse)

Quicksight will need to have access to the RDS instance. You will need to add the 54.153.249.96/27 CIDR IP range to the RDS Security Group. This is the range (Sydney region) where QuickSight traffic originates from when making outbound connections to databases.


### Using the Command Line Interface

Besides the user inteface, we have used so far, we can also issue commands that modify AWS resources from a command line interface. We are going to run some commands in CLI in the next class, so let's set this up now. 

For this we need to configure our credentials. This process will create long term credentials access to your AWS account. This is not the most recommended action (a more secure way would be to only have temporary credentials), but it is still very popular.

In the command line run the following command and paste the information from your IAM user. 

```
aws configure
```

If you got an error saying you don't have the aws cli in your computer, go to this [page](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to install it.

