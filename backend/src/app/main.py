from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.static_files import StaticFilesConfig
from litestar.config.cors import CORSConfig  

from .api.files import FileController
from .api.auth import register, login
from .api.routes import generate_route
from .services.db import init_db
from .api.post import PostController
from .api.water_controller import WaterController
from .api.vent_controller import VentController

init_db()

openapi_config = OpenAPIConfig(
    title="Flair API",
    version="1.0.0",
)

cors_config = CORSConfig(
    allow_origins=["https://flairbim.com"],   # или ["*"] в dev
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
    allow_credentials=True,
)

app = Litestar(
    debug=False,
    cors_config=cors_config,   # ✅ только это
    route_handlers=[
        register,
        login,
        generate_route,
        FileController,
        PostController,
        WaterController,
        VentController,
    ],
    openapi_config=openapi_config,
    static_files_config=[
        StaticFilesConfig(path="/static", directories=["output"])
    ],
)
