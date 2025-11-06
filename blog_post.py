from fastapi import FastAPI,APIRouter,Query,Body,Path,Depends,status,Response
from pydantic import BaseModel
from typing import Optional,List,Dict
from enum import Enum
router1 = APIRouter(
prefix = '/post',
tags = ['post']
)


class BlogCreate(BaseModel):
    title: str
    content:str
    published: Optional[bool]

@router1.post('/new')
def creat_blog(blog: BlogCreate):
    return {'data': blog}
class image(BaseModel):
    url:str
    alias:str

class BlogUpdate(BaseModel):
    title:  str
    content: str
    published: Optional[bool]
    tag : list[str] =["tag1","tag2"]
    metedata:dict[str,str] ={'str1':'val1'}
    image:Optional[image]=None
router2 = APIRouter(
prefix = '/put',
tags = ['put']
)

@router2.put('/new/{id}')
def creat_blog(blog: BlogUpdate, id: int, version: int = 10):
    return {
        'id': id,
        'data': blog,
        'version': version
        }

router3 = APIRouter(
prefix = '/post',
tags = ['post']
)

@router3.patch('/new/{id}/comment/{comment_id}')
def creat_comment (
    blog: BlogUpdate, id: int, 
    comment_title: Optional[int] = Query(None,

        title ='title of the comment',
        description ='some description for comment_title',
        alias ='commentTitle',
        deprecated =True
    ),
    content: str = Body(
        ...,
        min_lenght =10,
        max_lenght =120,
        regex="^[a-z\s]*$",
        
    ),
    v: Optional[List[str]] = Query(['1.0', '1.1', '1.2','1.3']),
    comment_id: int = Path(gt=5, le=10)
):
    return{
        'blog': blog,
        'id': id,
        'comment_tile': comment_title ,
        'content': content,
        'version': v,
        'comment_id': comment_id 
    }
def required_functionality():
    return{"message": "Learning the fastAPI is important"}

@router3.get(
    "/all",
    tags=["blog"],
    summary="Retrieve all blogs",
    description="This API call simulates fetching all blogs",
    response_description="The list of available blogs"
)
def get_blog(page: int = 1, page_size: Optional[int] = None, req_parameter: Dict = Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}"}

@router3.get("/{id}/comment/{comment_id}", tags=["comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    
    - **id**: mandatory path parameter  
    - **comment_id**: mandatory path parameter  
    - **valid**: optional query parameter  
    - **username**: optional query parameter  
    """
    return {"message": f"blog_id={id}, comment_id={comment_id}, valid={valid}, username={username}"}

class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@router3.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type: {type}"}

@router3.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog_by_id(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}   
router4 = APIRouter(
prefix = '/blog',
tags = ['blog']
)

@router4.delete('/new')
def delete_blog():
    pass