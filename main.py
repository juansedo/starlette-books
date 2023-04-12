from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route

import src.routes.books as books


async def index(request: Request):
    return PlainTextResponse(content="Hello, world!")


routes = [
    Route("/", endpoint=index),
    *books.routes,
]

app = Starlette(
    debug=True,
    routes=routes,
)
