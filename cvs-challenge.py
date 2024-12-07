import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node CandidatesDB
CandidatesDB_node1733460580136 = glueContext.create_dynamic_frame.from_options(
    connection_type = "sqlserver",
    connection_options = {
        "useConnectionProperties": "true",
        "dbtable": "dbo.Candidatos",
        "connectionName": "Sqlserver connection",
    },
    transformation_ctx = "CandidatesDB_node1733460580136"
)

# Script generated for node WorkExperienceDB
WorkExperienceDB_node1733462916467 = glueContext.create_dynamic_frame.from_options(
    connection_type = "sqlserver",
    connection_options = {
        "useConnectionProperties": "true",
        "dbtable": "dbo.Experiencia_Laboral",
        "connectionName": "Sqlserver connection",
    },
    transformation_ctx = "WorkExperienceDB_node1733462916467"
)

# Script generated for node VacantsDB
VacantsDB_node1733462978624 = glueContext.create_dynamic_frame.from_options(
    connection_type = "sqlserver",
    connection_options = {
        "useConnectionProperties": "true",
        "dbtable": "dbo.Vacantes",
        "connectionName": "Sqlserver connection",
    },
    transformation_ctx = "VacantsDB_node1733462978624"
)

# Script generated for node SQL Query Cadidate
SqlQuery3965 = '''
select * from dboCandidatos
'''
SQLQueryCadidate_node1733462847564 = sparkSqlQuery(glueContext, query = SqlQuery3965, mapping = {"dboCandidatos":CandidatesDB_node1733460580136}, transformation_ctx = "SQLQueryCadidate_node1733462847564")

# Script generated for node SQL Query WorkExp
SqlQuery3966 = '''
select * from dboExperiencia_Laboral
'''
SQLQueryWorkExp_node1733462954284 = sparkSqlQuery(glueContext, query = SqlQuery3966, mapping = {"dboExperiencia_Laboral":WorkExperienceDB_node1733462916467}, transformation_ctx = "SQLQueryWorkExp_node1733462954284")

# Script generated for node SQL Query Vacants
SqlQuery3964 = '''
select * from dboVacantes
'''
SQLQueryVacants_node1733463014466 = sparkSqlQuery(glueContext, query = SqlQuery3964, mapping = {"dboVacantes":VacantsDB_node1733462978624}, transformation_ctx = "SQLQueryVacants_node1733463014466")

# Script generated for node CandidateInfo
SqlQuery3967 = '''
SELECT 
    c.ID_Candidato,
    c.Nombre,
    c.Email,
    c.Telefono,
    c.Direccion,
    w.ID_Experiencia,
    w.ID_Candidato,
    w.Empresa,
    w.Titulo_Puesto,
    w.Duracion,
    w.Habilidades_Utilizadas
FROM dboCandidatos AS c
INNER JOIN dboWorkExp AS w
    ON c.ID_Candidato = w.ID_Candidato;
'''
CandidateInfo_node1733463091298 = sparkSqlQuery(glueContext, query = SqlQuery3967, mapping = {"dboCandidatos":SQLQueryCadidate_node1733462847564, "dboWorkExp":SQLQueryWorkExp_node1733462954284}, transformation_ctx = "CandidateInfo_node1733463091298")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQueryVacants_node1733463014466, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1733460406505", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1733463508294 = glueContext.getSink(path="s3://challenge-cvs-test-target", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1733463508294")
AmazonS3_node1733463508294.setCatalogInfo(catalogDatabase="cvs_challenge",catalogTableName="dbVacants")
AmazonS3_node1733463508294.setFormat("glueparquet", compression="snappy")
AmazonS3_node1733463508294.writeFrame(SQLQueryVacants_node1733463014466)
# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=CandidateInfo_node1733463091298, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1733460406505", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1733463698278 = glueContext.getSink(path="s3://challenge-cvs-test-target", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1733463698278")
AmazonS3_node1733463698278.setCatalogInfo(catalogDatabase="cvs_challenge",catalogTableName="dbCandidate")
AmazonS3_node1733463698278.setFormat("glueparquet", compression="snappy")
AmazonS3_node1733463698278.writeFrame(CandidateInfo_node1733463091298)
job.commit()