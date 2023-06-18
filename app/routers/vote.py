from fastapi import FastAPI,Response, status,HTTPException,Depends,APIRouter
from .. import schemas, model, database, oauth2
from sqlalchemy.orm import Session
from ..database import get_db


router=APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db:Session=Depends(get_db), current_user:id=Depends(oauth2.get_current_user)):

    post=db.query(model.post).filter(model.post.id == vote.posts_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {vote.posts_id} doesn't exist")

    vote_queary= db.query(model.Votes).filter(model.Votes.posts_id== vote.posts_id, model.Votes.users_id== current_user.id)
    found_vote= vote_queary.first()
    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user  {current_user.id} already voted on post {vote.posts_id}")
        new_vote=model.Votes(posts_id=vote.posts_id, users_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote doesn't exist")
        vote_queary.delete(synchronize_session=False)
        db.commit()
        return {"messege":"successfully deleted vote"}
        