# Workshop 1

This is the material and sources covered in Workshop 1


We are using these sources for the [production](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorks2019.bak) and the [data warehouse](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksDW2019.bak)datasets.

Here are the visual representation of the datasets.

- [Transaction](/images/adventureworks2008_schema.gif)
- [Datawarehouse](/images/adventureworksdw2008.png)


## Task: 
Copy the .bak files into the RDS SQL Server. 
This [tutorial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) gives an overview of the process.

Steps:
1) Download the two datasources to your local machine.
2) Save the two .bak files into an S3 bucket.
3) Restore the datasets into the RDS MSServer, using the commands below. Make sure to change the S3 bucket name.

#### To restore a dataset into RDS SQL Server

Command to restore datasets:

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


### Database Endpoints
```
Postgres
Endpoint: database-2.ceeffbcjqhgn.ap-southeast-2.rds.amazonaws.com
The user and password will be shared during the workshop. 

SQL Server
Endpoint: production.ceeffbcjqhgn.ap-southeast-2.rds.amazonaws.com
The user and password will be shared during the workshop. 
```




