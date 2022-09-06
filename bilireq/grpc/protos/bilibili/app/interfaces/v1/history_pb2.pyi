"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.archive.middleware.v1.preload_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DT:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _DTEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DT.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Unknown: _DT.ValueType  # 0
    """未知"""

    Phone: _DT.ValueType  # 1
    """手机端"""

    Pad: _DT.ValueType  # 2
    """ipad端"""

    PC: _DT.ValueType  # 3
    """web端"""

    TV: _DT.ValueType  # 4
    """TV端"""

    Car: _DT.ValueType  # 5
    """"""

    Iot: _DT.ValueType  # 6
    """"""

    AndPad: _DT.ValueType  # 7
    """apad端"""

class DT(_DT, metaclass=_DTEnumTypeWrapper):
    """设备标识代码"""
    pass

Unknown: DT.ValueType  # 0
"""未知"""

Phone: DT.ValueType  # 1
"""手机端"""

Pad: DT.ValueType  # 2
"""ipad端"""

PC: DT.ValueType  # 3
"""web端"""

TV: DT.ValueType  # 4
"""TV端"""

Car: DT.ValueType  # 5
""""""

Iot: DT.ValueType  # 6
""""""

AndPad: DT.ValueType  # 7
"""apad端"""

global___DT = DT


class _HistorySource:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _HistorySourceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_HistorySource.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    history_VALUE: _HistorySource.ValueType  # 0
    """主站历史记录页"""

    shopping_VALUE: _HistorySource.ValueType  # 1
    """会员购浏览记录"""

class HistorySource(_HistorySource, metaclass=_HistorySourceEnumTypeWrapper):
    """搜索历史记录来源"""
    pass

history_VALUE: HistorySource.ValueType  # 0
"""主站历史记录页"""

shopping_VALUE: HistorySource.ValueType  # 1
"""会员购浏览记录"""

global___HistorySource = HistorySource


class CardArticle(google.protobuf.message.Message):
    """专栏卡片"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COVERS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    DISPLAYATTENTION_FIELD_NUMBER: builtins.int
    BADGE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    @property
    def covers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """封面url"""
        pass
    name: typing.Text
    """UP主昵称"""

    mid: builtins.int
    """UP主mid"""

    displayAttention: builtins.bool
    """是否展示关注按钮"""

    badge: typing.Text
    """角标"""

    @property
    def relation(self) -> global___Relation:
        """关系信息"""
        pass
    def __init__(self,
        *,
        covers: typing.Optional[typing.Iterable[typing.Text]] = ...,
        name: typing.Text = ...,
        mid: builtins.int = ...,
        displayAttention: builtins.bool = ...,
        badge: typing.Text = ...,
        relation: typing.Optional[global___Relation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relation",b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["badge",b"badge","covers",b"covers","displayAttention",b"displayAttention","mid",b"mid","name",b"name","relation",b"relation"]) -> None: ...
global___CardArticle = CardArticle

class CardCheese(google.protobuf.message.Message):
    """课程卡片"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COVER_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    cover: typing.Text
    """封面url"""

    progress: builtins.int
    """观看进度"""

    duration: builtins.int
    """总计时长"""

    subtitle: typing.Text
    """单集标题"""

    def __init__(self,
        *,
        cover: typing.Text = ...,
        progress: builtins.int = ...,
        duration: builtins.int = ...,
        subtitle: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover",b"cover","duration",b"duration","progress",b"progress","subtitle",b"subtitle"]) -> None: ...
global___CardCheese = CardCheese

class CardLive(google.protobuf.message.Message):
    """直播卡片"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COVER_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    STSTUS_FIELD_NUMBER: builtins.int
    DISPLAY_ATTENTION_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    cover: typing.Text
    """封面url"""

    name: typing.Text
    """主播昵称"""

    mid: builtins.int
    """主播mid"""

    tag: typing.Text
    """直播分区名"""

    ststus: builtins.int
    """直播状态"""

    display_attention: builtins.bool
    """是否展示关注按钮"""

    @property
    def relation(self) -> global___Relation:
        """关系信息"""
        pass
    def __init__(self,
        *,
        cover: typing.Text = ...,
        name: typing.Text = ...,
        mid: builtins.int = ...,
        tag: typing.Text = ...,
        ststus: builtins.int = ...,
        display_attention: builtins.bool = ...,
        relation: typing.Optional[global___Relation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relation",b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover",b"cover","display_attention",b"display_attention","mid",b"mid","name",b"name","relation",b"relation","ststus",b"ststus","tag",b"tag"]) -> None: ...
global___CardLive = CardLive

class CardOGV(google.protobuf.message.Message):
    """pgc稿件卡片"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COVER_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    cover: typing.Text
    """封面url"""

    progress: builtins.int
    """观看进度"""

    duration: builtins.int
    """总计时长"""

    subtitle: typing.Text
    """单集标题"""

    def __init__(self,
        *,
        cover: typing.Text = ...,
        progress: builtins.int = ...,
        duration: builtins.int = ...,
        subtitle: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover",b"cover","duration",b"duration","progress",b"progress","subtitle",b"subtitle"]) -> None: ...
global___CardOGV = CardOGV

class CardUGC(google.protobuf.message.Message):
    """ugc稿件卡片"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COVER_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    DISPLAY_ATTENTION_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    VIDEOS_FIELD_NUMBER: builtins.int
    SHORT_LINK_FIELD_NUMBER: builtins.int
    SHARE_SUBTITLE_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    cover: typing.Text
    """封面url"""

    progress: builtins.int
    """观看进度"""

    duration: builtins.int
    """视频长度"""

    name: typing.Text
    """UP主昵称"""

    mid: builtins.int
    """UP主mid"""

    display_attention: builtins.bool
    """是否展示关注按钮"""

    cid: builtins.int
    """历史观看视频cid"""

    page: builtins.int
    """历史观看视频分P"""

    subtitle: typing.Text
    """历史观看视频分P的标题"""

    @property
    def relation(self) -> global___Relation:
        """关系信息"""
        pass
    bvid: typing.Text
    """稿件bvid"""

    videos: builtins.int
    """总分P数"""

    short_link: typing.Text
    """短链接"""

    share_subtitle: typing.Text
    """分享副标题"""

    view: builtins.int
    """播放数"""

    state: builtins.int
    """"""

    def __init__(self,
        *,
        cover: typing.Text = ...,
        progress: builtins.int = ...,
        duration: builtins.int = ...,
        name: typing.Text = ...,
        mid: builtins.int = ...,
        display_attention: builtins.bool = ...,
        cid: builtins.int = ...,
        page: builtins.int = ...,
        subtitle: typing.Text = ...,
        relation: typing.Optional[global___Relation] = ...,
        bvid: typing.Text = ...,
        videos: builtins.int = ...,
        short_link: typing.Text = ...,
        share_subtitle: typing.Text = ...,
        view: builtins.int = ...,
        state: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relation",b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bvid",b"bvid","cid",b"cid","cover",b"cover","display_attention",b"display_attention","duration",b"duration","mid",b"mid","name",b"name","page",b"page","progress",b"progress","relation",b"relation","share_subtitle",b"share_subtitle","short_link",b"short_link","state",b"state","subtitle",b"subtitle","videos",b"videos","view",b"view"]) -> None: ...
global___CardUGC = CardUGC

class ClearReq(google.protobuf.message.Message):
    """清空历史记录-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUSINESS_FIELD_NUMBER: builtins.int
    business: typing.Text
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """

    def __init__(self,
        *,
        business: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business"]) -> None: ...
global___ClearReq = ClearReq

class Cursor(google.protobuf.message.Message):
    """游标信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAX_FIELD_NUMBER: builtins.int
    MAXTP_FIELD_NUMBER: builtins.int
    max: builtins.int
    """本页最大值游标值"""

    maxTp: builtins.int
    """本页最大值游标类型"""

    def __init__(self,
        *,
        max: builtins.int = ...,
        maxTp: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max",b"max","maxTp",b"maxTp"]) -> None: ...
global___Cursor = Cursor

class CursorItem(google.protobuf.message.Message):
    """历史记录卡片信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CARD_UGC_FIELD_NUMBER: builtins.int
    CARD_OGV_FIELD_NUMBER: builtins.int
    CARD_ARTICLE_FIELD_NUMBER: builtins.int
    CARD_LIVE_FIELD_NUMBER: builtins.int
    CARD_CHEESE_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    VIEWAT_FIELD_NUMBER: builtins.int
    KID_FIELD_NUMBER: builtins.int
    OID_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    TP_FIELD_NUMBER: builtins.int
    DT_FIELD_NUMBER: builtins.int
    HAS_SHARE_FIELD_NUMBER: builtins.int
    @property
    def card_ugc(self) -> global___CardUGC:
        """ugc稿件"""
        pass
    @property
    def card_ogv(self) -> global___CardOGV:
        """pgc稿件"""
        pass
    @property
    def card_article(self) -> global___CardArticle:
        """专栏"""
        pass
    @property
    def card_live(self) -> global___CardLive:
        """直播"""
        pass
    @property
    def card_cheese(self) -> global___CardCheese:
        """课程"""
        pass
    title: typing.Text
    """标题"""

    uri: typing.Text
    """目标uri/url"""

    viewAt: builtins.int
    """观看时间"""

    kid: builtins.int
    """历史记录id"""

    oid: builtins.int
    """业务id"""

    business: typing.Text
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """

    tp: builtins.int
    """业务类型代码"""

    @property
    def dt(self) -> global___DeviceType:
        """设备标识"""
        pass
    has_share: builtins.bool
    """是否有分享按钮"""

    def __init__(self,
        *,
        card_ugc: typing.Optional[global___CardUGC] = ...,
        card_ogv: typing.Optional[global___CardOGV] = ...,
        card_article: typing.Optional[global___CardArticle] = ...,
        card_live: typing.Optional[global___CardLive] = ...,
        card_cheese: typing.Optional[global___CardCheese] = ...,
        title: typing.Text = ...,
        uri: typing.Text = ...,
        viewAt: builtins.int = ...,
        kid: builtins.int = ...,
        oid: builtins.int = ...,
        business: typing.Text = ...,
        tp: builtins.int = ...,
        dt: typing.Optional[global___DeviceType] = ...,
        has_share: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["card_article",b"card_article","card_cheese",b"card_cheese","card_item",b"card_item","card_live",b"card_live","card_ogv",b"card_ogv","card_ugc",b"card_ugc","dt",b"dt"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","card_article",b"card_article","card_cheese",b"card_cheese","card_item",b"card_item","card_live",b"card_live","card_ogv",b"card_ogv","card_ugc",b"card_ugc","dt",b"dt","has_share",b"has_share","kid",b"kid","oid",b"oid","title",b"title","tp",b"tp","uri",b"uri","viewAt",b"viewAt"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["card_item",b"card_item"]) -> typing.Optional[typing_extensions.Literal["card_ugc","card_ogv","card_article","card_live","card_cheese"]]: ...
global___CursorItem = CursorItem

class CursorReply(google.protobuf.message.Message):
    """获取历史记录列表(旧版)-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ITEMS_FIELD_NUMBER: builtins.int
    TAB_FIELD_NUMBER: builtins.int
    CURSOR_FIELD_NUMBER: builtins.int
    HASMORE_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorItem]:
        """卡片内容"""
        pass
    @property
    def tab(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorTab]:
        """顶部tab"""
        pass
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
        pass
    hasMore: builtins.bool
    """是否未拉取完"""

    def __init__(self,
        *,
        items: typing.Optional[typing.Iterable[global___CursorItem]] = ...,
        tab: typing.Optional[typing.Iterable[global___CursorTab]] = ...,
        cursor: typing.Optional[global___Cursor] = ...,
        hasMore: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor",b"cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cursor",b"cursor","hasMore",b"hasMore","items",b"items","tab",b"tab"]) -> None: ...
global___CursorReply = CursorReply

class CursorReq(google.protobuf.message.Message):
    """获取历史记录列表(旧版)-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CURSOR_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    PLAYER_PRELOAD_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
        pass
    business: typing.Text
    """业务类型
    all:全部 archive:视频 live:直播 article:专栏
    """

    @property
    def player_preload(self) -> global___PlayerPreloadParams:
        """秒开参数(旧版)"""
        pass
    @property
    def player_args(self) -> bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """秒开参数"""
        pass
    def __init__(self,
        *,
        cursor: typing.Optional[global___Cursor] = ...,
        business: typing.Text = ...,
        player_preload: typing.Optional[global___PlayerPreloadParams] = ...,
        player_args: typing.Optional[bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor",b"cursor","player_args",b"player_args","player_preload",b"player_preload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","cursor",b"cursor","player_args",b"player_args","player_preload",b"player_preload"]) -> None: ...
global___CursorReq = CursorReq

class CursorTab(google.protobuf.message.Message):
    """业务分类表"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUSINESS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ROUTER_FIELD_NUMBER: builtins.int
    FOCUS_FIELD_NUMBER: builtins.int
    business: typing.Text
    """业务类型"""

    name: typing.Text
    """名称"""

    router: typing.Text
    """路由uri"""

    focus: builtins.bool
    """tab定位"""

    def __init__(self,
        *,
        business: typing.Text = ...,
        name: typing.Text = ...,
        router: typing.Text = ...,
        focus: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","focus",b"focus","name",b"name","router",b"router"]) -> None: ...
global___CursorTab = CursorTab

class CursorV2Reply(google.protobuf.message.Message):
    """获取历史记录列表-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ITEMS_FIELD_NUMBER: builtins.int
    CURSOR_FIELD_NUMBER: builtins.int
    HASMORE_FIELD_NUMBER: builtins.int
    EMPTY_LINK_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorItem]:
        """卡片内容"""
        pass
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
        pass
    hasMore: builtins.bool
    """是否未拉取完"""

    empty_link: typing.Text
    """"""

    def __init__(self,
        *,
        items: typing.Optional[typing.Iterable[global___CursorItem]] = ...,
        cursor: typing.Optional[global___Cursor] = ...,
        hasMore: builtins.bool = ...,
        empty_link: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor",b"cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cursor",b"cursor","empty_link",b"empty_link","hasMore",b"hasMore","items",b"items"]) -> None: ...
global___CursorV2Reply = CursorV2Reply

class CursorV2Req(google.protobuf.message.Message):
    """获取历史记录列表-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CURSOR_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    PLAYER_PRELOAD_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    IS_LOCAL_FIELD_NUMBER: builtins.int
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
        pass
    business: typing.Text
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """

    @property
    def player_preload(self) -> global___PlayerPreloadParams:
        """秒开参数(旧版)"""
        pass
    @property
    def player_args(self) -> bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """秒开参数"""
        pass
    is_local: builtins.bool
    """是否选择本机的播放历史"""

    def __init__(self,
        *,
        cursor: typing.Optional[global___Cursor] = ...,
        business: typing.Text = ...,
        player_preload: typing.Optional[global___PlayerPreloadParams] = ...,
        player_args: typing.Optional[bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs] = ...,
        is_local: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor",b"cursor","player_args",b"player_args","player_preload",b"player_preload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","cursor",b"cursor","is_local",b"is_local","player_args",b"player_args","player_preload",b"player_preload"]) -> None: ...
global___CursorV2Req = CursorV2Req

class DeleteReq(google.protobuf.message.Message):
    """删除历史记录-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HIS_INFO_FIELD_NUMBER: builtins.int
    @property
    def his_info(self) -> global___HisInfo:
        """历史记录信息"""
        pass
    def __init__(self,
        *,
        his_info: typing.Optional[global___HisInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["his_info",b"his_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["his_info",b"his_info"]) -> None: ...
global___DeleteReq = DeleteReq

class DeviceType(google.protobuf.message.Message):
    """设备类型"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    type: global___DT.ValueType
    """设备标识代码"""

    icon: typing.Text
    """图标url"""

    def __init__(self,
        *,
        type: global___DT.ValueType = ...,
        icon: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["icon",b"icon","type",b"type"]) -> None: ...
global___DeviceType = DeviceType

class HisInfo(google.protobuf.message.Message):
    """历史记录信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUSINESS_FIELD_NUMBER: builtins.int
    KID_FIELD_NUMBER: builtins.int
    business: typing.Text
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """

    kid: builtins.int
    """历史记录id"""

    def __init__(self,
        *,
        business: typing.Text = ...,
        kid: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","kid",b"kid"]) -> None: ...
global___HisInfo = HisInfo

class HistoryTabReply(google.protobuf.message.Message):
    """获取历史记录tab-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TAB_FIELD_NUMBER: builtins.int
    @property
    def tab(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorTab]:
        """tab列表"""
        pass
    def __init__(self,
        *,
        tab: typing.Optional[typing.Iterable[global___CursorTab]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tab",b"tab"]) -> None: ...
global___HistoryTabReply = HistoryTabReply

class HistoryTabReq(google.protobuf.message.Message):
    """获取历史记录tab-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUSINESS_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    business: typing.Text
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """

    source: global___HistorySource.ValueType
    """查询请求来源"""

    keyword: typing.Text
    """搜索关键词"""

    def __init__(self,
        *,
        business: typing.Text = ...,
        source: global___HistorySource.ValueType = ...,
        keyword: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","keyword",b"keyword","source",b"source"]) -> None: ...
global___HistoryTabReq = HistoryTabReq

class LatestHistoryReply(google.protobuf.message.Message):
    """获取最新的历史记录-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ITEMS_FIELD_NUMBER: builtins.int
    SCENE_FIELD_NUMBER: builtins.int
    RTIME_FIELD_NUMBER: builtins.int
    FLAG_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> global___CursorItem:
        """卡片内容"""
        pass
    scene: typing.Text
    """场景"""

    rtime: builtins.int
    """弹窗停留时间"""

    flag: typing.Text
    """分组的标志(客户端埋点上报)"""

    def __init__(self,
        *,
        items: typing.Optional[global___CursorItem] = ...,
        scene: typing.Text = ...,
        rtime: builtins.int = ...,
        flag: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["items",b"items"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flag",b"flag","items",b"items","rtime",b"rtime","scene",b"scene"]) -> None: ...
global___LatestHistoryReply = LatestHistoryReply

class LatestHistoryReq(google.protobuf.message.Message):
    """获取最新的历史记录-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUSINESS_FIELD_NUMBER: builtins.int
    PLAYER_PRELOAD_FIELD_NUMBER: builtins.int
    business: typing.Text
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """

    @property
    def player_preload(self) -> global___PlayerPreloadParams:
        """秒开参数"""
        pass
    def __init__(self,
        *,
        business: typing.Text = ...,
        player_preload: typing.Optional[global___PlayerPreloadParams] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["player_preload",b"player_preload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","player_preload",b"player_preload"]) -> None: ...
global___LatestHistoryReq = LatestHistoryReq

class NoReply(google.protobuf.message.Message):
    """空响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___NoReply = NoReply

class Page(google.protobuf.message.Message):
    """页面信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PN_FIELD_NUMBER: builtins.int
    TOTAL_FIELD_NUMBER: builtins.int
    pn: builtins.int
    """当前页码"""

    total: builtins.int
    """总计条目数"""

    def __init__(self,
        *,
        pn: builtins.int = ...,
        total: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pn",b"pn","total",b"total"]) -> None: ...
global___Page = Page

class PlayerPreloadParams(google.protobuf.message.Message):
    """秒开参数"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QN_FIELD_NUMBER: builtins.int
    FNVER_FIELD_NUMBER: builtins.int
    FNVAL_FIELD_NUMBER: builtins.int
    FORCEHOST_FIELD_NUMBER: builtins.int
    FOURK_FIELD_NUMBER: builtins.int
    qn: builtins.int
    """清晰度"""

    fnver: builtins.int
    """流版本"""

    fnval: builtins.int
    """流类型"""

    forceHost: builtins.int
    """是否强制域名"""

    fourk: builtins.int
    """是否4K"""

    def __init__(self,
        *,
        qn: builtins.int = ...,
        fnver: builtins.int = ...,
        fnval: builtins.int = ...,
        forceHost: builtins.int = ...,
        fourk: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fnval",b"fnval","fnver",b"fnver","forceHost",b"forceHost","fourk",b"fourk","qn",b"qn"]) -> None: ...
global___PlayerPreloadParams = PlayerPreloadParams

class Relation(google.protobuf.message.Message):
    """关系信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int
    IS_FOLLOW_FIELD_NUMBER: builtins.int
    IS_FOLLOWED_FIELD_NUMBER: builtins.int
    status: builtins.int
    """关系状态
    1:未关注 2:已关注 3:被关注 4:互关
    """

    is_follow: builtins.int
    """用户关注UP主"""

    is_followed: builtins.int
    """UP主关注用户"""

    def __init__(self,
        *,
        status: builtins.int = ...,
        is_follow: builtins.int = ...,
        is_followed: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_follow",b"is_follow","is_followed",b"is_followed","status",b"status"]) -> None: ...
global___Relation = Relation

class SearchReply(google.protobuf.message.Message):
    """搜索历史记录-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ITEMS_FIELD_NUMBER: builtins.int
    HASMORE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorItem]:
        """卡片内容"""
        pass
    hasMore: builtins.bool
    """是否未拉取完"""

    @property
    def page(self) -> global___Page:
        """页面信息"""
        pass
    def __init__(self,
        *,
        items: typing.Optional[typing.Iterable[global___CursorItem]] = ...,
        hasMore: builtins.bool = ...,
        page: typing.Optional[global___Page] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page",b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hasMore",b"hasMore","items",b"items","page",b"page"]) -> None: ...
global___SearchReply = SearchReply

class SearchReq(google.protobuf.message.Message):
    """搜索历史记录-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEYWORD_FIELD_NUMBER: builtins.int
    PN_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    keyword: typing.Text
    """关键词"""

    pn: builtins.int
    """页码"""

    business: typing.Text
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """

    def __init__(self,
        *,
        keyword: typing.Text = ...,
        pn: builtins.int = ...,
        business: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business",b"business","keyword",b"keyword","pn",b"pn"]) -> None: ...
global___SearchReq = SearchReq
