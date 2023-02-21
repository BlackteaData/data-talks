import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
import gs_to_timestamp
from awsglue.dynamicframe import DynamicFrame


# Script generated for node remove-time
def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    from pyspark.sql.functions import split, col

    df = dfc.select(list(dfc.keys())[0]).toDF()
    df = df.withColumn("date-only", split(col("date-time"), " ").getItem(0))
    dyf_dmy = DynamicFrame.fromDF(df, glueContext, "remove_time")

    return DynamicFrameCollection({"CustomTransform0": dyf_dmy}, glueContext)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket - Covid
S3bucketCovid_node1676932718489 = glueContext.create_dynamic_frame.from_catalog(
    database="covid-bitcoin",
    table_name="covid_csv",
    transformation_ctx="S3bucketCovid_node1676932718489",
)

# Script generated for node S3 bucket - bitcoin
S3bucketbitcoin_node1676934120081 = glueContext.create_dynamic_frame.from_catalog(
    database="covid-bitcoin",
    table_name="btcusd_csv",
    transformation_ctx="S3bucketbitcoin_node1676934120081",
)

# Script generated for node Change Schema (Apply Mapping)
ChangeSchemaApplyMapping_node1676942493115 = ApplyMapping.apply(
    frame=S3bucketCovid_node1676932718489,
    mappings=[
        ("uid", "long", "uid", "long"),
        ("iso2", "string", "iso2", "string"),
        ("iso3", "string", "iso3", "string"),
        ("code3", "long", "code3", "long"),
        ("admin2", "string", "admin2", "string"),
        ("latitude", "double", "latitude", "double"),
        ("longitude", "double", "longitude", "double"),
        ("province_state", "string", "province_state", "string"),
        ("country_region", "string", "country_region", "string"),
        ("date", "string", "date", "string"),
        ("confirmed", "long", "confirmed", "long"),
        ("deaths", "long", "deaths", "long"),
        ("recovered", "string", "recovered", "long"),
    ],
    transformation_ctx="ChangeSchemaApplyMapping_node1676942493115",
)

# Script generated for node to-date
todate_node1676940585987 = S3bucketbitcoin_node1676934120081.gs_to_timestamp(
    colName="timestamp", colType="autodetect", newColName="date-time"
)

# Script generated for node remove-time
removetime_node1676941371612 = MyTransform(
    glueContext,
    DynamicFrameCollection(
        {"todate_node1676940585987": todate_node1676940585987}, glueContext
    ),
)

# Script generated for node Select From Collection
SelectFromCollection_node1676941588173 = SelectFromCollection.apply(
    dfc=removetime_node1676941371612,
    key=list(removetime_node1676941371612.keys())[0],
    transformation_ctx="SelectFromCollection_node1676941588173",
)

# Script generated for node Join
ChangeSchemaApplyMapping_node1676942493115DF = (
    ChangeSchemaApplyMapping_node1676942493115.toDF()
)
SelectFromCollection_node1676941588173DF = SelectFromCollection_node1676941588173.toDF()
Join_node1676935034338 = DynamicFrame.fromDF(
    ChangeSchemaApplyMapping_node1676942493115DF.join(
        SelectFromCollection_node1676941588173DF,
        (
            ChangeSchemaApplyMapping_node1676942493115DF["date"]
            == SelectFromCollection_node1676941588173DF["date-only"]
        ),
        "left",
    ),
    glueContext,
    "Join_node1676935034338",
)

# Script generated for node Amazon S3
AmazonS3_node1676933298468 = glueContext.getSink(
    path="s3://blacktea/curated/covid/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["country_region"],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1676933298468",
)
AmazonS3_node1676933298468.setCatalogInfo(
    catalogDatabase="covid-bitcoin", catalogTableName="covid-curated"
)
AmazonS3_node1676933298468.setFormat("glueparquet")
AmazonS3_node1676933298468.writeFrame(ChangeSchemaApplyMapping_node1676942493115)
# Script generated for node Amazon S3
AmazonS3_node1676934727328 = glueContext.getSink(
    path="s3://blacktea/curated/btcusd/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1676934727328",
)
AmazonS3_node1676934727328.setCatalogInfo(
    catalogDatabase="covid-bitcoin", catalogTableName="btcusd-curated"
)
AmazonS3_node1676934727328.setFormat("glueparquet")
AmazonS3_node1676934727328.writeFrame(SelectFromCollection_node1676941588173)
# Script generated for node Amazon S3
AmazonS3_node1676935204544 = glueContext.getSink(
    path="s3://blacktea/curated/joined/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["country_region"],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1676935204544",
)
AmazonS3_node1676935204544.setCatalogInfo(
    catalogDatabase="covid-bitcoin", catalogTableName="joined-curated"
)
AmazonS3_node1676935204544.setFormat("glueparquet")
AmazonS3_node1676935204544.writeFrame(Join_node1676935034338)
job.commit()
