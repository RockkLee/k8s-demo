from pydantic import BaseModel


class Msg(BaseModel):
    message: str


class MsgResp(Msg):
    def __init__(self, message: str):
        super().__init__(message=message)

    class Config:
        from_attributes = True