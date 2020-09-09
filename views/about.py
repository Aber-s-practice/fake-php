from indexpy.http import HTTPView


class HTTP(HTTPView):
    async def get(request):
        return "about"
