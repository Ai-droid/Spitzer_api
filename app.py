#modules
from types import NoneType
from fastapi import FastAPI
from config import assignment,audit,quality_audit,db_conn
from sqlalchemy import insert, update

app=FastAPI()

#assignment fetch button
@app.get('/fetch/assignment')
async def index_assignment(audit_vertical, region, month_of_import, year_of_import):
    query=assignment.select()#.fatchall()
    data = db_conn.execute(query.where(
        (assignment.columns.audit_vertical == audit_vertical) & 
        (assignment.columns.region == region) &
        (assignment.columns.month_of_import == month_of_import) &
        (assignment.columns.year_of_import == year_of_import))).fetchone()
    #If the record doesn't exist it'll return null
    return {
        "data":data
    }

#audit fetch button
@app.get('/fetch/audit')
async def index_audit(audit_vertical, region, month_of_import, year_of_import):
    query=audit.select()#.fatchall()
    data = db_conn.execute(query.where(
        (audit.columns.audit_vertical == audit_vertical) & 
        (audit.columns.region == region) &
        (audit.columns.month_of_import == month_of_import) &
        (audit.columns.year_of_import == year_of_import))).fetchone()
    #If the record doesn't exist it'll return null
    return {
        "data":data
    }

#quality_audit fetch button
@app.get('/fetch/quality_audit')
async def index_quality_audit(audit_vertical, region, month_of_import, year_of_import):
    query=quality_audit.select()#.fatchall()
    data = db_conn.execute(query.where(
        (quality_audit.columns.audit_vertical == audit_vertical) & 
        (quality_audit.columns.region == region) &
        (quality_audit.columns.month_of_import == month_of_import) &
        (quality_audit.columns.year_of_import == year_of_import))).fetchone()
    #If the record doesn't exist it'll return null
    return {
        "data":data
    }



#assignment submit button
@app.post('/submit/assignment')
async def submit_assignment(audit_vertical,region,month_of_import,audit_leader,auditor,date_of_data_ingestion,name_of_other_business_verticals,no_of_vostok_asins_to_be_audited,no_of_di_asins_to_be_audited,no_of_declarations_to_be_audited,no_of_po_to_be_audited,target_date_of_closure_of_audit,standard_time_taken_for_audit,year_of_import,no_of_other_business_type_asins):

    #query
    query = insert(assignment).values(
        audit_vertical= audit_vertical, 
        region= region,
        month_of_import=month_of_import,
        audit_leader= audit_leader,
        auditor= auditor,
        date_of_data_ingestion=date_of_data_ingestion,
        no_of_vostok_asins_to_be_audited=no_of_vostok_asins_to_be_audited,
        no_of_di_asins_to_be_audited=no_of_di_asins_to_be_audited,
        no_of_declarations_to_be_audited=no_of_declarations_to_be_audited,
        no_of_po_to_be_audited=no_of_po_to_be_audited,
        target_date_of_closure_of_audit=target_date_of_closure_of_audit,
        standard_time_taken_for_audit=standard_time_taken_for_audit,
        year_of_import=year_of_import,
        no_of_other_business_type_asins=no_of_other_business_type_asins,
        name_of_other_business_verticals=name_of_other_business_verticals )
    
    #query execution
    db_conn.execute(query)
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Insert" : "successfull"
    }

#audit submit button
@app.post('/submit/audit')
async def submit_audit(audit_vertical,region,month_of_import,year_of_import,auditor,date_of_audit_initiated,audit_complete_date,audit_time_taken_by_auditor,currency,overpayment_of_duties,overpayment_vostok, overpayment_di,overpayment_other_business_verticals,underpayment_of_duties,underpayment_vostok,underpayment_di,underpayment_other_business_verticals,key_audit_findings,key_issues,vostok_broker_errors,vostok_beagle_errors,di_broker_errors,di_beagle_errors,other_business_broker_errors,other_business_beagle_errors,broker_error_sim_details,beagle_error_sim_details,status):

    #query
    query = insert(audit).values(
        audit_vertical= audit_vertical, 
        region= region,
        month_of_import=month_of_import,
        year_of_import=year_of_import,
        auditor= auditor,
        date_of_audit_initiated=date_of_audit_initiated,
        audit_complete_date=audit_complete_date,
        audit_time_taken_by_auditor=audit_time_taken_by_auditor,
        currency=currency,
        overpayment_of_duties=overpayment_of_duties,
        overpayment_vostok=overpayment_vostok, 
        overpayment_di=overpayment_di,
        overpayment_other_business_verticals=overpayment_other_business_verticals,
        underpayment_of_duties=underpayment_of_duties,
        underpayment_vostok=underpayment_vostok,
        underpayment_di=underpayment_di,
        underpayment_other_business_verticals=underpayment_other_business_verticals,
        key_audit_findings=key_audit_findings,
        key_issues=key_issues,
        vostok_broker_errors=vostok_broker_errors,
        vostok_beagle_errors=vostok_beagle_errors,
        di_broker_errors=di_broker_errors,
        di_beagle_errors=di_beagle_errors,
        other_business_broker_errors=other_business_broker_errors,
        other_business_beagle_errors=other_business_beagle_errors,
        broker_error_sim_details=broker_error_sim_details,
        beagle_error_sim_details=beagle_error_sim_details,
        status=status)

    #query execution
    db_conn.execute(query)
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Insert" : "successfull"
    }

#quality_audit submit button
@app.post('/submit/quality_audit')
async def submit_quality_audit(audit_vertical,region,month_of_import, year_of_import,auditor,quality_auditor,status_of_qa,date_of_sharing_data_with_qa,qa_remark,qa_financial_impact,audit_accuracy_before_qa_calibration,audit_accuracy_after_qa_calibration,delacaration_accuracy_before_qa,delacaration_accuracy_after_qa ):
    
    #query
    query = insert(quality_audit).values(
        audit_vertical= audit_vertical, 
        region= region,
        month_of_import=month_of_import,
        year_of_import=year_of_import,
        auditor= auditor,
        quality_auditor=quality_auditor,
        status_of_qa=status_of_qa,
        date_of_sharing_data_with_qa=date_of_sharing_data_with_qa,
        qa_remark=qa_remark,
        qa_financial_impact=qa_financial_impact,
        audit_accuracy_before_qa_calibration=audit_accuracy_before_qa_calibration,    
        audit_accuracy_after_qa_calibration=audit_accuracy_after_qa_calibration,
        delacaration_accuracy_before_qa=delacaration_accuracy_before_qa,
        delacaration_accuracy_after_qa=delacaration_accuracy_after_qa)
    
    #query execution
    db_conn.execute(query)
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Insert" : "successfull"
    }



@app.put('/update/assignment')
async def update_row(audit_vertical,region,month_of_import,audit_leader,auditor,date_of_data_ingestion,name_of_other_business_verticals,no_of_vostok_asins_to_be_audited,no_of_di_asins_to_be_audited,no_of_declarations_to_be_audited,no_of_po_to_be_audited,target_date_of_closure_of_audit,standard_time_taken_for_audit,year_of_import,no_of_other_business_type_asins):
    
    #query
    query = update(assignment).values(
        audit_vertical= audit_vertical, 
        region= region,
        month_of_import=month_of_import,
        audit_leader= audit_leader,
        auditor= auditor,
        date_of_data_ingestion=date_of_data_ingestion,
        no_of_vostok_asins_to_be_audited=no_of_vostok_asins_to_be_audited,
        no_of_di_asins_to_be_audited=no_of_di_asins_to_be_audited,
        no_of_declarations_to_be_audited=no_of_declarations_to_be_audited,
        no_of_po_to_be_audited=no_of_po_to_be_audited,
        target_date_of_closure_of_audit=target_date_of_closure_of_audit,
        standard_time_taken_for_audit=standard_time_taken_for_audit,
        year_of_import=year_of_import,
        no_of_other_business_type_asins=no_of_other_business_type_asins,
        name_of_other_business_verticals=name_of_other_business_verticals ) 
    
    #query execution
    db_conn.execute(query.where(
        (assignment.columns.audit_vertical == audit_vertical) & 
        (assignment.columns.region == region) &
        (assignment.columns.month_of_import == month_of_import) &
        (assignment.columns.year_of_import == year_of_import)))
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Update" : "successfull"
    }

@app.put('/update/audit')
async def update_row(audit_vertical,region,month_of_import,year_of_import,auditor,date_of_audit_initiated,audit_complete_date,audit_time_taken_by_auditor,currency,overpayment_of_duties,overpayment_vostok, overpayment_di,overpayment_other_business_verticals,underpayment_of_duties,underpayment_vostok,underpayment_di,underpayment_other_business_verticals,key_audit_findings,key_issues,vostok_broker_errors,vostok_beagle_errors,di_broker_errors,di_beagle_errors,other_business_broker_errors,other_business_beagle_errors,broker_error_sim_details,beagle_error_sim_details,status):
    
    #query
    query = update(audit).values(
        audit_vertical= audit_vertical, 
        region= region,
        month_of_import=month_of_import,
        year_of_import=year_of_import,
        auditor= auditor,
        date_of_audit_initiated=date_of_audit_initiated,
        audit_complete_date=audit_complete_date,
        audit_time_taken_by_auditor=audit_time_taken_by_auditor,
        currency=currency,
        overpayment_of_duties=overpayment_of_duties,
        overpayment_vostok=overpayment_vostok, 
        overpayment_di=overpayment_di,
        overpayment_other_business_verticals=overpayment_other_business_verticals,
        underpayment_of_duties=underpayment_of_duties,
        underpayment_vostok=underpayment_vostok,
        underpayment_di=underpayment_di,
        underpayment_other_business_verticals=underpayment_other_business_verticals,
        key_audit_findings=key_audit_findings,
        key_issues=key_issues,
        vostok_broker_errors=vostok_broker_errors,
        vostok_beagle_errors=vostok_beagle_errors,
        di_broker_errors=di_broker_errors,
        di_beagle_errors=di_beagle_errors,
        other_business_broker_errors=other_business_broker_errors,
        other_business_beagle_errors=other_business_beagle_errors,
        broker_error_sim_details=broker_error_sim_details,
        beagle_error_sim_details=beagle_error_sim_details,
        status=status ) 
    
    #query execution
    db_conn.execute(query.where(
        (assignment.columns.audit_vertical == audit_vertical) & 
        (assignment.columns.region == region) &
        (assignment.columns.month_of_import == month_of_import) &
        (assignment.columns.year_of_import == year_of_import)))
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Update" : "successfull"
    }

@app.put('/update/quality_audit')
async def update_row(audit_vertical,region,month_of_import, year_of_import,auditor,quality_auditor,status_of_qa,date_of_sharing_data_with_qa,qa_remark,qa_financial_impact,audit_accuracy_before_qa_calibration,audit_accuracy_after_qa_calibration,delacaration_accuracy_before_qa,delacaration_accuracy_after_qa ):
    
    #query
    query = update(quality_audit).values(
        audit_vertical= audit_vertical, 
        region= region,
        month_of_import=month_of_import,
        year_of_import=year_of_import,
        auditor= auditor,
        quality_auditor=quality_auditor,
        status_of_qa=status_of_qa,
        date_of_sharing_data_with_qa=date_of_sharing_data_with_qa,
        qa_remark=qa_remark,
        qa_financial_impact=qa_financial_impact,
        audit_accuracy_before_qa_calibration=audit_accuracy_before_qa_calibration,    
        audit_accuracy_after_qa_calibration=audit_accuracy_after_qa_calibration,
        delacaration_accuracy_before_qa=delacaration_accuracy_before_qa,
        delacaration_accuracy_after_qa=delacaration_accuracy_after_qa ) 
    
    #query execution
    db_conn.execute(query.where(
        (assignment.columns.audit_vertical == audit_vertical) & 
        (assignment.columns.region == region) &
        (assignment.columns.month_of_import == month_of_import) &
        (assignment.columns.year_of_import == year_of_import)))
    #data=db_conn.execute(assignment.select()).fetchall()
    return {
        "Update" : "successfull"
    }   
