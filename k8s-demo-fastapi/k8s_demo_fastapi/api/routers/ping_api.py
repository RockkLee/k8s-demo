from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status, HTTPException, Response

from k8s_demo_fastapi.api.schemas.msg import MsgResp
from k8s_demo_fastapi.orm.connection import get_session
from k8s_demo_fastapi.orm.models.pingpong import PingPong


router = APIRouter(
    prefix="/ping",
    tags=['ping_api']
)


@router.post("/msg/{input_msg}", response_model=MsgResp, status_code=status.HTTP_200_OK)
async def insert(input_msg: str, db: AsyncSession = Depends(get_session)):
    pingpong = PingPong(ping_msg=input_msg, create_date=datetime.now())
    db.add(pingpong)
    await db.commit()
    return MsgResp(f"Pong! (saved msg to db)")


@router.get("/getall", response_model=MsgResp, status_code=status.HTTP_200_OK)
async def getall(db: AsyncSession = Depends(get_session)):
    # get all
    stm = await db.execute(select(PingPong))
    pingpongs = stm.scalars().all()

    def format_pingpong(pingpong: PingPong):
        return f"({pingpong.id}, {pingpong.ping_msg}, {pingpong.create_date})"
    output_ls = list(map(format_pingpong, pingpongs))

    return MsgResp(f"Get all pingpongs: {output_ls}")


@router.delete("/deleteall", response_model=MsgResp, status_code=status.HTTP_200_OK)
async def deleteall(db: AsyncSession = Depends(get_session)):
    # delete all
    await db.execute(PingPong.__table__.delete())
    await db.commit()
    return MsgResp(f"Deleted all pingpongs")