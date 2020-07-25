from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.responses import FileResponse
from starlette.routing import Route, Mount
from print_boleto import print_boleto_html, print_boleto_pdf


def homepage(request):
    return PlainTextResponse('Hello, world!')


def user_me(request):
    username = "John Doe"
    return PlainTextResponse('Hello, %s!' % username)


async def boleto_html(request):
    uuid = request.path_params['uuid']
    print_boleto_html(uuid)
    return FileResponse('boleto/' +   uuid + '.html')


async def boleto_pdf(request):
    uuid = request.path_params['uuid']
    print_boleto_pdf(uuid)
    return FileResponse('boleto/' +   uuid + '.pdf')


def user(request):
    username = request.path_params['username']
    return PlainTextResponse('Hello, %s!' % username)


def startup():
    print('Ready to go')


routes = [
    Route('/', homepage),
    Route('/boleto/html/{uuid}', boleto_html),
    Route('/boleto/pdf/{uuid}', boleto_pdf),
    Route('/user/{username}', user),


]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
