import www.orm, asyncio
from www.models import User, Blog, Comment


async def test(loop):
    await www.orm.create_pool(loop, user='root', passwd='pass', db='awesome')
    u = User(name='Test5', email='test5@example.com', passwd='123456780', image='about:blank')
    await u.save()
    a = await u.findAll()  # 这个要打印才显示出来
    print(a)


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
www.orm.__pool.close()  # 在关闭event loop之前，首先需要关闭连接池。
loop.run_until_complete(www.orm.__pool.wait_closed())  # 在关闭event loop之前，首先需要关闭连接池。
loop.close()