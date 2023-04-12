from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

from src.database.models.books import BookRepository


def getAll(request: Request):
    books = BookRepository.getAll()
    response = {
        "data": books,
        "count": len(books),
        "message": "Books retrieved",
    }
    return JSONResponse(content=response)

def getOne(request: Request):
    id = request.path_params.get('id')
    book = BookRepository.getOne(id)
    return JSONResponse(content=book)

async def createOne(request: Request):
    try:
        body = await request.json()
        BookRepository.createOne(body)
        return JSONResponse(content={"message": "Book created!"})
    except KeyError as e:
        return JSONResponse(status_code=400, content={"message": "Missing parameter: " + str(e)})
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": "Book not created!"})

routes = [
    Mount('/books', routes=[
        Route('/', endpoint=getAll, methods=['GET']),
        Route('/', endpoint=createOne, methods=['POST']),
        Route('/{id:int}', endpoint=getOne, methods=['GET']),
    ])
]
