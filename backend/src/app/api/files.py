from typing import Annotated
from litestar import Controller, post, get, delete, Request, Response
from litestar.datastructures import UploadFile
from litestar.params import Body, Parameter
from litestar.status_codes import HTTP_201_CREATED, HTTP_200_OK

from ..services.storage_service import (
    upload_file,
    download_file,
    generate_presigned_url,
    list_files,
    delete_file_by_name,
)


class FileController(Controller):
    path = "/files"
    tags = ["Файлы"]

    @post("/upload", status_code=HTTP_201_CREATED)
    async def upload(self, data: Annotated[UploadFile, Body(media_type="multipart/form-data")]) -> dict:
        """Upload file to MinIO bucket."""
        await upload_file(data.file, data.filename, data.content_type or "application/octet-stream")
        return {"filename": data.filename, "status": "uploaded"}

    @get("/{filename:str}")
    async def download(self, filename: Annotated[str, Parameter()]) -> Response:
        """Download file by name from MinIO."""
        content = await download_file(filename)
        return Response(content=content, media_type="application/octet-stream")

    @get("/{filename:str}/url")
    async def get_presigned_url(self, filename: Annotated[str, Parameter()]) -> dict:
        """Get presigned public download URL for a file."""
        url = generate_presigned_url(filename)
        return {"url": url}

    @get("/")
    async def list_all(self) -> list[str]:
        """List all files in bucket."""
        return list_files()

    @delete("/{filename:str}", status_code=HTTP_200_OK)
    async def delete(self, filename: Annotated[str, Parameter()]) -> dict:
        """Delete a file by name."""
        delete_file_by_name(filename)
        return {"filename": filename, "status": "deleted"}
