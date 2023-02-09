# Workshop 2

## Agenda

Create infrastructure:
- S3 bucket (5min)
- Two databases on RDS: SQL Server (production) and Postgres (data warehouse) (45min)
- DMS to import and transform data. Create and test connections (30-45 min)
- Import data (30min)
- Move data from production database into data warehouse using DMS (20min) 

## Task: Create an S3 bucket
This bucket will contain the backup database files that will be loaded to the database later on.

Steps:
1) Go to S3 console
2) Write a unique bucket name (name has to be unique among all of the S3 buckets from ALL AWS accounts)
3) Let all Default configuration
4) Click `Create Bucket`

## Task: Create an RDS instance

Steps:
1) Go to RDS console
2) Click on `Databases` and `Create database` 
3) Select the desired database engine (we will create a Microsoft SQL Server and PostgreSQL)
4) We will use the default for most options. A few items to change:
	a) Credentials settings: Let AWS Secrets Manager to manage the password
	b) Instance configuration: Select the instance included in the free tier (usually t3.small). The cost of RDS instances is related to the size and type of the instance, so a larger and more powerful instance equals to a more expensive database. Another factor in the cost is licensing. Oracle and Microsoft charges licensing so you might be in a situation where even though the computer that is running the database is free, but you have to pay for the software that is running on the instance. MySQL and Postgres are open source so no licensing on these two engines.
	c) Select Public access = yes. As we are just learning about RDS and the data is public available, this option is okay. In real life, the database will be in a Private subnet and only accessible, securely, via resources in the AWS or through a VPN.

This paper goes into more details about each option:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html

## Task: Load the database 
Copy the .bak files into the RDS SQL Server. 
This [tutorial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) gives an overview of the process.

Steps:
1) Download the two datasources to your local machine.
2) Save the two .bak files into an S3 bucket.
3) Restore the datasets into the RDS MSServer, using the commands below. Make sure to change the S3 bucket name.

#### To restore a dataset into RDS SQL Server

Command to restore datasets:

In the first stage, both of these datasets will be restored in the SQL Server database. 

Production DB
```
exec msdb.dbo.rds_restore_database
	@restore_db_name='prod',
	@s3_arn_to_restore_from='arn:aws:s3:::blacktea/AdventureWorks2019.bak',
	@with_norecovery=0,
	@type='FULL';
```

Data Warehouse
```
exec msdb.dbo.rds_restore_database
	@restore_db_name='dw',
	@s3_arn_to_restore_from='arn:aws:s3:::blacktea/AdventureWorksDW2019.bak',
	@with_norecovery=0,
	@type='FULL';
```

To check the stage of the restore you can run this command (update the ID number of the transaction you have just run):

```
exec msdb.dbo.rds_task_status @task_id=1;
```

### Errors and Issues

During the process, you may find some errors. I've highlighted the ones I found and how to fix them.

#### Error 1
Database backup/restore option is not enabled yet or is in the process of being enabled.

To fix this issue, I have used these two sources:

[Create an option group](https://stackoverflow.com/questions/57005157/restore-from-s3-bucket-to-sql-server-getting-error-database-backup-restore-optio)
[AWS Solution](https://aws.amazon.com/premiumsupport/knowledge-center/native-backup-rds-sql-server/)

#### Error 2
MS-CDC has not been enabled on database

We can't run CDC using this version of MSServer. If you are in the required version, then running the command `EXEC sys.sp_cdc_enable_db` will do the trick.

Message when running the command on the current DB:

This instance of SQL Server is the Express Edition (64-bit). Change data capture is only available in the Enterprise, Developer, Enterprise Evaluation, and Standard editions.


### Database Migration Service (DMS)

We will now, load the dw database from MSSQL into the PostgreSQL database using DMS.



## Notes

The database should be created inside a Private subnet and accessed using a VPN or from a EC2 (virtual machine) instance, but for simplicity purposes we will create a database with a Public IP and let your IP connect to it only.

