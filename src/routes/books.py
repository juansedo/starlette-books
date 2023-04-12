from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

from src.database.models.books import BookRepository


def getAll(request: Request):
    books = BookRepository.getAll()
    response = {
        "message": "Books retrieved",
        "books": books,
        "count": len(books)
    }
    return JSONResponse(content=response)

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
