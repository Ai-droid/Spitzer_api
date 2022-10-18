#modules
from types import NoneType
from sqlalchemy import create_engine, MetaData
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from config import assignment,audit,quality_audit
from sqlalchemy import insert, update
from pydantic_config import Assignment, Audit,Quality_audit

app=FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware( CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine('mysql+pymysql://spitzer_admin:spitzer_admin@spitzer-db.clxcbiehe0ph.us-east-1.rds.amazonaws.com:3306/spitzer')
meta = MetaData()
db_conn = engine.connect()

#assignment fetch button
@app.get('/fetch/assignment')
async def index_assignment(request: Assignment):
    query=assignment.select()#.fatchall()
    db_data = db_conn.execute(query.where(
        (assignment.columns.audit_vertical == request.audit_vertical) & 
        (assignment.columns.region == request.region) &
        (assignment.columns.month_of_import == request.month_of_import) &
        (assignment.columns.year_of_import == request.year_of_import))).fetchone()
    #If the record doesn't exist it'll return null
    return {
        db_data
    }

#audit fetch button
@app.get('/fetch/audit')
async def index_audit(request: Audit):
    query=audit.select()#.fatchall()
    db_data = db_conn.execute(query.where(
        (audit.columns.audit_vertical == request.audit_vertical) & 
        (audit.columns.region == request.region) &
        (audit.columns.month_of_import == request.month_of_import) &
        (audit.columns.year_of_import == request.year_of_import))).fetchone()
    #If the record doesn't exist it'll return null
    return {
        db_data
    }

#quality_audit fetch button
@app.get('/fetch/quality_audit')
async def index_quality_audit(request: Quality_audit):
    query=quality_audit.select()#.fatchall()
    db_data = db_conn.execute(query.where(
        (quality_audit.columns.audit_vertical == request.audit_vertical) & 
        (quality_audit.columns.region == request.region) &
        (quality_audit.columns.month_of_import == request.month_of_import) &
        (quality_audit.columns.year_of_import == request.year_of_import))).fetchone()
    #If the record doesn't exist it'll return null
    return {
        db_data
    }



#assignment submit button
@app.post('/submit/assignment')
async def submit_assignment(request: Assignment):

    #query
    query = assignment.insert().values(
        audit_vertical= request.audit_vertical, 
        region= request.region,
        month_of_import= request.month_of_import,
        year_of_import= request.year_of_import,
        audit_leader= request.audit_leader,
        auditor= request.auditor,
        date_of_data_ingestion= request.date_of_data_ingestion,
        standard_time_taken_for_audit= request.standard_time_taken_for_audit,
        no_of_asins_to_be_audited= request.no_of_asins_to_be_audited,
        no_of_vostok_asins= request.no_of_vostok_asins,
        no_of_di_asins= request.no_of_di_asins,
        no_of_declarations= request.no_of_declarations,
        no_of_po= request.no_of_po,
        no_of_other_business_type_asins= request.no_of_other_business_type_asins,
        target_date_of_closure= request.target_date_of_closure,
        name_of_other_business_verticals= request.name_of_other_business_verticals)
    
    #query execution
    db_conn.execute(query)
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Insert successfull"
    }

#audit submit button
@app.post('/submit/audit')
async def submit_audit(request: Audit):

    #query
    query = insert(audit).values(
        audit_vertical= request.audit_vertical, 
        region= request.region,
        month_of_import=request.month_of_import,
        year_of_import=request.year_of_import,
        auditor= request.auditor,
        date_of_audit_initiated=request.date_of_audit_initiated,
        audit_completion_date=request.audit_completion_date,
        time_taken_by_auditor=request.time_taken_by_auditor,
        total_import_value = request.total_import_value,
        total_duty_paid=request.total_duty_paid,
        currency=request.currency,
        overpayment_of_duties=request.overpayment_of_duties,
        overpayment_vostok=request.overpayment_vostok, 
        overpayment_di=request.overpayment_di,
        overpayment_other_business_verticals=request.overpayment_other_business_verticals,
        underpayment_of_duties=request.underpayment_of_duties,
        underpayment_vostok=request.underpayment_vostok,
        underpayment_di=request.underpayment_di,
        underpayment_other_business_verticals=request.underpayment_other_business_verticals,
        audit_population_target=request.audit_population_target,
        audit_population_unbiased=request.audit_population_unbiased,
        audit_coverage=request.audit_coverage,
        key_audit_findings=request.key_audit_findings,
        key_issues=request.key_issues,
        vostok_broker_errors=request.vostok_broker_errors,
        vostok_beagle_errors=request.vostok_beagle_errors,
        di_broker_errors=request.di_broker_errors,
        di_beagle_errors=request.di_beagle_errors,
        other_business_broker_errors=request.other_business_broker_errors,
        other_business_beagle_errors=request.other_business_beagle_errors,
        broker_error_sim_details=request.broker_error_sim_details,
        beagle_error_sim_details=request.beagle_error_sim_details,
        status=request.status)

    #query execution
    db_conn.execute(query)
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Insert successfull"
    }

#quality_audit submit button
@app.post('/submit/quality_audit')
async def submit_quality_audit(request: Quality_audit):
    
    #query
    query = insert(quality_audit).values(
        audit_vertical= request.audit_vertical, 
        region= request.region,
        month_of_import= request.month_of_import,
        year_of_import= request.year_of_import,
        auditor= request.auditor,
        quality_auditor= request.quality_auditor,
        status_of_qa= request.status_of_qa,
        date_of_sharing_data_with_qa= request.date_of_sharing_data_with_qa,
        qa_remark= request.qa_remark,
        qa_financial_impact= request.qa_financial_impact,
        audit_accuracy_before_qa= request.audit_accuracy_before_qa,    
        audit_accuracy_after_qa= request.audit_accuracy_after_qa,
        delacaration_accuracy_before_qa= request.delacaration_accuracy_before_qa,
        delacaration_accuracy_after_qa= request.delacaration_accuracy_after_qa)
    
    #query execution
    db_conn.execute(query)
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Insert successfull"
    }



@app.put('/update/assignment')
async def update_row(request: Assignment):
    
    #query
    query = update(assignment).values(
        audit_vertical= request.audit_vertical, 
        region= request.region,
        month_of_import= request.month_of_import,
        year_of_import= request.year_of_import,
        audit_leader= request.audit_leader,
        auditor= request.auditor,
        date_of_data_ingestion= request.date_of_data_ingestion,
        standard_time_taken_for_audit= request.standard_time_taken_for_audit,
        no_of_asins_to_be_audited= request.no_of_asins_to_be_audited,
        no_of_vostok_asins= request.no_of_vostok_asins,
        no_of_di_asins= request.no_of_di_asins,
        no_of_declarations= request.no_of_declarations,
        no_of_po= request.no_of_po,
        no_of_other_business_type_asins= request.no_of_other_business_type_asins,
        target_date_of_closure= request.target_date_of_closure,
        name_of_other_business_verticals= request.name_of_other_business_verticals) 
    
    #query execution
    db_conn.execute(query.where(
        (assignment.columns.audit_vertical == request.audit_vertical) & 
        (assignment.columns.region == request.region) &
        (assignment.columns.month_of_import == request.month_of_import) &
        (assignment.columns.year_of_import == request.year_of_import)))
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Update successfull"
    }

@app.put('/update/audit')
async def update_row(request: Audit):
    
    #query
    query = update(audit).values(
        audit_vertical= request.audit_vertical, 
        region= request.region,
        month_of_import=request.month_of_import,
        year_of_import=request.year_of_import,
        auditor= request.auditor,
        date_of_audit_initiated=request.date_of_audit_initiated,
        audit_completion_date=request.audit_completion_date,
        time_taken_by_auditor=request.time_taken_by_auditor,
        total_import_value = request.total_import_value,
        total_duty_paid=request.total_duty_paid,
        currency=request.currency,
        overpayment_of_duties=request.overpayment_of_duties,
        overpayment_vostok=request.overpayment_vostok, 
        overpayment_di=request.overpayment_di,
        overpayment_other_business_verticals=request.overpayment_other_business_verticals,
        underpayment_of_duties=request.underpayment_of_duties,
        underpayment_vostok=request.underpayment_vostok,
        underpayment_di=request.underpayment_di,
        underpayment_other_business_verticals=request.underpayment_other_business_verticals,
        audit_population_target=request.audit_population_target,
        audit_population_unbiased=request.audit_population_unbiased,
        audit_coverage=request.audit_coverage,
        key_audit_findings=request.key_audit_findings,
        key_issues=request.key_issues,
        vostok_broker_errors=request.vostok_broker_errors,
        vostok_beagle_errors=request.vostok_beagle_errors,
        di_broker_errors=request.di_broker_errors,
        di_beagle_errors=request.di_beagle_errors,
        other_business_broker_errors=request.other_business_broker_errors,
        other_business_beagle_errors=request.other_business_beagle_errors,
        broker_error_sim_details=request.broker_error_sim_details,
        beagle_error_sim_details=request.beagle_error_sim_details,
        status=request.status) 
    
    #query execution
    db_conn.execute(query.where(
        (assignment.columns.audit_vertical == request.audit_vertical) & 
        (assignment.columns.region == request.region) &
        (assignment.columns.month_of_import == request.month_of_import) &
        (assignment.columns.year_of_import == request.year_of_import)))
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Update successfull"
    }

@app.put('/update/quality_audit')
async def update_row(request: Quality_audit):
    
    #query
    query = update(quality_audit).values(
        audit_vertical= request.audit_vertical, 
        region= request.region,
        month_of_import= request.month_of_import,
        year_of_import= request.year_of_import,
        auditor= request.auditor,
        quality_auditor= request.quality_auditor,
        status_of_qa= request.status_of_qa,
        date_of_sharing_data_with_qa= request.date_of_sharing_data_with_qa,
        qa_remark= request.qa_remark,
        qa_financial_impact= request.qa_financial_impact,
        audit_accuracy_before_qa= request.audit_accuracy_before_qa,    
        audit_accuracy_after_qa= request.audit_accuracy_after_qa,
        delacaration_accuracy_before_qa= request.delacaration_accuracy_before_qa,
        delacaration_accuracy_after_qa= request.delacaration_accuracy_after_qa) 
    
    #query execution
    db_conn.execute(query.where(
        (assignment.columns.audit_vertical == request.audit_vertical) & 
        (assignment.columns.region == request.region) &
        (assignment.columns.month_of_import == request.month_of_import) &
        (assignment.columns.year_of_import == request.year_of_import)))
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Update successfull"
    }   
