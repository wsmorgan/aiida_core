#!/usr/bin/env python
import sys
import os

def launch_ws():

    """
    To control the wf_stauts use the procedure 
    
    wf.list_workflows() 
    
    and to force the retrival of some calculation you can use the function
    
    wf.retrieve_by_uuid(uuid_wf).finish_step_calculations(methohd_wf)
    
    """
        
    from aiida.orm import Calculation, Code, Computer
    computer = Computer(hostname="localhost",transport_type='local',scheduler_type='pbspro')
    computer.set_workdir("/tmp/{username}/aida")
    computer.store()
    
    import aiida.orm.workflow as wf
    from aiida.workflows import wf_demo
    from aiida.common.datastructures import wf_states
    
    params = {}
    params['nmachine']=2

    w = wf_demo.WorkflowDemo()
    w.set_params(params)
    w.start()
    
    w = wf_demo.WorkflowDemoBranch()
    w.set_params(params)
    w.start()