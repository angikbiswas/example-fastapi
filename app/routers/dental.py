from fastapi import Request,Response,Depends,APIRouter
# from .. import model,schemas
from .models import *
from ..schema import connect,execute


router= APIRouter(
    prefix="/dental",
    tags=['dental']
)

@router.get("/")
async def getAll(request:Request):
    result=await connect("select * from evt_denti_o.dent_excep_thrshld_maint")
    print(result)
    return result
@router.put("/")
async def updateRec(body:thresoldupdate):
    # query=f"insert into evt_denti_o.thrshld_excep_dent_maint()"
    print(body)
    return body