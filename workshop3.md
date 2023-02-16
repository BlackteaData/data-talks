# Workshop 3

## Agenda

- Review last week and move data using DMS (1hr)
- General overview of Glue (15min)
- Create a Glue Crawler (20min)
- Read data using Athena (30min)
- Visualise data using Quicksight (30min)
- Configure AWS CLI (15min)


In this workshop, we will cover AWS native Analytical and Visualisation tools.

## Task 1: Query a table stored in S3 from Athena

We will query a CSV file from Athena

### S3 console
1) Upload a CSV file to the S3 bucket. This process will work with any CSV file. Here is an example: [Flight dataset](/files/flights.csv).

2) Go to the S3 bucket and click on `create folder`. Folder name = flight_data. Leave encryption as SSE-S3.

3) Upload only the file `flights.csv`.


#### Try creating another crawler for a different file
The Glue Crawler can be very useful in creating schema-on-read. However, in some instances the data won't be in the desired format. The raw files for the database we have been using is one of them. Have a go downloading it and going through the same steps as before.

For this exercise, download this [zip file](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksDW-data-warehouse-install-script.zip) to your local machine and unzip. This folder contains all of the CSV files and SQL commands to create the same DW database we created before hand.

You will notice an issue with showing the dataset. If you have a look at the CSV file, the separator is a pipe `|`, instead of the default comma symbol `,`. There are multiple ways to `transform` this data, that can be investigated later on. 


### AWS Glue console
4) Go to Crawlers and `Create a Crawler`.

5) The path source will be the bucket and folder you have just created, followed by `/`.

6) Run the crawler and have a look at Athena. 

### Amazon Athena
7) Use SQL to query the dataset in Athena.


This [page](https://awstip.com/querying-data-from-s3-using-aws-athena-18a41d061d94) provides a good walkthrough of the steps required.


## Task 2: Create dashboards in Quicksight

Quicksight is the native AWS solution to build and share Business Inteligence (BI) dashboards.

1) Enrol in the free trial for Quicksight.
2) Create two datasources for Quicksight
    a) Athena
    b) RDS Postgres (data warehouse)

Quicksight will need to have access to the RDS instance. You will need to add the 54.153.249.96/27 CIDR IP range to the RDS Security Group. This is the range (Sydney region) where QuickSight traffic originates from when making outbound connections to databases.


## Task 3: Setup the AWS CLI (Command Line Interface)

Besides the user interface, we have used so far, we can also issue commands that modify AWS resources from a command line interface. We are going to run some commands in CLI in the next workshop, so let's set this up now. 

For this we need to configure our credentials. This process will create long term credentials access to your AWS account. This is not the most recommended action (a more secure way would be to only have temporary credentials), but it is still a very popular setup.

In the command line run the following command and paste the information from your IAM user. 

```
aws configure
```

If you got an error saying you don't have the aws cli in your computer, go to this [page](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to install it.

