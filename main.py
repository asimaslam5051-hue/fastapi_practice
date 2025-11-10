#importing fastapi importing fastapi class from fastapi package
from fastapi import FastAPI
#create an instance of the FastAPI class.
#This object (app) will contain all your API routes, configuration, and middleware.
app = FastAPI()
#Creating a Route (Endpoint)
@app.get("/")
#function That Handles the Request
def read_index():
    return "Hello from FastAPI!"

from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def get():
    return "hello word"

#feature
#Automatic documentation
#FastApi automatically genrates for us the documentation for the endpoint
#.swagger
#RerDOC
#standered python3
#its a modern UI and modern API it uses standered pythobn
#security and authentication
#security and authentication is integrated and there are multiple type of security that we can use.
#dependency injection is also one of  the also one of the main feature of this framework
#we have multiple injection of dependency injection  for instance and we have multiple levels 
#so dependencies can have their own dependencies and so on
#and validation is handeled automatically for us and so on and so fath
#testing _ coverage 100%
#testin in fast api give 100 percent coverage
from typing import Optional
from fastapi import FastAPI
from enum  import Enum
app = FastAPI()

@app.get('/hello')
def index():
    return {"good!"}

@app.get('/about')
def index2():
    return {'message': 'Hi!'}
#@app.get('/blog/all')    
#def get_blog_all():
    #return{'message': 'blog is provided'}

#Query parameter (page, page_size) any function parameter not part of the path  
@app.get('/blogs/all')
def get_all_blogs(page, page_size):
    return{'message': f"all{page_size}blogs on page {page}"}
#default value and optional_value
@app.get('/blog/all')
def get_all_blog(page = 10, page_size: Optional[int] = None):
    return{'message': f'all{page_size}blogs on page{page}'}
@app.get('/blog/{id}/comments/{comments_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str]= None):
    return{'message': f'blog_id{id}, comment_id'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto =  'howto'

@app.get('/blog/type/{type}')
def _get_blog_type(type: BlogType):
    return{'message': f'Blog type{type}'}



#pathparameter
@app.get('/blog/{id}', tags = ['blog','comment'])
def get_blog(id):
    return{'message': f'blog with id {id}'}
 

def get_all_blog():
     return('message'f'blog provided')
@app.get('/blog', tags = ['blog'])
def get_all_blog (page ,page_siz):
    return{'message': f'all{page_size} blogs on page {page}'}
@app.get('/blog/{id}/comment/{comment_id}',tags = ['blog','comment'])
def get_comment(id:int,comment_id:int,valid:bool=True,username:Optional[str] = None):
    """
    simulates retriving a comment of a blog

    - **id** mandatry path parameter
    - **comment_id** mandatery path perameter
    - **valid** optional query perameter
    - **username** optional query perameter
    """
    return{'message':f'blog_id{id},comment_id{comment_id},valid{valid},username{username}'}

class BlogType(str, Enum):
    short =  'short'
    story =  'story'
    howto =  'howto'


@app.get('/blog/type/{type}', tags = ['blog'])
def _get_all_blog_type(type: BlogType):
    return{'message'f'Blog_type{type}'}


def get_blog(id: int):
    if  id > 3:
        return {'error':f'blog is not found'}
    else:
        return{'message':f'blog wit id{id}'}
#Request Body