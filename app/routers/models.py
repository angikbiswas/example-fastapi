import datetime
from pydantic import Field,BaseModel
from typing import Any, Optional

class thresoldupdate(BaseModel):

    dent_excep_attrib_key:int 
    acct_num:str
    updt_ts: Optional[datetime.datetime] =Field(readOnly=True)
    updt_usr_id :Optional[str]=Field(default='svc_evt_batch')
    excep_thrshid_pct:int
    eff_dt:datetime.date 
    expirn_dt:datetime.date
    dent_excep_attrib_nm :Optional [str]=Field(default='subscriber count check') 
    note_txt:Optional [str]=Field(default='null')
    appry_usr_id:Optional [str]
    appry_ts:Optional[datetime.date]
    mast_case_id:Optional [str]=Field(default='null')