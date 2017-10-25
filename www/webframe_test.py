from aiohttp import web
import asyncio
from coroweb import add_routes,add_static
#from coroweb import add_routes,add_static
#  .coroweb: ModuleNotFoundError: No module named '__main__.coroweb'; '__main__' is not a package


from app import init_jinja2,datetime_filter,logger_factory,response_factory
import logging; logging.basicConfig(level=logging.INFO)

import orm
from config.config import config

#编写web框架测试
async def init(loop):
    await orm.create_pool(loop, **config['db'])
    app = web.Application(loop=loop,middlewares=[logger_factory,response_factory])
    init_jinja2(app,filters=dict(datetime=datetime_filter),path = r"/Users/lingli/PycharmProjects/awesome/www/templates")#初始化Jinja2，这里值得注意是设置文件路径的path参数
    add_routes(app,'webframe_test_handler')
    add_static(app)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()