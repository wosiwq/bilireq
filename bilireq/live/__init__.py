from typing import List, Union

from ..utils import get, post

BASE_URL = "https://api.live.bilibili.com"


async def get_rooms_info_by_uids(
    uids: List[Union[int, str]], *, auth=None, reqtype="app", **kwargs
):
    """根据 UID 批量获取直播间信息"""
    url = f"{BASE_URL}/room/v1/Room/get_status_info_by_uids"
    data = {"uids": uids}
    return await post(url, json=data, auth=auth, reqtype=reqtype, **kwargs)


async def get_rooms_info_by_ids(
    room_ids: List[Union[int, str]], *, auth=None, reqtype="app", **kwargs
):
    """根据房间号批量获取直播间信息"""
    url = f"{BASE_URL}/room/v1/Room/get_info_by_id"
    data = {"ids": room_ids}
    return await post(url, json=data, auth=auth, reqtype=reqtype, **kwargs)


async def get_room_info_by_uid(
    uid: Union[int, str], *, auth=None, reqtype="app", **kwargs
):
    """根据 UID 获取指定直播间信息"""
    url = f"{BASE_URL}/room/v1/Room/getRoomInfoOld"
    params = {"mid": uid}
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)


async def get_room_info_by_id(
    room_id: Union[int, str], *, auth=None, reqtype="app", **kwargs
):
    """根据房间号获取指定直播间信息"""
    url = f"{BASE_URL}/room/v1/Room/get_info"
    params = {"id": room_id}
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)

async def get_gift_config(*, auth=None, reqtype="web", **kwargs):
    """获取礼物配置"""
    url = f"{BASE_URL}/gift/v3/live/gift_config"
    return await get(url, auth=auth, reqtype=reqtype, **kwargs)

async def get_room_detail_by_room_id(
    room_id: Union[int, str], *, auth=None, reqtype="web", **kwargs
):
    """根据房间号获取指定直播间信息"""
    url = f"{BASE_URL}/xlive/web-room/v1/index/getInfoByRoom"
    params = {"room_id": room_id}
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)