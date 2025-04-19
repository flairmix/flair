from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.static_files import StaticFilesConfig

from app.api.files import FileController
from app.api.auth import register, login
from app.api.routes import generate_route
from app.services.db import init_db
from app.api.post import PostController
init_db()



app = Litestar(
    route_handlers=[register, login, 
                    generate_route, 
                    FileController,
                    PostController,    
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
   