from fastapi import APIRouter,Depends,status,HTTPException, Response
from sqlalchemy.orm import session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import model
from .. import database,schemas,util,oauth2


router= APIRouter(
     tags=['Authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(user_creadential:OAuth2PasswordRequestForm=Depends(), db:session=Depends(database.get_db)):
    user=db.query(model.user).filter(model.user.email==user_creadential.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail=f"Invalid creadential")
    if not util.verify(user_creadential.password,user.password):
          raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail=f"Invalid creadential")
    access_token= oauth2.create_access_token(data={"user_id":user.id})
    
    return {"access_token": access_token,"token_type":"bearer"}



