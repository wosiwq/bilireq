"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.dynamic.common.dynamic_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DynamicButtonClickBizType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _DynamicButtonClickBizTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DynamicButtonClickBizType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DYNAMIC_BUTTON_CLICK_BIZ_TYPE_NONE: _DynamicButtonClickBizType.ValueType  # 0
    """"""

    DYNAMIC_BUTTON_CLICK_BIZ_TYPE_LIVE: _DynamicButtonClickBizType.ValueType  # 1
    """"""

    DYNAMIC_BUTTON_CLICK_BIZ_TYPE_DYN_UP: _DynamicButtonClickBizType.ValueType  # 2
    """"""

class DynamicButtonClickBizType(_DynamicButtonClickBizType, metaclass=_DynamicButtonClickBizTypeEnumTypeWrapper):
    """"""
    pass

DYNAMIC_BUTTON_CLICK_BIZ_TYPE_NONE: DynamicButtonClickBizType.ValueType  # 0
""""""

DYNAMIC_BUTTON_CLICK_BIZ_TYPE_LIVE: DynamicButtonClickBizType.ValueType  # 1
""""""

DYNAMIC_BUTTON_CLICK_BIZ_TYPE_DYN_UP: DynamicButtonClickBizType.ValueType  # 2
""""""

global___DynamicButtonClickBizType = DynamicButtonClickBizType


class _ReserveButtonMode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ReserveButtonModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReserveButtonMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESERVE_BUTTON_MODE_NONE: _ReserveButtonMode.ValueType  # 0
    """"""

    RESERVE_BUTTON_MODE_RESERVE: _ReserveButtonMode.ValueType  # 1
    """"""

    RESERVE_BUTTON_MODE_UP_CANCEL: _ReserveButtonMode.ValueType  # 2
    """"""

class ReserveButtonMode(_ReserveButtonMode, metaclass=_ReserveButtonModeEnumTypeWrapper):
    """"""
    pass

RESERVE_BUTTON_MODE_NONE: ReserveButtonMode.ValueType  # 0
""""""

RESERVE_BUTTON_MODE_RESERVE: ReserveButtonMode.ValueType  # 1
""""""

RESERVE_BUTTON_MODE_UP_CANCEL: ReserveButtonMode.ValueType  # 2
""""""

global___ReserveButtonMode = ReserveButtonMode


class _ReserveButtonStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ReserveButtonStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReserveButtonStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESERVE_BUTTON_STATUS_NONE: _ReserveButtonStatus.ValueType  # 0
    """"""

    RESERVE_BUTTON_STATUS_UNCHECK: _ReserveButtonStatus.ValueType  # 1
    """"""

    RESERVE_BUTTON_STATUS_CHECK: _ReserveButtonStatus.ValueType  # 2
    """"""

class ReserveButtonStatus(_ReserveButtonStatus, metaclass=_ReserveButtonStatusEnumTypeWrapper):
    """"""
    pass

RESERVE_BUTTON_STATUS_NONE: ReserveButtonStatus.ValueType  # 0
""""""

RESERVE_BUTTON_STATUS_UNCHECK: ReserveButtonStatus.ValueType  # 1
""""""

RESERVE_BUTTON_STATUS_CHECK: ReserveButtonStatus.ValueType  # 2
""""""

global___ReserveButtonStatus = ReserveButtonStatus


class CreateDynReq(google.protobuf.message.Message):
    """创建动态-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    META_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    SCENE_FIELD_NUMBER: builtins.int
    PICS_FIELD_NUMBER: builtins.int
    REPOST_SRC_FIELD_NUMBER: builtins.int
    VIDEO_FIELD_NUMBER: builtins.int
    SKETCH_TYPE_FIELD_NUMBER: builtins.int
    SKETCH_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    DYN_TAG_FIELD_NUMBER: builtins.int
    ATTACH_CARD_FIELD_NUMBER: builtins.int
    OPTION_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    UPLOAD_ID_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> bilibili.dynamic.common.dynamic_pb2.UserCreateMeta:
        """用户创建接口meta信息"""
        pass
    @property
    def content(self) -> bilibili.dynamic.common.dynamic_pb2.CreateContent:
        """发布的内容"""
        pass
    scene: bilibili.dynamic.common.dynamic_pb2.CreateScene.ValueType
    """发布类型"""

    @property
    def pics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[bilibili.dynamic.common.dynamic_pb2.CreatePic]:
        """图片内容"""
        pass
    @property
    def repost_src(self) -> bilibili.dynamic.common.dynamic_pb2.DynIdentity:
        """转发源"""
        pass
    @property
    def video(self) -> bilibili.dynamic.common.dynamic_pb2.CreateDynVideo:
        """动态视频"""
        pass
    sketch_type: builtins.int
    """通用模板类型：2048方图 2049竖图 其他值无效"""

    @property
    def sketch(self) -> bilibili.dynamic.common.dynamic_pb2.Sketch:
        """通用模板的元内容（网页内容）"""
        pass
    @property
    def program(self) -> bilibili.dynamic.common.dynamic_pb2.Program:
        """小程序的内容"""
        pass
    @property
    def dyn_tag(self) -> bilibili.dynamic.common.dynamic_pb2.CreateTag:
        """动态附加小卡"""
        pass
    @property
    def attach_card(self) -> bilibili.dynamic.common.dynamic_pb2.CreateAttachCard:
        """动态附加大卡"""
        pass
    @property
    def option(self) -> bilibili.dynamic.common.dynamic_pb2.CreateOption:
        """特殊的创建选项"""
        pass
    @property
    def topic(self) -> bilibili.dynamic.common.dynamic_pb2.CreateTopic:
        """"""
        pass
    upload_id: typing.Text
    """"""

    def __init__(self,
        *,
        meta: typing.Optional[bilibili.dynamic.common.dynamic_pb2.UserCreateMeta] = ...,
        content: typing.Optional[bilibili.dynamic.common.dynamic_pb2.CreateContent] = ...,
        scene: bilibili.dynamic.common.dynamic_pb2.CreateScene.ValueType = ...,
        pics: typing.Optional[typing.Iterable[bilibili.dynamic.common.dynamic_pb2.CreatePic]] = ...,
        repost_src: typing.Optional[bilibili.dynamic.common.dynamic_pb2.DynIdentity] = ...,
        video: typing.Optional[bilibili.dynamic.common.dynamic_pb2.CreateDynVideo] = ...,
        sketch_type: builtins.int = ...,
        sketch: typing.Optional[bilibili.dynamic.common.dynamic_pb2.Sketch] = ...,
        program: typing.Optional[bilibili.dynamic.common.dynamic_pb2.Program] = ...,
        dyn_tag: typing.Optional[bilibili.dynamic.common.dynamic_pb2.CreateTag] = ...,
        attach_card: typing.Optional[bilibili.dynamic.common.dynamic_pb2.CreateAttachCard] = ...,
        option: typing.Optional[bilibili.dynamic.common.dynamic_pb2.CreateOption] = ...,
        topic: typing.Optional[bilibili.dynamic.common.dynamic_pb2.CreateTopic] = ...,
        upload_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["attach_card",b"attach_card","content",b"content","dyn_tag",b"dyn_tag","meta",b"meta","option",b"option","program",b"program","repost_src",b"repost_src","sketch",b"sketch","topic",b"topic","video",b"video"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attach_card",b"attach_card","content",b"content","dyn_tag",b"dyn_tag","meta",b"meta","option",b"option","pics",b"pics","program",b"program","repost_src",b"repost_src","scene",b"scene","sketch",b"sketch","sketch_type",b"sketch_type","topic",b"topic","upload_id",b"upload_id","video",b"video"]) -> None: ...
global___CreateDynReq = CreateDynReq

class CreateInitCheckReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SCENE_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    REPOST_FIELD_NUMBER: builtins.int
    scene: builtins.int
    """"""

    @property
    def meta(self) -> bilibili.dynamic.common.dynamic_pb2.MetaDataCtrl:
        """"""
        pass
    @property
    def repost(self) -> bilibili.dynamic.common.dynamic_pb2.RepostInitCheck:
        """"""
        pass
    def __init__(self,
        *,
        scene: builtins.int = ...,
        meta: typing.Optional[bilibili.dynamic.common.dynamic_pb2.MetaDataCtrl] = ...,
        repost: typing.Optional[bilibili.dynamic.common.dynamic_pb2.RepostInitCheck] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta",b"meta","repost",b"repost"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["meta",b"meta","repost",b"repost","scene",b"scene"]) -> None: ...
global___CreateInitCheckReq = CreateInitCheckReq

class CreatePageInfosReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_ID_FIELD_NUMBER: builtins.int
    topic_id: builtins.int
    """"""

    def __init__(self,
        *,
        topic_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["topic_id",b"topic_id"]) -> None: ...
global___CreatePageInfosReq = CreatePageInfosReq

class CreatePageInfosRsp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_FIELD_NUMBER: builtins.int
    @property
    def topic(self) -> global___CreatePageTopicInfo:
        """"""
        pass
    def __init__(self,
        *,
        topic: typing.Optional[global___CreatePageTopicInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["topic",b"topic"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["topic",b"topic"]) -> None: ...
global___CreatePageInfosRsp = CreatePageInfosRsp

class CreatePageTopicInfo(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_ID_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    topic_id: builtins.int
    """"""

    topic_name: typing.Text
    """"""

    def __init__(self,
        *,
        topic_id: builtins.int = ...,
        topic_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["topic_id",b"topic_id","topic_name",b"topic_name"]) -> None: ...
global___CreatePageTopicInfo = CreatePageTopicInfo

class CreatePermissionButtonClickReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    type: global___DynamicButtonClickBizType.ValueType
    """"""

    def __init__(self,
        *,
        type: global___DynamicButtonClickBizType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["type",b"type"]) -> None: ...
global___CreatePermissionButtonClickReq = CreatePermissionButtonClickReq

class CreatePermissionButtonClickRsp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CreatePermissionButtonClickRsp = CreatePermissionButtonClickRsp

class CreatePlusButtonClickReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CreatePlusButtonClickReq = CreatePlusButtonClickReq

class CreatePlusButtonClickRsp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CreatePlusButtonClickRsp = CreatePlusButtonClickRsp

class DynamicButtonClickReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DynamicButtonClickReq = DynamicButtonClickReq

class DynamicButtonClickRsp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DynamicButtonClickRsp = DynamicButtonClickRsp

class HotSearchReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___HotSearchReq = HotSearchReq

class HotSearchRsp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Item(google.protobuf.message.Message):
        """"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        WORDS_FIELD_NUMBER: builtins.int
        words: typing.Text
        """"""

        def __init__(self,
            *,
            words: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["words",b"words"]) -> None: ...

    ITEMS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HotSearchRsp.Item]:
        """"""
        pass
    version: typing.Text
    """"""

    def __init__(self,
        *,
        items: typing.Optional[typing.Iterable[global___HotSearchRsp.Item]] = ...,
        version: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["items",b"items","version",b"version"]) -> None: ...
global___HotSearchRsp = HotSearchRsp

class ReserveButtonClickReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UID_FIELD_NUMBER: builtins.int
    RESERVE_ID_FIELD_NUMBER: builtins.int
    RESERVE_TOTAL_FIELD_NUMBER: builtins.int
    CUR_BTN_STATUS_FIELD_NUMBER: builtins.int
    SPMID_FIELD_NUMBER: builtins.int
    DYN_ID_FIELD_NUMBER: builtins.int
    DYN_TYPE_FIELD_NUMBER: builtins.int
    uid: builtins.int
    """"""

    reserve_id: builtins.int
    """"""

    reserve_total: builtins.int
    """"""

    cur_btn_status: builtins.int
    """"""

    spmid: typing.Text
    """"""

    dyn_id: builtins.int
    """"""

    dyn_type: builtins.int
    """"""

    def __init__(self,
        *,
        uid: builtins.int = ...,
        reserve_id: builtins.int = ...,
        reserve_total: builtins.int = ...,
        cur_btn_status: builtins.int = ...,
        spmid: typing.Text = ...,
        dyn_id: builtins.int = ...,
        dyn_type: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cur_btn_status",b"cur_btn_status","dyn_id",b"dyn_id","dyn_type",b"dyn_type","reserve_id",b"reserve_id","reserve_total",b"reserve_total","spmid",b"spmid","uid",b"uid"]) -> None: ...
global___ReserveButtonClickReq = ReserveButtonClickReq

class ReserveButtonClickResp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FINAL_BTN_STATUS_FIELD_NUMBER: builtins.int
    BTN_MODE_FIELD_NUMBER: builtins.int
    RESERVE_UPDATE_FIELD_NUMBER: builtins.int
    DESC_UPDATE_FIELD_NUMBER: builtins.int
    HAS_ACTIVITY_FIELD_NUMBER: builtins.int
    ACTIVITY_URL_FIELD_NUMBER: builtins.int
    TOAST_FIELD_NUMBER: builtins.int
    final_btn_status: global___ReserveButtonStatus.ValueType
    """"""

    btn_mode: global___ReserveButtonMode.ValueType
    """"""

    reserve_update: builtins.int
    """"""

    desc_update: typing.Text
    """"""

    has_activity: builtins.bool
    """"""

    activity_url: typing.Text
    """"""

    toast: typing.Text
    """"""

    def __init__(self,
        *,
        final_btn_status: global___ReserveButtonStatus.ValueType = ...,
        btn_mode: global___ReserveButtonMode.ValueType = ...,
        reserve_update: builtins.int = ...,
        desc_update: typing.Text = ...,
        has_activity: builtins.bool = ...,
        activity_url: typing.Text = ...,
        toast: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activity_url",b"activity_url","btn_mode",b"btn_mode","desc_update",b"desc_update","final_btn_status",b"final_btn_status","has_activity",b"has_activity","reserve_update",b"reserve_update","toast",b"toast"]) -> None: ...
global___ReserveButtonClickResp = ReserveButtonClickResp

class SubmitCheckReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTENT_FIELD_NUMBER: builtins.int
    PICS_FIELD_NUMBER: builtins.int
    @property
    def content(self) -> bilibili.dynamic.common.dynamic_pb2.CreateContent:
        """"""
        pass
    @property
    def pics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[bilibili.dynamic.common.dynamic_pb2.CreatePic]:
        """"""
        pass
    def __init__(self,
        *,
        content: typing.Optional[bilibili.dynamic.common.dynamic_pb2.CreateContent] = ...,
        pics: typing.Optional[typing.Iterable[bilibili.dynamic.common.dynamic_pb2.CreatePic]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content",b"content"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","pics",b"pics"]) -> None: ...
global___SubmitCheckReq = SubmitCheckReq

class SubmitCheckRsp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___SubmitCheckRsp = SubmitCheckRsp

class SuggestReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    S_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    s: typing.Text
    """"""

    type: builtins.int
    """"""

    def __init__(self,
        *,
        s: typing.Text = ...,
        type: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["s",b"s","type",b"type"]) -> None: ...
global___SuggestReq = SuggestReq

class SuggestRsp(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIST_FIELD_NUMBER: builtins.int
    TRACK_ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    @property
    def list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """"""
        pass
    track_id: typing.Text
    """"""

    version: typing.Text
    """"""

    def __init__(self,
        *,
        list: typing.Optional[typing.Iterable[typing.Text]] = ...,
        track_id: typing.Text = ...,
        version: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["list",b"list","track_id",b"track_id","version",b"version"]) -> None: ...
global___SuggestRsp = SuggestRsp
