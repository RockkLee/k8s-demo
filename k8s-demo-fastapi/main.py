import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from k8s_demo_fastapi.api.routers import ping_api
from k8s_demo_fastapi.helper.log import logger

app = FastAPI()
app.include_router(ping_api.router)

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    logger.info("Hello World v1.0.1")
    return {"message": "Hello World v1.0.1"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
