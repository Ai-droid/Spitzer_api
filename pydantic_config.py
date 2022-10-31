# from sqlalchemy import create_engine, MetaData
# from sqlalchemy import Table,Column
# from sqlalchemy.sql.sqltypes import Integer,String,Float
from pydantic import BaseModel

# engine = create_engine('mysql+pymysql://spitzer_admin:spitzer_admin@spitzer-db.clxcbiehe0ph.us-east-1.rds.amazonaws.com:3306/spitzer')
# meta = MetaData()
# db_conn = engine.connect()

class Assignment(BaseModel):
    audit_vertical: str
    region: str
    month_of_import: str
    year_of_import: int
    audit_leader: str
    auditor: str
    date_of_data_ingestion: str | None = None
    standard_time_taken_for_audit: int | None = None
    no_of_asins_to_be_audited: int | None = None
    no_of_vostok_asins: int | None = None
    no_of_di_asins: int | None = None
    no_of_declarations: int | None = None
    no_of_po: int | None = None
    target_date_of_closure: str | None = None
    no_of_other_business_type_asins: int | None = None
    name_of_other_business_verticals: str | None = None


class Audit_detail(BaseModel):
    audit_vertical: str
    region: str
    month_of_import: str
    year_of_import: int
    auditor: str
    status: str
    date_of_audit_initiated: str 
    audit_completion_date: str | None = None
    time_taken_by_auditor: int| None = None
    total_import_value: int | None = None
    total_duty_paid: float | None = None
    currency: str | None = None
    overpayment_of_duties: float | None = None
    overpayment_vostok: float | None = None
    overpayment_di: float | None = None
    overpayment_other_business_verticals: float | None = None
    underpayment_of_duties: float | None = None
    underpayment_vostok: float | None = None
    underpayment_di: float | None = None
    underpayment_other_business_verticals: float | None = None
    audit_population_target: int | None = None
    audit_population_unbiased: int | None = None
    audit_coverage: float | None = None
    key_audit_findings: str | None = None
    key_issues: str | None = None
    vostok_broker_errors: int | None = None
    vostok_beagle_errors: int | None = None
    di_broker_errors: int | None = None
    di_beagle_errors: int | None = None
    other_business_broker_errors: int | None = None
    other_business_beagle_errors: int | None = None
    broker_error_sim_details: str | None = None
    beagle_error_sim_details: str | None = None
    

class Quality_assurance(BaseModel):
    audit_vertical: str
    region: str
    month_of_import: str
    year_of_import: int
    auditor: str
    quality_auditor: str
    status_of_qa: str
    date_of_sharing_data_with_qa: str | None = None
    qa_remark: str | None = None
    qa_financial_impact: int | None = None
    audit_accuracy_before_qa: int | None = None
    audit_accuracy_after_qa: int | None = None
    delacaration_accuracy_before_qa: float | None = None
    delacaration_accuracy_after_qa: float | None = None
