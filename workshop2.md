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

1) Download the two datasources to your local machine.
2) Go to S3 console
3) Select Buckets than `Create Bucket`
4) Write a unique bucket name (name has to be unique among all of the S3 buckets from ALL AWS accounts)
5) Let all Default configuration and Click `Create Bucket`
6) Click on the Bucket you just created
7) Click on the Upload and `Drag and drop` the files you want to upload or choose `Add files`. (Save the two .bak files into the S3 bucket)
8) Click on `Upload`

## Task: VPC and Security Group

The correct thing would be to create a new VPC and Security Group but for this lab, we will use the default VPC and Security Group.

1) Go to `VPC`, `Security Group` and select the `default` security group.
2) Select `Inbound rules` and then select `Edit Inbound rules`
3) Change `Type` to `MSSQL` and `Source` to `My IP`. Then `Add a new Rule` and set the type as `PostgreSQL` and the Source as `My IP` too and click `Save`. 

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

5) Select the Engine Type `PostgreSQL` and the `Free tier template`. Type a name for your DB instance and select the option `Manage master credentials in AWS Secrets Manager`. Check the `Public Access` option as `Yes` and click on `Create Database`.
7) While Postgres is being created, let's configure the Group Options for MSSQL. Click `Group Options` and then `Create Group`.
8) Define a `name and description` for the new group and select the Engine and Version according to the MSSQL version you are going to create and click on create. (We will use `sqlserver-ex version 15`) 
9) Select the group that was created and click on `Add option`
10) In option details select `SQLSERVER_BACKUP_RESTORE`. In IAM role select `Create a new role` and give a name for the new role. In S3 destination, select the bucket you created earlier and in Scheduling select `Immediately`. Finally, click on `Add option`.
11) Now let's create the MSSQL. Go to Database and select `Create New Database`. Select `MSSQL Express Edition` engine `15`.
12) Define a name for the database, select the `Manage master credentials in AWS Secrets Manager` option. Mark the `Public Access` option as `yes`. In additional settings, in `option group`, select the group that was created earlier and click `Create Database`.   

## Task: Load the database 
Copy the .bak files into the RDS SQL Server. 
This [tutorial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) gives an overview of the process.

Steps:

1) Restore the datasets into the RDS MSSQL Server, using the commands below. Make sure to change the S3 bucket name.

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

