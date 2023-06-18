from fastapi import FastAPI,Response, status,HTTPException,Depends,APIRouter
from .. import model,schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import Optional,List
from .. import oauth2
from sqlalchemy import func

router= APIRouter(
    prefix="/post",
    tags=['post']
)

#@router.get("/",response_model=List[schemas.post])
@router.get("/",response_model=List[schemas.postOut  ])
def get_post( db:Session=Depends(get_db), current_user:id=Depends(oauth2.get_current_user), limit:int=10, skip:int=0,
             search:Optional[str]=""):
    # posts=db.query(model.post).filter(model.post.title.contains(search)).limit(limit).offset(skip).all()
     posts= db.query(model.post, func.count(model.Votes.posts_id).label("votes")).join(model.Votes, model.Votes.posts_id==model.post.id, isouter=True).group_by(model.post.id).filter(model.post.title.contains(search)).limit(limit).offset(skip).all()
     #print(search)
     #cursor.execute("select * from posts")
     #posts=cursor.fetchall()
     #print(posts)
     #formatted_results = [{"post": post_id, "votes": votes} for post_id, votes in results]
     
     
     return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.post)
def create_post(post: schemas.createPost, db:Session=Depends(get_db), current_user:id=Depends(oauth2.get_current_user)):
    print(current_user.email)
    new_post=model.post(owner_id=current_user.id, **post.dict())
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    #cursor.execute("INSERT INTO POSTS(title,content,published) VALUES(%s, %s, %s) RETURNING *", (post.title,post.content,post.published))
    #new_post= cursor.fetchone()
    #conn.commit()
    return new_post
@router.get("/{id}",response_model=schemas.postOut)
def get_post(id:int,db:Session=Depends(get_db),current_user:id=Depends(oauth2.get_current_user)):
   
    #post= db.query(model.post).filter(model.post.id==id).first()
    post=db.query(model.post, func.count(model.Votes.posts_id).label("votes")).join(model.Votes, model.Votes.posts_id==model.post.id, isouter=True).group_by(model.post.id).filter(model.post.id==id).first()
    #cursor.execute("select * from posts where id= %s",(str(id)))
    #post=cursor.fetchone()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not exit")
        #response.status_code= status.HTTP_404_NOT_FOUND
        #return{"message":f"post with id:{id} was not exit"}
    
    
    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db:Session=Depends(get_db),current_user:id=Depends(oauth2.get_current_user)):
    #cursor.execute("delete from posts where id=%s returning *",(str(id),))
    #deleted_post= cursor.fetchone()
    #conn.commit()
    deleted_post= db.query(model.post).filter(model.post.id==id)
    post= deleted_post.first()
   
    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found")
    deleted_post.delete(synchronize_session=False)

    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
   
   
    db.commit()
   
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.post)
def update_post(id:int,updated_post:schemas.createPost,db:Session=Depends(get_db),current_user:id=Depends(oauth2.get_current_user)):
    #cursor.execute("update posts set title= %s, content= %s, published= %s where id=%s returning*", (post.title,post.content,post.published,str(id)) )
    #updated_post= cursor.fetchone()
    #conn.commit()
    post_query=  db.query(model.post).filter(model.post.id==id)
    post=post_query.first()

    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found")
    post_query.update(updated_post.dict(),synchronize_session=False)

    if  post.owner_id!=current_user.id:
        

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    db.commit()
   
    return post_query.first()