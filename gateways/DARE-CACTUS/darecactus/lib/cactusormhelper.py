import darecactus.model as model
import darecactus.model.meta as meta
import time
from sqlalchemy.sql import and_, or_
import os
#contains various job manipulation techniques

einstientoolkit_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'DARE', 'examples', 'cactus', 'einsteintoolkit.th')


#User JOB status
LOCAL_QUEUE   = 1
NEW = 1
RUNNING = 2
FAILED  = 3
DONE    = 4


#Extra Launched BigJob status
SCHEDULER_QUEUE = 5

thorns_default=['einsteintoolkit.th']

        
def add_job(userid):
    #.first()
    status ="Queue"
    """adds a job to the queue"""
    job_queue = model.job()
    job_queue.status = str(1)
    job_queue.userid = str(userid)
    job_queue.submitted_time = time.asctime()
    
    meta.Session.add(job_queue)
    meta.Session.commit()

    #to find ID 
    njob = meta.Session.query(model.job)
    job = njob.filter(model.job.submitted_time == str(job_queue.submitted_time)).one()
    
    return job.id

def add_allnewjobinfo(cleaned_data, jobid):
    
    for key in cleaned_data:
        newjobinfo = model.jobinfo()
        newjobinfo.key = key                    
        newjobinfo.value = cleaned_data[key]
        newjobinfo.submitted_time = time.asctime()
        newjobinfo.jobid = jobid
        meta.Session.add(newjobinfo)
    
    meta.Session.add(newjobinfo)


def add_newjobinfo(key, value, jobid):
    
    newjobinfo = model.jobinfo()
    newjobinfo.key = key                    
    newjobinfo.value = value
    newjobinfo.submitted_time = time.asctime()
    newjobinfo.jobid = jobid
    
    meta.Session.add(newjobinfo)
    meta.Session.commit()

def add_param(paramfile, jobid):
    
    newparam = model.paramlist()
    newparam.jobid = jobid
    newparam.description = "desc"
                        
    newparam.submitted_time = time.asctime()
    newparam.filename = str(paramfile.filename).replace(" ", "_")
    
    mmm=paramfile.file.read() 
    newparam.paramfile = mmm 
    meta.Session.add(newparam)
    meta.Session.commit()

def get_paramfile(jobid):
    
    params = meta.Session.query(model.paramlist)
    param = params.filter(model.paramlist.jobid == int(jobid)).one()

    return param.filename, param.paramfile


def add_thorn(userid, desc, thornfile):
    
    newthorn = model.thornlist()
    newthorn.userid = userid
    newthorn.description = desc
                        
    newthorn.submitted_time = time.asctime()
    newthorn.filename = str(thornfile.filename).replace(" ", "_")
    
    mmm=thornfile.file.read() 
    newthorn.thornfile = mmm 
    meta.Session.add(newthorn)
    meta.Session.commit()


def get_thornfile(thornid):

    if thornid.lower() == 'einsteintoolkit.th':
        return thornid.lower(), file(einstientoolkit_file,'r').read()
    else:    
        thorns = meta.Session.query(model.thornlist)
        thorn = thorns.filter(model.thornlist.id == int(thornid)).one()   
        return thorn.filename, thorn.thornfile

def get_job_file(jobid, file_type):

    if (file_type == 'thorn'):
        thorn_id = get_jobinfo_detail(jobid, 'thornlist')
        return get_thornfile(thorn_id[0].value)
    else:
         return get_paramfile(jobid)

def get_jobinfo_detail(jobid, jobinfokey):
    all_jobinfo = meta.Session.query(model.jobinfo)
    return all_jobinfo.filter(and_(model.jobinfo.jobid == jobid, model.jobinfo.key ==jobinfokey)).all()
    

def get_thornlist(userid):

    all_thorns = meta.Session.query(model.thornlist)
    user_thorns = all_thorns.filter(model.thornlist.userid==userid).all()   

    default_thorn = model.thornlist()
    default_thorn.description = 'this is default'
    default_thorn.id= 'default'                    
    default_thorn.submitted_time = 'default'
         
    default_thorn.filename = 'einsteintoolkit.th'
    default_thorn.thornfile  = file(einstientoolkit_file)
        
    user_thorns.append(default_thorn)
    
    return user_thorns
    
def get_thornlist_job(userid):

    all_thorns = meta.Session.query(model.thornlist)
    user_thorns = all_thorns.filter(model.thornlist.userid==userid).all()   
    
    thorns=[]
    
    for thorn in  user_thorns:
        thorns.append([thorn.id,thorn.filename])
    
    for thorn in thorns_default:   
        thorns.append([thorn,thorn])
        
    return thorns


def get_jobinfo(jobid):
    #to find ID 
    jobinfo = meta.Session.query(model.jobinfo)
    new_jobinfo = jobinfo.filter(model.jobinfo.jobid == jobid)
    return new_jobinfo


def get_jobtype(jobid):
    #to find ID 
    jobinfo = meta.Session.query(model.jobinfo)
    new_jobinfo = jobinfo.filter(and_(model.jobinfo.jobid ==jobid\
                 , model.jobinfo.key == "appname")).one()
    
    return new_jobinfo.value

def get_jobinfoids(jobid):
    #to find ID 
    jobinfo = meta.Session.query(model.jobinfo)
    new_jobinfo = jobinfo.filter(model.jobinfo.jobid == jobid)
    newjobinfoids =[]     
    if (new_jobinfo):
        for jq in new_jobinfo:
            newjobinfoids.append(jq.id) 
    else:
        newjobinfoids.append("nojobinfo")
        
    return newjobinfoids

    
def get_jobid(jobinfoid):
    #to find ID 
    jobinfo = meta.Session.query(model.jobinfo)
    new_jobinfo = jobinfo.filter(model.jobinfo.id == jobinfoid)
    newjobinfoids =[] 
    
    if (new_jobinfo):
        jobid = jq.id 
    else:
        jobid= "nojobid"
    return jobid
            
def del_job(jobid):
    
    """deletes a job from the jobs"""
    jobs =  meta.Session.query(model.job).get(jobid)
    meta.Session.delete(jobs)

    """deletes a job from job info table"""
    jobinfo = meta.Session.query(model.jobinfo)
    jobsinfo =  jobinfo.filter(model.jobinfo.jobid==jobid).all()
    for deljobsinfo in jobsinfo:
        meta.Session.delete(jobsinfo) 
    meta.Session.commit()  
            
def update_job_status(jobid, status):
    """updates a job status from the queue"""
    jobs_q =  meta.Session.query(model.job)
    jq =  jobs_q.filter(model.job.id==jobid).one()
    jq.status = str(status)
    meta.Session.commit()
    
def update_job_pid(jobid, pid):
    """updates a job status from the queue"""
    jobs_q =  meta.Session.query(model.job)
    jq =  jobs_q.filter(model.job.id==jobid).one()
    #print "updating",jobid, pid  
    jq.dareprocess_id = str(pid)
    meta.Session.commit()  
    
def get_job_pid(jobid):
    #to find ID 
    job= meta.Session.query(model.job)
    new_job = job.filter(model.job.id ==jobid).one()
    pid = new_job.dareprocess_id
    if (pid==""):
        pid = None
    return pid
    
    
def update_job_detail_status(jobid, detail_status):

    """updates a job status from the queue"""
    jobs_q =  meta.Session.query(model.job)
    jq =  jobs_q.filter(model.job.id==jobid).one()
    jq.detail_status = str(detail_status)
    meta.Session.commit()    
    

def check_new_jobs():
    jobs =  meta.Session.query(model.job)
 
  # jobs that are in queue
    new_jobs =  jobs.filter(model.job.status==str(1)).all()    
    newjobids =[] 
    
    if (new_jobs):
        for jq in new_jobs:
            newjobids.append(jq.id) 
    else:
        newjobids.append("nojobs")     
    print "check new jobs Done",newjobids
    return newjobids
    

""" absolete
def update_jobinfo_status(jobinfoid, status):
    #updates a job status from the queue
    jobid = get_jobid(jobinfoid)
    
    #apply statuses here remote queue but running launched
    if (status ==status):
        ustatus = status
        
    update_job_status(jobid, ustatus)
    jobs_q =  meta.Session.query(model.jobinfo)
    jq =  jobs_q.filter(model.jobinfo.id==jobinfoid).one()
    jq.status = str(status)
    meta.Session.commit()
"""
