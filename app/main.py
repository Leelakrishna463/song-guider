from fastapi import FastAPI, Depends, status
from app.api.auth.api_key import authorize_request
from app.api.songs.routes import router as song_router
from fastapi.responses import JSONResponse
from app.logger import logger


app = FastAPI(title='song-guider', dependencies=[Depends(authorize_request)])
app.include_router(song_router, prefix="/songs")


logger.info("Song Guider application is starting")


@app.get("/health")
def health_check():
    return JSONResponse(
        content={"status": "healthy"},
        status_code=status.HTTP_200_OK
    )

