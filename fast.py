from typing import Optional
from fastapi import FastAPI
from enum  import Enum

app = FastAPI()

@app.get("/")
def read_index():
    return 'How are you!'

@app.get('/')
def get():
    return "how are you"
@app.get('/id',tags = ['blog'])
def get(id):
    return {'message':'id is provided'}

@app.get('/blog/{id}', tags = ['blog'])
def get_blog(id):
    return {'message': f'blog with id {id}'}
@app.get(
    '/blog/all',
    tags = ['blog'],
    summary = 'retrive all blogs',
    description = 'This api call simulate fetching all blogs',
    response_description = 'The list of  available blogs'
)  




def get_all_blog ( page = 1 ,page size:optional[int]= None,):
     return('message'f'blog provided')
@app.get('/blog', tags = ['blog'])
def get_all_blog (page ,page_siz):
    return{'message':f'all{page_size}blogs on page{page}'}
@app.get('/blog/{id}/comment/{co'message': f'all{page_size} blogs on page {page}'}comment_id}',tags = ['blog','comment'])
def get_comment(id:int,comment_id:int,valid:bool=True,username:Optional[str] = None):
    """
    simulates retriving a comment of a blog

    - **id** mandatry path parameter
    - **comment_id** mandatery path perameter
    - **valid** optional query perameter
    - **username** optional query perameter
    """
    return{'message':'blog_id{id},comment_id{comment_id},valid{valid},username{username}'}

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
#operation description
#we talk about status code which basically lets the caller know what outcome of the operation was
#we will see the manipulate the status code based on some internal functionality
#tag so tag are basically away to structureour endpoint  in different logic way
#summary and description
#which are two very important way in which we can textually describe our endpoints and what exectly
#they do so that we give more in
#@app.get('/blog/{id}',status_code = 404)
#def get_blog(id: int):
    #if id>5:
        #return {'error':f'blog is not found'}
    #else:
        #return{'message': f'blog with id {id}'}
#tags allow us to  structure and organize our operations within  a single file so we are catogerize
#so for instance we have when we define the tag we have a list  the amount of the number of strinng
#we provide and that list equal the number ofcategorise that operation will be placed there
#operaton based on the string that we provide in the tags and also we can provide multiplescatogrise
#two more pieces of information that we can add our operation are summary and description
#there are basically information that we provide mainlyfor our documentation purpose,riht
#so for people who are using our API they are typing to finger out what a method does 
#we can provide more informationhsing summary and description
#info regarding operation
#@app.get(
    #'blog/all',
    #tags = ['blog'],
    #summary = 'retrive all blogs',
    #description 'This api calls simulate fetching all blogs'
#)
#Description also takenfrom function docstring
#Status code
#Ye batata hai ki API ka default HTTP response code kya hoga.
#By default har endpoint 200 OK deta hai, lekin aap isko change kar sakte ho.
@app.get('/blog/all',status_code = 200)
def get_all_blog(page,page_size):
    return{'message':f'all{page_size} blogs on page {page}'}
#tags
#Tags endpoints ko group karne ke liye hote hain.
#Agar aapke project me bohot saare endpoints hain (Users, Blogs, Comments, etc.),
# to tags use karke aap unhe categories me divide kar sakte
@app.get('/blog/{id}/comment/{comment_id}',tags = ['blog','comment'])
def get_comment(id:int,comment_id:int,valid:bool=True,username:Optional[str] = None):
#summary
#Ye ek short one-line title hota hai jo endpoint ke upar show hota hai Swagger docs me
 @app.get(
     '/blog/all',
    tags = ['blog'],
    summary = 'retrive all blogs',
    description = 'This api call simulate fetching all blogs',
    response_description = 'The list of  available blogs'
)
#description
#Ye endpoint ka detailed explanation hota hai.
    
 @app.get(
    '/blog/all',
    tags = ['blog'],
    summary = 'retrive all blogs',
    description = 'This api call simulate fetching all blogs',
    response_description = 'The list of  available blogs'
)  




#respons description
#Ye batata hai ki response ka meaning kya hai.
#Isse API consumer ko clear ho jata hai ki response actually kya represent karta hai.

 @app.get(
    '/blog/all',
    tags = ['blog'],
    summary = 'retrive all blogs',
    description = 'This api call simulate fetching all blogs',
    response_description = 'The list of  available blogs'
)  
 @app.get('/blog/{id}/comment/{comment_id}',tags = ['blog','comment'])
 def get_comment(id:int,comment_id:int,valid:bool=True,username:Optional[str] = None):
    """
    simulates retriving a comment of a blog

    - **id** mandatry path parameter
    - **comment_id** mandatery path perameter
    - **valid** optional query perameter
    - **username** optional query perameter
    """
    return{'message':'blog_id{id},comment_id{comment_id},valid{valid},username{username}'}

