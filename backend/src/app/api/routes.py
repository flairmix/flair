from litestar import post
from litestar.params import Body
from ..services.dxf_builder import build_dxf_file

@post("/generate")
async def generate_route(data: dict = Body()) -> dict:
    filepath = build_dxf_file(data)
    return {"download_url": f"/static/{filepath.name}"}
