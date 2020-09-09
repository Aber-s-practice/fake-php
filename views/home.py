from indexpy.http import HTTPView
from indexpy.http.responses import HTMLResponse


class HTTP(HTTPView):
    async def get(request):
        return HTMLResponse('home <a href="/about.php">about</a>')
