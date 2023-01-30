Hello Data Talks peeps!

All of the course material will be posted here! This repo is a Work In Progress!

[Presentation slides](https://docs.google.com/presentation/d/14xoWjsRJLO8B04qzxm4xvdpIrpLY8U5u4LyHlKto-zw/edit?usp=sharing)

[Dataset example for OLTP and DW](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms)


This is the high level plan of what we are going to run:

## [Workshop 1](/workshop1.md)

- Brief overview (10min)
- Overview of cloud (15min)
- Go through the different types of services available in the cloud (15min)
- Baseline knowledge, covering database, data lake, ETL process, networking, security (50min)
- Go through the architecture of the demo, explaining its components and why they are there (20min)

### Live demo! 
- Create AWS account (40 min)
- Overview of AWS console (20 min)
- Create an alarm to control costs (10 min)

## [Workshop 2](/workshop2.md)
Create infra:
- 2 databases on RDS: SQL Server (production) and Postgres (data warehouse) (1 hour)
- DMS. Create and test connections (30-45 min)
- Import data (30 min) 

## [Workshop 3](/workshop3.md)
- Move data from production into data warehouse using DMS (20min) 
- Pull data from external API into our data warehouse (20min)
- Read data using Athena (20min)
- Run simple transformation using AWS Glue (1hr)
- Visualise data using Quicksight (30 min)

## [Workshop 4](/workshop4.md)
- Continue any activities we haven't finished
- Keep learning


## Notes

The database should be created inside a Private subnet and accessed using a VPN or from a EC2 (virtual machine) instance, but for simplicity purposes we will create a database with a Public IP and let your IP connect to it only.