[20:52:36] Loading DB...                                                                                      main.py:95
[20:52:44] DB loaded                                                                                          main.py:99
[20:52:45] Loading tasks...                                                                                   main.py:62
  100/100         DB loaded       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00 0:00:08
⠇  399077/1255301 Loading Tasks   ━━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━━  32% 0:00:41 0:00:17
⠇       0/1255301 Making Requests ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   0% -:--:-- -:--:--
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 113, in <module>
    asyncio.run(
  File "C:\Program Files\Python310\lib\asyncio\runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "C:\Program Files\Python310\lib\asyncio\base_events.py", line 646, in run_until_complete
    return future.result()
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 66, in concurrent_scheduler
    resp = json.loads(db[key])["Response"]
  File "C:\Program Files\Python310\lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Program Files\Python310\lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Program Files\Python310\lib\json\decoder.py", line 353, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Invalid \escape: line 1 column 296 (char 295)
Task exception was never retrieved
future: <Task finished name='Task-24' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-23' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-22' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-21' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-20' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-19' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-18' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-17' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-16' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-15' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-14' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-13' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-12' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-11' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-10' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-9' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-8' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-7' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-6' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-5' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-4' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-3' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed
Task exception was never retrieved
future: <Task finished name='Task-2' coro=<bound_fetch() done, defined at C:\Users\xeon7\Downloads\imdb\main.py:36> exception=RuntimeError('Session is closed')>
Traceback (most recent call last):
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 39, in bound_fetch
    data = await fetch(url, session)
  File "C:\Users\xeon7\Downloads\imdb\main.py", line 29, in fetch
    async with session.get(url) as response:
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 1138, in __aenter__
    self._resp = await self._coro
  File "C:\Users\xeon7\AppData\Roaming\Python\Python310\site-packages\aiohttp\client.py", line 399, in _request
    raise RuntimeError("Session is closed")
RuntimeError: Session is closed