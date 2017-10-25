import asyncio
from coroweb import get,post
from models import User

#编写用于测试的URL处理函数
# @get('/')
# async def handler_url_blog(request):
#     body='<h1>Awesome</h1>'
#     return body
# @get('/greeting')
# async def handler_url_greeting(*,name,request):
#     body='<h1>Awesome: /greeting %s</h1>'%name
#     return body


@get('/')

async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
