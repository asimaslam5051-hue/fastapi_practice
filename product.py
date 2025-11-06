from fastapi.responses import Response,HTMLResponse,PlainTextResponse
from fastapi import APIRouter,Header,Cookie,Form
from typing import Optional,List
router = APIRouter(
   prefix="/product",
   tags=["product"]
)

products = ['watch', 'camera', 'phone']

@router.post("/product/")
def create_product(name: str = Form(...), price: int = Form(...)):
    return {"name": name, "price": price}
products = ['watch', 'camera', 'phone']
@router.post('/new')
def create_product(name:str = Form(...)):
   products.append(name)
   return products



@router.get('/all')
def get_all_products():
    #return products
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key = "test_cookie",value="test_cookie_value")
    return response

@router. get('/withheader')
def get_products(
  response:Response,
  test_cookie:Optional[str] = Cookie(None),
  custom_header: Optional[List[str]]=Header(None),
  ):
  if custom_header:
    response.headers['custom_response_header'] = " and ".join(custom_header)
  return {
     'data':  products,
     'custom_header': custom_header,
     'my_cookie' : test_cookie
  }  
@router.get('/{id}', responses={
    202:{
      "content":{
       "text/html":{
         "example":"<div>product</div>"

       }

      },
      "Description": "Returns the HTML for an object"
    },
    404:{
       "content":{
        "text/Plain":{
         "example":"product not found"

       }

      },
      "description": "A cleartext error message"
    }

    
})
def get_product(id:int):
    if id > len(products):
        out ='product not available'
        return PlainTextResponse(status_code=404, content=out, media_type="text/html")
    else:    
      product = products[id]
      out = f"""
      <header>
        <style>
        .product{{
         weidth : 500px;
         height:  300pk;
         border:  2px inset green;
         background_colour: lightblue;
         text aline: center;
      }}
        </style>
      </head>
      <div class ="product">{product}</div>
      """
      return HTMLResponse(content=out, media_type="text/html")

