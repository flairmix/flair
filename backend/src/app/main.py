from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.static_files import StaticFilesConfig

from .api.files import FileController
from .api.auth import register, login
from .api.routes import generate_route
from .services.db import init_db
from .api.post import PostController
from .api.water_controller import WaterController

init_db()


app = Litestar(
    route_handlers=[register, login, 
                    generate_route, 
                    FileController,
                    PostController,    
                    WaterController,    
                    ],
    openapi_config=OpenAPIConfig(
        title="Flair API",
        version="1.0.0"
    ),
    static_files_config=[
        StaticFilesConfig(path="/static", directories=["output"])
    ]
)


# set ENV=dev
# uvicorn app.main:app --reload --port 8000 --app-dir src

# uvicorn src.app.main:app --host 0.0.0.0 --port 8000