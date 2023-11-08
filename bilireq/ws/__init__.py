from typing import Union

from bilireq.utils import get

BASE_URL = "https://api.live.bilibili.com"


async def get_ws_conf_by_room_id(
    room_id: Union[int, str], *, auth=None, reqtype="web", **kwargs
):
    """根据房间号获取直播间弹幕服务器地址"""
    url = f"{BASE_URL}/room/v1/Danmu/getConf"
    params = {"room_id": room_id, "platform": "pc", "player": "web"}
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)


async def get_ws_conf_by_room_id_new(
    room_id: Union[int, str], *, auth=None, reqtype="web", **kwargs
):
    """根据房间号获取直播间弹幕服务器地址"""
    url = f"{BASE_URL}/xlive/web-room/v1/index/getDanmuInfo"
    params = {"id": room_id, "type": 0}
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)
