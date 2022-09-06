"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.playurl.v1.playurl_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BusinessInfo(google.protobuf.message.Message):
    """其他业务信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_PREVIEW_FIELD_NUMBER: builtins.int
    BP_FIELD_NUMBER: builtins.int
    MARLIN_TOKEN_FIELD_NUMBER: builtins.int
    is_preview: builtins.bool
    """当前视频是否是预览"""

    bp: builtins.bool
    """用户是否承包过"""

    marlin_token: typing.Text
    """drm使用"""

    def __init__(self,
        *,
        is_preview: builtins.bool = ...,
        bp: builtins.bool = ...,
        marlin_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bp",b"bp","is_preview",b"is_preview","marlin_token",b"marlin_token"]) -> None: ...
global___BusinessInfo = BusinessInfo

class Event(google.protobuf.message.Message):
    """事件"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHAKE_FIELD_NUMBER: builtins.int
    @property
    def shake(self) -> global___Shake:
        """震动"""
        pass
    def __init__(self,
        *,
        shake: typing.Optional[global___Shake] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["shake",b"shake"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["shake",b"shake"]) -> None: ...
global___Event = Event

class LivePlayInfo(google.protobuf.message.Message):
    """播放信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CURRENT_QN_FIELD_NUMBER: builtins.int
    QUALITY_DESCRIPTION_FIELD_NUMBER: builtins.int
    DURL_FIELD_NUMBER: builtins.int
    current_qn: builtins.int
    """"""

    @property
    def quality_description(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QualityDescription]:
        """"""
        pass
    @property
    def durl(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResponseDataUrl]:
        """"""
        pass
    def __init__(self,
        *,
        current_qn: builtins.int = ...,
        quality_description: typing.Optional[typing.Iterable[global___QualityDescription]] = ...,
        durl: typing.Optional[typing.Iterable[global___ResponseDataUrl]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["current_qn",b"current_qn","durl",b"durl","quality_description",b"quality_description"]) -> None: ...
global___LivePlayInfo = LivePlayInfo

class LivePlayViewReply(google.protobuf.message.Message):
    """直播播放页信息-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROOM_INFO_FIELD_NUMBER: builtins.int
    PLAY_INFO_FIELD_NUMBER: builtins.int
    @property
    def room_info(self) -> global___RoomInfo:
        """房间信息"""
        pass
    @property
    def play_info(self) -> global___LivePlayInfo:
        """播放信息"""
        pass
    def __init__(self,
        *,
        room_info: typing.Optional[global___RoomInfo] = ...,
        play_info: typing.Optional[global___LivePlayInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["play_info",b"play_info","room_info",b"room_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["play_info",b"play_info","room_info",b"room_info"]) -> None: ...
global___LivePlayViewReply = LivePlayViewReply

class LivePlayViewReq(google.protobuf.message.Message):
    """直播播放页信息-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EP_ID_FIELD_NUMBER: builtins.int
    QUALITY_FIELD_NUMBER: builtins.int
    PTYPE_FIELD_NUMBER: builtins.int
    HTTPS_FIELD_NUMBER: builtins.int
    PLAY_TYPE_FIELD_NUMBER: builtins.int
    DEVICE_TYPE_FIELD_NUMBER: builtins.int
    ep_id: builtins.int
    """剧集epid"""

    quality: builtins.int
    """清晰度
    0,10000:原画 400:蓝光 250:超清 150:高清 80:流畅
    """

    ptype: builtins.int
    """类型
    0:音频 2:hevc 4:dash 8:p2p, 16:蒙版
    """

    https: builtins.bool
    """是否请求https"""

    play_type: builtins.int
    """0:默认直播间播放 1:投屏播放"""

    device_type: builtins.int
    """投屏设备
    0:默认其他 1:OTT设备
    """

    def __init__(self,
        *,
        ep_id: builtins.int = ...,
        quality: builtins.int = ...,
        ptype: builtins.int = ...,
        https: builtins.bool = ...,
        play_type: builtins.int = ...,
        device_type: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["device_type",b"device_type","ep_id",b"ep_id","https",b"https","play_type",b"play_type","ptype",b"ptype","quality",b"quality"]) -> None: ...
global___LivePlayViewReq = LivePlayViewReq

class PlayAbilityConf(google.protobuf.message.Message):
    """禁用功能配置"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BACKGROUND_PLAY_DISABLE_FIELD_NUMBER: builtins.int
    FLIP_DISABLE_FIELD_NUMBER: builtins.int
    CAST_DISABLE_FIELD_NUMBER: builtins.int
    FEEDBACK_DISABLE_FIELD_NUMBER: builtins.int
    SUBTITLE_DISABLE_FIELD_NUMBER: builtins.int
    PLAYBACK_RATE_DISABLE_FIELD_NUMBER: builtins.int
    TIME_UP_DISABLE_FIELD_NUMBER: builtins.int
    PLAYBACK_MODE_DISABLE_FIELD_NUMBER: builtins.int
    SCALE_MODE_DISABLE_FIELD_NUMBER: builtins.int
    LIKE_DISABLE_FIELD_NUMBER: builtins.int
    DISLIKE_DISABLE_FIELD_NUMBER: builtins.int
    COIN_DISABLE_FIELD_NUMBER: builtins.int
    ELEC_DISABLE_FIELD_NUMBER: builtins.int
    SHARE_DISABLE_FIELD_NUMBER: builtins.int
    SCREEN_SHOT_DISABLE_FIELD_NUMBER: builtins.int
    LOCK_SCREEN_DISABLE_FIELD_NUMBER: builtins.int
    RECOMMEND_DISABLE_FIELD_NUMBER: builtins.int
    PLAYBACK_SPEED_DISABLE_FIELD_NUMBER: builtins.int
    DEFINITION_DISABLE_FIELD_NUMBER: builtins.int
    SELECTIONS_DISABLE_FIELD_NUMBER: builtins.int
    NEXT_DISABLE_FIELD_NUMBER: builtins.int
    EDIT_DM_DISABLE_FIELD_NUMBER: builtins.int
    SMALL_WINDOW_DISABLE_FIELD_NUMBER: builtins.int
    SHAKE_DISABLE_FIELD_NUMBER: builtins.int
    OUTER_DM_DISABLE_FIELD_NUMBER: builtins.int
    INNER_DM_DISABLE_FIELD_NUMBER: builtins.int
    FREYA_ENTER_DISABLE_FIELD_NUMBER: builtins.int
    DOLBY_DISABLE_FIELD_NUMBER: builtins.int
    FREYA_FULL_DISABLE_FIELD_NUMBER: builtins.int
    SKIP_OPED_SWITCH_DISABLE_FIELD_NUMBER: builtins.int
    background_play_disable: builtins.bool
    """后台播放"""

    flip_disable: builtins.bool
    """镜像反转"""

    cast_disable: builtins.bool
    """投屏"""

    feedback_disable: builtins.bool
    """反馈"""

    subtitle_disable: builtins.bool
    """字幕"""

    playback_rate_disable: builtins.bool
    """播放速度"""

    time_up_disable: builtins.bool
    """定时停止"""

    playback_mode_disable: builtins.bool
    """播放方式"""

    scale_mode_disable: builtins.bool
    """画面尺寸"""

    like_disable: builtins.bool
    """赞"""

    dislike_disable: builtins.bool
    """踩"""

    coin_disable: builtins.bool
    """投币"""

    elec_disable: builtins.bool
    """充电"""

    share_disable: builtins.bool
    """分享"""

    screen_shot_disable: builtins.bool
    """截图"""

    lock_screen_disable: builtins.bool
    """锁定"""

    recommend_disable: builtins.bool
    """相关推荐"""

    playback_speed_disable: builtins.bool
    """播放速度"""

    definition_disable: builtins.bool
    """清晰度"""

    selections_disable: builtins.bool
    """选集"""

    next_disable: builtins.bool
    """下一集"""

    edit_dm_disable: builtins.bool
    """编辑弹幕"""

    small_window_disable: builtins.bool
    """小窗"""

    shake_disable: builtins.bool
    """震动"""

    outer_dm_disable: builtins.bool
    """外层面板弹幕设置"""

    inner_dm_disable: builtins.bool
    """三点内弹幕设置"""

    freya_enter_disable: builtins.bool
    """一起看入口"""

    dolby_disable: builtins.bool
    """杜比音效"""

    freya_full_disable: builtins.bool
    """全屏一起看入口"""

    skip_oped_switch_disable: builtins.bool
    """"""

    def __init__(self,
        *,
        background_play_disable: builtins.bool = ...,
        flip_disable: builtins.bool = ...,
        cast_disable: builtins.bool = ...,
        feedback_disable: builtins.bool = ...,
        subtitle_disable: builtins.bool = ...,
        playback_rate_disable: builtins.bool = ...,
        time_up_disable: builtins.bool = ...,
        playback_mode_disable: builtins.bool = ...,
        scale_mode_disable: builtins.bool = ...,
        like_disable: builtins.bool = ...,
        dislike_disable: builtins.bool = ...,
        coin_disable: builtins.bool = ...,
        elec_disable: builtins.bool = ...,
        share_disable: builtins.bool = ...,
        screen_shot_disable: builtins.bool = ...,
        lock_screen_disable: builtins.bool = ...,
        recommend_disable: builtins.bool = ...,
        playback_speed_disable: builtins.bool = ...,
        definition_disable: builtins.bool = ...,
        selections_disable: builtins.bool = ...,
        next_disable: builtins.bool = ...,
        edit_dm_disable: builtins.bool = ...,
        small_window_disable: builtins.bool = ...,
        shake_disable: builtins.bool = ...,
        outer_dm_disable: builtins.bool = ...,
        inner_dm_disable: builtins.bool = ...,
        freya_enter_disable: builtins.bool = ...,
        dolby_disable: builtins.bool = ...,
        freya_full_disable: builtins.bool = ...,
        skip_oped_switch_disable: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["background_play_disable",b"background_play_disable","cast_disable",b"cast_disable","coin_disable",b"coin_disable","definition_disable",b"definition_disable","dislike_disable",b"dislike_disable","dolby_disable",b"dolby_disable","edit_dm_disable",b"edit_dm_disable","elec_disable",b"elec_disable","feedback_disable",b"feedback_disable","flip_disable",b"flip_disable","freya_enter_disable",b"freya_enter_disable","freya_full_disable",b"freya_full_disable","inner_dm_disable",b"inner_dm_disable","like_disable",b"like_disable","lock_screen_disable",b"lock_screen_disable","next_disable",b"next_disable","outer_dm_disable",b"outer_dm_disable","playback_mode_disable",b"playback_mode_disable","playback_rate_disable",b"playback_rate_disable","playback_speed_disable",b"playback_speed_disable","recommend_disable",b"recommend_disable","scale_mode_disable",b"scale_mode_disable","screen_shot_disable",b"screen_shot_disable","selections_disable",b"selections_disable","shake_disable",b"shake_disable","share_disable",b"share_disable","skip_oped_switch_disable",b"skip_oped_switch_disable","small_window_disable",b"small_window_disable","subtitle_disable",b"subtitle_disable","time_up_disable",b"time_up_disable"]) -> None: ...
global___PlayAbilityConf = PlayAbilityConf

class PlayViewReply(google.protobuf.message.Message):
    """ 播放页信息-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VIDEO_INFO_FIELD_NUMBER: builtins.int
    PLAY_CONF_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    @property
    def video_info(self) -> bilibili.app.playurl.v1.playurl_pb2.VideoInfo:
        """视频流信息"""
        pass
    @property
    def play_conf(self) -> global___PlayAbilityConf:
        """播放控件用户自定义配置"""
        pass
    @property
    def business(self) -> global___BusinessInfo:
        """业务需要的其他信息"""
        pass
    @property
    def event(self) -> global___Event:
        """事件"""
        pass
    def __init__(self,
        *,
        video_info: typing.Optional[bilibili.app.playurl.v1.playurl_pb2.VideoInfo] = ...,
        play_conf: typing.Optional[global___PlayAbilityConf] = ...,
        business: typing.Optional[global___BusinessInfo] = ...,
        event: typing.Optional[global___Event] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["business",b"business","event",b"event","play_conf",b"play_conf","video_info",b"video_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","event",b"event","play_conf",b"play_conf","video_info",b"video_info"]) -> None: ...
global___PlayViewReply = PlayViewReply

class PlayViewReq(google.protobuf.message.Message):
    """播放页信息-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EPID_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    QN_FIELD_NUMBER: builtins.int
    FNVER_FIELD_NUMBER: builtins.int
    FNVAL_FIELD_NUMBER: builtins.int
    DOWNLOAD_FIELD_NUMBER: builtins.int
    FORCE_HOST_FIELD_NUMBER: builtins.int
    FOURK_FIELD_NUMBER: builtins.int
    SPMID_FIELD_NUMBER: builtins.int
    FROM_SPMID_FIELD_NUMBER: builtins.int
    TEENAGERS_MODE_FIELD_NUMBER: builtins.int
    PREFER_CODEC_TYPE_FIELD_NUMBER: builtins.int
    IS_PREVIEW_FIELD_NUMBER: builtins.int
    ROOM_ID_FIELD_NUMBER: builtins.int
    epid: builtins.int
    """剧集epid"""

    cid: builtins.int
    """视频cid"""

    qn: builtins.int
    """清晰度"""

    fnver: builtins.int
    """视频流版本"""

    fnval: builtins.int
    """视频流格式"""

    download: builtins.int
    """下载模式
    0:播放 1:flv下载 2:dash下载
    """

    force_host: builtins.int
    """流url强制是用域名
    0:允许使用ip 1:使用http 2:使用https
    """

    fourk: builtins.bool
    """是否4K"""

    spmid: typing.Text
    """当前页spm"""

    from_spmid: typing.Text
    """上一页spm"""

    teenagers_mode: builtins.int
    """青少年模式"""

    prefer_codec_type: bilibili.app.playurl.v1.playurl_pb2.CodeType.ValueType
    """视频编码"""

    is_preview: builtins.bool
    """是否强制请求预览视频"""

    room_id: builtins.int
    """一起看房间id"""

    def __init__(self,
        *,
        epid: builtins.int = ...,
        cid: builtins.int = ...,
        qn: builtins.int = ...,
        fnver: builtins.int = ...,
        fnval: builtins.int = ...,
        download: builtins.int = ...,
        force_host: builtins.int = ...,
        fourk: builtins.bool = ...,
        spmid: typing.Text = ...,
        from_spmid: typing.Text = ...,
        teenagers_mode: builtins.int = ...,
        prefer_codec_type: bilibili.app.playurl.v1.playurl_pb2.CodeType.ValueType = ...,
        is_preview: builtins.bool = ...,
        room_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cid",b"cid","download",b"download","epid",b"epid","fnval",b"fnval","fnver",b"fnver","force_host",b"force_host","fourk",b"fourk","from_spmid",b"from_spmid","is_preview",b"is_preview","prefer_codec_type",b"prefer_codec_type","qn",b"qn","room_id",b"room_id","spmid",b"spmid","teenagers_mode",b"teenagers_mode"]) -> None: ...
global___PlayViewReq = PlayViewReq

class ProjectReply(google.protobuf.message.Message):
    """投屏地址-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_FIELD_NUMBER: builtins.int
    @property
    def project(self) -> bilibili.app.playurl.v1.playurl_pb2.PlayURLReply: ...
    def __init__(self,
        *,
        project: typing.Optional[bilibili.app.playurl.v1.playurl_pb2.PlayURLReply] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["project",b"project"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["project",b"project"]) -> None: ...
global___ProjectReply = ProjectReply

class ProjectReq(google.protobuf.message.Message):
    """投屏地址-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EP_ID_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    QN_FIELD_NUMBER: builtins.int
    FNVER_FIELD_NUMBER: builtins.int
    FNVAL_FIELD_NUMBER: builtins.int
    DOWNLOAD_FIELD_NUMBER: builtins.int
    FORCEHOST_FIELD_NUMBER: builtins.int
    FOURK_FIELD_NUMBER: builtins.int
    SPMID_FIELD_NUMBER: builtins.int
    FROMSPMID_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    DEVICE_TYPE_FIELD_NUMBER: builtins.int
    USE_NEW_PROJECT_CODE_FIELD_NUMBER: builtins.int
    ep_id: builtins.int
    """剧集epid"""

    cid: builtins.int
    """视频cid"""

    qn: builtins.int
    """清晰度"""

    fnver: builtins.int
    """视频流版本"""

    fnval: builtins.int
    """视频流格式"""

    download: builtins.int
    """下载模式
    0:播放 1:flv下载 2:dash下载
    """

    forceHost: builtins.int
    """流url强制是用域名
    0:允许使用ip 1:使用http 2:使用https
    """

    fourk: builtins.bool
    """是否4K"""

    spmid: typing.Text
    """当前页spm"""

    fromSpmid: typing.Text
    """上一页spm"""

    protocol: builtins.int
    """使用协议
    0:默认乐播 1:自建协议 2:云投屏 3:airplay
    """

    device_type: builtins.int
    """投屏设备
    0:默认其他 1:OTT设备
    """

    use_new_project_code: builtins.bool
    """"""

    def __init__(self,
        *,
        ep_id: builtins.int = ...,
        cid: builtins.int = ...,
        qn: builtins.int = ...,
        fnver: builtins.int = ...,
        fnval: builtins.int = ...,
        download: builtins.int = ...,
        forceHost: builtins.int = ...,
        fourk: builtins.bool = ...,
        spmid: typing.Text = ...,
        fromSpmid: typing.Text = ...,
        protocol: builtins.int = ...,
        device_type: builtins.int = ...,
        use_new_project_code: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cid",b"cid","device_type",b"device_type","download",b"download","ep_id",b"ep_id","fnval",b"fnval","fnver",b"fnver","forceHost",b"forceHost","fourk",b"fourk","fromSpmid",b"fromSpmid","protocol",b"protocol","qn",b"qn","spmid",b"spmid","use_new_project_code",b"use_new_project_code"]) -> None: ...
global___ProjectReq = ProjectReq

class QualityDescription(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QN_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    qn: builtins.int
    """"""

    desc: typing.Text
    """"""

    def __init__(self,
        *,
        qn: builtins.int = ...,
        desc: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["desc",b"desc","qn",b"qn"]) -> None: ...
global___QualityDescription = QualityDescription

class ResponseDataUrl(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    URL_FIELD_NUMBER: builtins.int
    STREAM_TYPE_FIELD_NUMBER: builtins.int
    PTAG_FIELD_NUMBER: builtins.int
    url: typing.Text
    stream_type: builtins.int
    """表示stream类型,按位表示
    Value|  1   |  1  |  1   |  1   |     1
    --------------------------------------------
    desc | mask | p2p | dash | hevc | only-audio
    """

    ptag: builtins.int
    """表示支持p2p的cdn厂商,按位表示
    值   | 1  |  1  |  1  | 1  |  1  | 1  | 1  | 1
    -----------------------------------------------
    CDN	| hw | bdy | bsy | ws | txy | qn | js | bvc
    """

    def __init__(self,
        *,
        url: typing.Text = ...,
        stream_type: builtins.int = ...,
        ptag: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ptag",b"ptag","stream_type",b"stream_type","url",b"url"]) -> None: ...
global___ResponseDataUrl = ResponseDataUrl

class RoomInfo(google.protobuf.message.Message):
    """房间信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROOM_ID_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SHOW_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间长号"""

    uid: builtins.int
    """主播mid"""

    @property
    def status(self) -> global___RoomStatusInfo:
        """状态相关"""
        pass
    @property
    def show(self) -> global___RoomShowInfo:
        """展示相关"""
        pass
    def __init__(self,
        *,
        room_id: builtins.int = ...,
        uid: builtins.int = ...,
        status: typing.Optional[global___RoomStatusInfo] = ...,
        show: typing.Optional[global___RoomShowInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["show",b"show","status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["room_id",b"room_id","show",b"show","status",b"status","uid",b"uid"]) -> None: ...
global___RoomInfo = RoomInfo

class RoomShowInfo(google.protobuf.message.Message):
    """房间信息-展示相关"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHORT_ID_FIELD_NUMBER: builtins.int
    POPULARITY_COUNT_FIELD_NUMBER: builtins.int
    LIVE_START_TIME_FIELD_NUMBER: builtins.int
    short_id: builtins.int
    """短号"""

    popularity_count: builtins.int
    """人气值"""

    live_start_time: builtins.int
    """最近一次开播时间戳"""

    def __init__(self,
        *,
        short_id: builtins.int = ...,
        popularity_count: builtins.int = ...,
        live_start_time: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["live_start_time",b"live_start_time","popularity_count",b"popularity_count","short_id",b"short_id"]) -> None: ...
global___RoomShowInfo = RoomShowInfo

class RoomStatusInfo(google.protobuf.message.Message):
    """房间信息-状态相关"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIVE_STATUS_FIELD_NUMBER: builtins.int
    LIVE_SCREEN_TYPE_FIELD_NUMBER: builtins.int
    LIVE_MARK_FIELD_NUMBER: builtins.int
    LOCK_STATUS_FIELD_NUMBER: builtins.int
    LOCK_TIME_FIELD_NUMBER: builtins.int
    HIDDEN_STATUS_FIELD_NUMBER: builtins.int
    HIDDEN_TIME_FIELD_NUMBER: builtins.int
    LIVE_TYPE_FIELD_NUMBER: builtins.int
    ROOM_SHIELD_FIELD_NUMBER: builtins.int
    live_status: builtins.int
    """直播间状态
    0:未开播 1:直播中 2:轮播中
    """

    live_screen_type: builtins.int
    """横竖屏方向
    0:横屏 1:竖屏
    """

    live_mark: builtins.int
    """是否开播过标识"""

    lock_status: builtins.int
    """封禁状态
    0:未封禁 1:审核封禁 2:全网封禁
    """

    lock_time: builtins.int
    """封禁时间戳"""

    hidden_status: builtins.int
    """隐藏状态
    0:不隐藏 1:隐藏
    """

    hidden_time: builtins.int
    """隐藏时间戳"""

    live_type: builtins.int
    """直播类型
    0:默认 1:摄像头直播 2;录屏直播 3:语音直播
    """

    room_shield: builtins.int
    """"""

    def __init__(self,
        *,
        live_status: builtins.int = ...,
        live_screen_type: builtins.int = ...,
        live_mark: builtins.int = ...,
        lock_status: builtins.int = ...,
        lock_time: builtins.int = ...,
        hidden_status: builtins.int = ...,
        hidden_time: builtins.int = ...,
        live_type: builtins.int = ...,
        room_shield: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hidden_status",b"hidden_status","hidden_time",b"hidden_time","live_mark",b"live_mark","live_screen_type",b"live_screen_type","live_status",b"live_status","live_type",b"live_type","lock_status",b"lock_status","lock_time",b"lock_time","room_shield",b"room_shield"]) -> None: ...
global___RoomStatusInfo = RoomStatusInfo

class Shake(google.protobuf.message.Message):
    """震动"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILE_FIELD_NUMBER: builtins.int
    file: typing.Text
    """文件地址"""

    def __init__(self,
        *,
        file: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file",b"file"]) -> None: ...
global___Shake = Shake
