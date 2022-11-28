import asyncio
import functools
import aiohttp
from socket import AF_INET
from typing import Optional, Any


SIZE_POOL_AIOHTTP = 100


# Stolen from stella
# https://github.com/InterStella0/stella_bot/blob/master/utils/decorators.py#L70-L79
def in_executor(loop=None):
    """Makes a sync blocking function unblocking"""
    loop = loop or asyncio.get_event_loop()

    def inner_function(func):
        @functools.wraps(func)
        def function(*args, **kwargs):
            partial = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, partial)

        return function

    return inner_function


class SingletonAiohttp:
    sem: Optional[asyncio.Semaphore] = None
    aiohttp_client: Optional[aiohttp.ClientSession] = None

    @classmethod
    def get_aiohttp_client(cls) -> aiohttp.ClientSession:
        if cls.aiohttp_client is None:
            timeout = aiohttp.ClientTimeout(total=2)
            connector = aiohttp.TCPConnector(family=AF_INET, limit_per_host=SIZE_POOL_AIOHTTP)
            cls.aiohttp_client = aiohttp.ClientSession(timeout=timeout, connector=connector)

        return cls.aiohttp_client

    @classmethod
    async def close_aiohttp_client(cls) -> None:
        if cls.aiohttp_client:
            await cls.aiohttp_client.close()
            cls.aiohttp_client = None

    @classmethod
    async def query_url(cls, url: str) -> Any:
        client = cls.get_aiohttp_client()

        try:
            async with client.post(url) as response:
                if response.status != 200:
                    return {"ERROR OCCURED" + str(await response.text())}

                json_result = await response.json()
        except Exception as e:
            return {"ERROR": e}

        return json_result


async def on_start_up() -> None:
    SingletonAiohttp.get_aiohttp_client()


async def on_shutdown() -> None:
    await SingletonAiohttp.close_aiohttp_client()
