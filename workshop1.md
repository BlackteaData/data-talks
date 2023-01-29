# Workshop 1

This is the material and sources covered in Workshop 1


We are using these sources for the [production](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorks2019.bak) and the [data warehouse](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksDW2019.bak)datasets.

Task: Copy the .bak files into the RDS SQL Server. This [tutorial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) gives an overview of the process.


#### Error 1
Database backup/restore option is not enabled yet or is in the process of being enabled
To fix this issue, I have used these two sources:

[Create an option group](https://stackoverflow.com/questions/57005157/restore-from-s3-bucket-to-sql-server-getting-error-database-backup-restore-optio)
[AWS Solution](https://aws.amazon.com/premiumsupport/knowledge-center/native-backup-rds-sql-server/)


### Endpoints
Postgres
Endpoint: database-2.ceeffbcjqhgn.ap-southeast-2.rds.amazonaws.com
The user and password are stored on [Secrets Manager](rds!db-031c8c48-80cb-4c2c-86d7-705928bc24d7), but you won't have access to it - we will share the credentials during the workshop. 

SQL Server
Endpoint: production.ceeffbcjqhgn.ap-southeast-2.rds.amazonaws.com
[User and Password](rds!db-e4f703c3-0169-46bc-9a6c-18be4c755e8e)




#### To restore a dataset into RDS SQL Server

Command to restore datasets
exec msdb.dbo.rds_restore_database
	@restore_db_name='prod',
	@s3_arn_to_restore_from='arn:aws:s3:::blacktea/AdventureWorks2019.bak',
	@with_norecovery=0,
	@type='FULL';

exec msdb.dbo.rds_restore_database
	@restore_db_name='dw',
	@s3_arn_to_restore_from='arn:aws:s3:::blacktea/AdventureWorksDW2019.bak',
	@with_norecovery=0,
	@type='FULL';

