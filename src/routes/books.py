from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route


def getAll(request: Request):
    return JSONResponse(content={"message": "Hello, world!"})

def getOne(request: Request):
    id = request.path_params.get('id')
    return JSONResponse(content={"message": f"Book {id}"})

def createOne(request: Request):
    return JSONResponse(content={"message": "Book created!"})

routes = [
    Mount('/books', routes=[
        Route('/', endpoint=getAll, methods=['GET']),
        Route('/', endpoint=createOne, methods=['POST']),
        Route('/{id:int}', endpoint=getOne, methods=['GET']),
    ])
]
