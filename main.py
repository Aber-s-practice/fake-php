from indexpy import Index
from indexpy.routing import FileRoutes, ASGIRoute
from indexpy.http.responses import RedirectResponse

app = Index()
app.router.extend(FileRoutes("views", suffix=".php"))
app.router.append(
    ASGIRoute("/", RedirectResponse("/home.php"), name=None, type=("http",))
)
