"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.archive.middleware.v1.preload_pb2
import bilireq.grpc.protos.bilibili.app.card.v1.common_pb2
import bilireq.grpc.protos.bilibili.app.dynamic.v2.dynamic_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _TopicCardType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _TopicCardTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TopicCardType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ILLEGAL_TYPE: _TopicCardType.ValueType  # 0
    """"""

    DYNAMIC: _TopicCardType.ValueType  # 1
    """"""

    FOLD: _TopicCardType.ValueType  # 2
    """"""

class TopicCardType(_TopicCardType, metaclass=_TopicCardTypeEnumTypeWrapper):
    """"""
    pass

ILLEGAL_TYPE: TopicCardType.ValueType  # 0
""""""

DYNAMIC: TopicCardType.ValueType  # 1
""""""

FOLD: TopicCardType.ValueType  # 2
""""""

global___TopicCardType = TopicCardType


class DetailsTopInfo(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_INFO_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    STATS_DESC_FIELD_NUMBER: builtins.int
    HAS_CREATE_JURISDICTION_FIELD_NUMBER: builtins.int
    OPERATION_CONTENT_FIELD_NUMBER: builtins.int
    HEAD_IMG_URL_FIELD_NUMBER: builtins.int
    HEAD_IMG_BACKCOLOR_FIELD_NUMBER: builtins.int
    WORD_COLOR_FIELD_NUMBER: builtins.int
    @property
    def topic_info(self) -> global___TopicInfo:
        """"""
        pass
    @property
    def user(self) -> global___User:
        """"""
        pass
    stats_desc: typing.Text
    """"""

    has_create_jurisdiction: builtins.bool
    """"""

    @property
    def operation_content(self) -> global___OperationContent:
        """"""
        pass
    head_img_url: typing.Text
    """"""

    head_img_backcolor: typing.Text
    """"""

    word_color: builtins.int
    """"""

    def __init__(self,
        *,
        topic_info: typing.Optional[global___TopicInfo] = ...,
        user: typing.Optional[global___User] = ...,
        stats_desc: typing.Text = ...,
        has_create_jurisdiction: builtins.bool = ...,
        operation_content: typing.Optional[global___OperationContent] = ...,
        head_img_url: typing.Text = ...,
        head_img_backcolor: typing.Text = ...,
        word_color: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["operation_content",b"operation_content","topic_info",b"topic_info","user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["has_create_jurisdiction",b"has_create_jurisdiction","head_img_backcolor",b"head_img_backcolor","head_img_url",b"head_img_url","operation_content",b"operation_content","stats_desc",b"stats_desc","topic_info",b"topic_info","user",b"user","word_color",b"word_color"]) -> None: ...
global___DetailsTopInfo = DetailsTopInfo

class FoldCardItem(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_SHOW_FOLD_FIELD_NUMBER: builtins.int
    FOLD_COUNT_FIELD_NUMBER: builtins.int
    CARD_SHOW_DESC_FIELD_NUMBER: builtins.int
    FOLD_DESC_FIELD_NUMBER: builtins.int
    is_show_fold: builtins.int
    """"""

    fold_count: builtins.int
    """"""

    card_show_desc: typing.Text
    """"""

    fold_desc: typing.Text
    """"""

    def __init__(self,
        *,
        is_show_fold: builtins.int = ...,
        fold_count: builtins.int = ...,
        card_show_desc: typing.Text = ...,
        fold_desc: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["card_show_desc",b"card_show_desc","fold_count",b"fold_count","fold_desc",b"fold_desc","is_show_fold",b"is_show_fold"]) -> None: ...
global___FoldCardItem = FoldCardItem

class FunctionalCard(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CAPSULES_FIELD_NUMBER: builtins.int
    TRAFFIC_CARD_FIELD_NUMBER: builtins.int
    GAME_CARD_FIELD_NUMBER: builtins.int
    @property
    def capsules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TopicCapsule]:
        """"""
        pass
    @property
    def traffic_card(self) -> global___TrafficCard:
        """"""
        pass
    @property
    def game_card(self) -> global___GameCard:
        """"""
        pass
    def __init__(self,
        *,
        capsules: typing.Optional[typing.Iterable[global___TopicCapsule]] = ...,
        traffic_card: typing.Optional[global___TrafficCard] = ...,
        game_card: typing.Optional[global___GameCard] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["game_card",b"game_card","traffic_card",b"traffic_card"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["capsules",b"capsules","game_card",b"game_card","traffic_card",b"traffic_card"]) -> None: ...
global___FunctionalCard = FunctionalCard

class GameCard(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GAME_ID_FIELD_NUMBER: builtins.int
    GAME_ICON_FIELD_NUMBER: builtins.int
    GAME_NAME_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    GAME_TAGS_FIELD_NUMBER: builtins.int
    NOTICE_FIELD_NUMBER: builtins.int
    GAME_LINK_FIELD_NUMBER: builtins.int
    game_id: builtins.int
    """"""

    game_icon: typing.Text
    """"""

    game_name: typing.Text
    """"""

    score: typing.Text
    """"""

    game_tags: typing.Text
    """"""

    notice: typing.Text
    """"""

    game_link: typing.Text
    """"""

    def __init__(self,
        *,
        game_id: builtins.int = ...,
        game_icon: typing.Text = ...,
        game_name: typing.Text = ...,
        score: typing.Text = ...,
        game_tags: typing.Text = ...,
        notice: typing.Text = ...,
        game_link: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["game_icon",b"game_icon","game_id",b"game_id","game_link",b"game_link","game_name",b"game_name","game_tags",b"game_tags","notice",b"notice","score",b"score"]) -> None: ...
global___GameCard = GameCard

class InlineProgressBar(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ICON_DRAG_FIELD_NUMBER: builtins.int
    ICON_DRAG_HASH_FIELD_NUMBER: builtins.int
    ICON_STOP_FIELD_NUMBER: builtins.int
    ICON_STOP_HASH_FIELD_NUMBER: builtins.int
    icon_drag: typing.Text
    """"""

    icon_drag_hash: typing.Text
    """"""

    icon_stop: typing.Text
    """"""

    icon_stop_hash: typing.Text
    """"""

    def __init__(self,
        *,
        icon_drag: typing.Text = ...,
        icon_drag_hash: typing.Text = ...,
        icon_stop: typing.Text = ...,
        icon_stop_hash: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["icon_drag",b"icon_drag","icon_drag_hash",b"icon_drag_hash","icon_stop",b"icon_stop","icon_stop_hash",b"icon_stop_hash"]) -> None: ...
global___InlineProgressBar = InlineProgressBar

class LargeCoverInline(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT1_FIELD_NUMBER: builtins.int
    COVER_LEFT_ICON1_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT2_FIELD_NUMBER: builtins.int
    COVER_LEFT_ICON2_FIELD_NUMBER: builtins.int
    RIGHT_TOP_LIVE_BADGE_FIELD_NUMBER: builtins.int
    EXTRA_URI_FIELD_NUMBER: builtins.int
    INLINE_PROGRESS_BAR_FIELD_NUMBER: builtins.int
    TOPIC_THREE_POINT_FIELD_NUMBER: builtins.int
    COVER_LEFT_DESC_FIELD_NUMBER: builtins.int
    HIDE_DANMU_SWITCH_FIELD_NUMBER: builtins.int
    DISABLE_DANMU_FIELD_NUMBER: builtins.int
    CAN_PLAY_FIELD_NUMBER: builtins.int
    DURATION_TEXT_FIELD_NUMBER: builtins.int
    RELATION_DATA_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """"""
        pass
    cover_left_text1: typing.Text
    """"""

    cover_left_icon1: builtins.int
    """"""

    cover_left_text2: typing.Text
    """"""

    cover_left_icon2: builtins.int
    """"""

    @property
    def right_top_live_badge(self) -> global___RightTopLiveBadge:
        """"""
        pass
    extra_uri: typing.Text
    """"""

    @property
    def inline_progress_bar(self) -> global___InlineProgressBar:
        """"""
        pass
    @property
    def topic_three_point(self) -> global___TopicThreePoint:
        """"""
        pass
    cover_left_desc: typing.Text
    """"""

    hide_danmu_switch: builtins.bool
    """"""

    disable_danmu: builtins.bool
    """"""

    can_play: builtins.int
    """"""

    duration_text: typing.Text
    """"""

    @property
    def relation_data(self) -> global___RelationData:
        """"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        cover_left_text1: typing.Text = ...,
        cover_left_icon1: builtins.int = ...,
        cover_left_text2: typing.Text = ...,
        cover_left_icon2: builtins.int = ...,
        right_top_live_badge: typing.Optional[global___RightTopLiveBadge] = ...,
        extra_uri: typing.Text = ...,
        inline_progress_bar: typing.Optional[global___InlineProgressBar] = ...,
        topic_three_point: typing.Optional[global___TopicThreePoint] = ...,
        cover_left_desc: typing.Text = ...,
        hide_danmu_switch: builtins.bool = ...,
        disable_danmu: builtins.bool = ...,
        can_play: builtins.int = ...,
        duration_text: typing.Text = ...,
        relation_data: typing.Optional[global___RelationData] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base","inline_progress_bar",b"inline_progress_bar","relation_data",b"relation_data","right_top_live_badge",b"right_top_live_badge","topic_three_point",b"topic_three_point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","can_play",b"can_play","cover_left_desc",b"cover_left_desc","cover_left_icon1",b"cover_left_icon1","cover_left_icon2",b"cover_left_icon2","cover_left_text1",b"cover_left_text1","cover_left_text2",b"cover_left_text2","disable_danmu",b"disable_danmu","duration_text",b"duration_text","extra_uri",b"extra_uri","hide_danmu_switch",b"hide_danmu_switch","inline_progress_bar",b"inline_progress_bar","relation_data",b"relation_data","right_top_live_badge",b"right_top_live_badge","topic_three_point",b"topic_three_point"]) -> None: ...
global___LargeCoverInline = LargeCoverInline

class LiveBadgeResource(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TEXT_FIELD_NUMBER: builtins.int
    ANIMATION_URL_FIELD_NUMBER: builtins.int
    ANIMATION_URL_HASH_FIELD_NUMBER: builtins.int
    BACKGROUND_COLOR_LIGHT_FIELD_NUMBER: builtins.int
    BACKGROUND_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    ALPHA_LIGHT_FIELD_NUMBER: builtins.int
    ALPHA_NIGHT_FIELD_NUMBER: builtins.int
    FONT_COLOR_FIELD_NUMBER: builtins.int
    text: typing.Text
    """"""

    animation_url: typing.Text
    """"""

    animation_url_hash: typing.Text
    """"""

    background_color_light: typing.Text
    """"""

    background_color_night: typing.Text
    """"""

    alpha_light: builtins.int
    """"""

    alpha_night: builtins.int
    """"""

    font_color: typing.Text
    """"""

    def __init__(self,
        *,
        text: typing.Text = ...,
        animation_url: typing.Text = ...,
        animation_url_hash: typing.Text = ...,
        background_color_light: typing.Text = ...,
        background_color_night: typing.Text = ...,
        alpha_light: builtins.int = ...,
        alpha_night: builtins.int = ...,
        font_color: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alpha_light",b"alpha_light","alpha_night",b"alpha_night","animation_url",b"animation_url","animation_url_hash",b"animation_url_hash","background_color_light",b"background_color_light","background_color_night",b"background_color_night","font_color",b"font_color","text",b"text"]) -> None: ...
global___LiveBadgeResource = LiveBadgeResource

class OperationCard(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LARGE_COVER_INLINE_FIELD_NUMBER: builtins.int
    @property
    def large_cover_inline(self) -> global___LargeCoverInline:
        """"""
        pass
    def __init__(self,
        *,
        large_cover_inline: typing.Optional[global___LargeCoverInline] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["card",b"card","large_cover_inline",b"large_cover_inline"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["card",b"card","large_cover_inline",b"large_cover_inline"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["card",b"card"]) -> typing.Optional[typing_extensions.Literal["large_cover_inline"]]: ...
global___OperationCard = OperationCard

class OperationContent(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATION_CARD_FIELD_NUMBER: builtins.int
    @property
    def operation_card(self) -> global___OperationCard:
        """"""
        pass
    def __init__(self,
        *,
        operation_card: typing.Optional[global___OperationCard] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["operation_card",b"operation_card"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["operation_card",b"operation_card"]) -> None: ...
global___OperationContent = OperationContent

class RelationData(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_FAV_FIELD_NUMBER: builtins.int
    IS_COIN_FIELD_NUMBER: builtins.int
    IS_FOLLOW_FIELD_NUMBER: builtins.int
    IS_LIKE_FIELD_NUMBER: builtins.int
    LIKE_COUNT_FIELD_NUMBER: builtins.int
    is_fav: builtins.bool
    """"""

    is_coin: builtins.bool
    """"""

    is_follow: builtins.bool
    """"""

    is_like: builtins.bool
    """"""

    like_count: builtins.int
    """"""

    def __init__(self,
        *,
        is_fav: builtins.bool = ...,
        is_coin: builtins.bool = ...,
        is_follow: builtins.bool = ...,
        is_like: builtins.bool = ...,
        like_count: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_coin",b"is_coin","is_fav",b"is_fav","is_follow",b"is_follow","is_like",b"is_like","like_count",b"like_count"]) -> None: ...
global___RelationData = RelationData

class RightTopLiveBadge(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIVE_STATUS_FIELD_NUMBER: builtins.int
    IN_LIVE_FIELD_NUMBER: builtins.int
    LIVE_STATS_DESC_FIELD_NUMBER: builtins.int
    live_status: builtins.int
    """"""

    @property
    def in_live(self) -> global___LiveBadgeResource:
        """"""
        pass
    live_stats_desc: typing.Text
    """"""

    def __init__(self,
        *,
        live_status: builtins.int = ...,
        in_live: typing.Optional[global___LiveBadgeResource] = ...,
        live_stats_desc: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["in_live",b"in_live"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["in_live",b"in_live","live_stats_desc",b"live_stats_desc","live_status",b"live_status"]) -> None: ...
global___RightTopLiveBadge = RightTopLiveBadge

class SortContent(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SORT_BY_FIELD_NUMBER: builtins.int
    SORT_NAME_FIELD_NUMBER: builtins.int
    sort_by: builtins.int
    """"""

    sort_name: typing.Text
    """"""

    def __init__(self,
        *,
        sort_by: builtins.int = ...,
        sort_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sort_by",b"sort_by","sort_name",b"sort_name"]) -> None: ...
global___SortContent = SortContent

class ThreePointItem(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TITLE_FIELD_NUMBER: builtins.int
    JUMP_URL_FIELD_NUMBER: builtins.int
    title: typing.Text
    """"""

    jump_url: typing.Text
    """"""

    def __init__(self,
        *,
        title: typing.Text = ...,
        jump_url: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jump_url",b"jump_url","title",b"title"]) -> None: ...
global___ThreePointItem = ThreePointItem

class TopicActivities(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACTIVITY_FIELD_NUMBER: builtins.int
    ACT_LIST_TITLE_FIELD_NUMBER: builtins.int
    @property
    def activity(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TopicActivity]:
        """"""
        pass
    act_list_title: typing.Text
    """"""

    def __init__(self,
        *,
        activity: typing.Optional[typing.Iterable[global___TopicActivity]] = ...,
        act_list_title: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["act_list_title",b"act_list_title","activity",b"activity"]) -> None: ...
global___TopicActivities = TopicActivities

class TopicActivity(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACTIVITY_ID_FIELD_NUMBER: builtins.int
    ACTIVITY_NAME_FIELD_NUMBER: builtins.int
    JUMP_URL_FIELD_NUMBER: builtins.int
    ICON_URL_FIELD_NUMBER: builtins.int
    activity_id: builtins.int
    """"""

    activity_name: typing.Text
    """"""

    jump_url: typing.Text
    """"""

    icon_url: typing.Text
    """"""

    def __init__(self,
        *,
        activity_id: builtins.int = ...,
        activity_name: typing.Text = ...,
        jump_url: typing.Text = ...,
        icon_url: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activity_id",b"activity_id","activity_name",b"activity_name","icon_url",b"icon_url","jump_url",b"jump_url"]) -> None: ...
global___TopicActivity = TopicActivity

class TopicCapsule(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    JUMP_URL_FIELD_NUMBER: builtins.int
    ICON_URL_FIELD_NUMBER: builtins.int
    name: typing.Text
    """"""

    jump_url: typing.Text
    """"""

    icon_url: typing.Text
    """"""

    def __init__(self,
        *,
        name: typing.Text = ...,
        jump_url: typing.Text = ...,
        icon_url: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["icon_url",b"icon_url","jump_url",b"jump_url","name",b"name"]) -> None: ...
global___TopicCapsule = TopicCapsule

class TopicCardItem(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    DYNAMIC_ITEM_FIELD_NUMBER: builtins.int
    FORD_CARD_ITEM_FIELD_NUMBER: builtins.int
    type: builtins.int
    """"""

    @property
    def dynamic_item(self) -> bilibili.app.dynamic.v2.dynamic_pb2.DynamicItem:
        """"""
        pass
    @property
    def ford_card_item(self) -> global___FoldCardItem:
        """"""
        pass
    def __init__(self,
        *,
        type: builtins.int = ...,
        dynamic_item: typing.Optional[bilibili.app.dynamic.v2.dynamic_pb2.DynamicItem] = ...,
        ford_card_item: typing.Optional[global___FoldCardItem] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dynamic_item",b"dynamic_item","ford_card_item",b"ford_card_item"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dynamic_item",b"dynamic_item","ford_card_item",b"ford_card_item","type",b"type"]) -> None: ...
global___TopicCardItem = TopicCardItem

class TopicCardList(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_CARD_ITEMS_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    HAS_MORE_FIELD_NUMBER: builtins.int
    TOPIC_SORT_BY_CONF_FIELD_NUMBER: builtins.int
    @property
    def topic_card_items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TopicCardItem]:
        """"""
        pass
    offset: typing.Text
    """"""

    has_more: builtins.bool
    """"""

    @property
    def topic_sort_by_conf(self) -> global___TopicSortByConf:
        """"""
        pass
    def __init__(self,
        *,
        topic_card_items: typing.Optional[typing.Iterable[global___TopicCardItem]] = ...,
        offset: typing.Text = ...,
        has_more: builtins.bool = ...,
        topic_sort_by_conf: typing.Optional[global___TopicSortByConf] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["topic_sort_by_conf",b"topic_sort_by_conf"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["has_more",b"has_more","offset",b"offset","topic_card_items",b"topic_card_items","topic_sort_by_conf",b"topic_sort_by_conf"]) -> None: ...
global___TopicCardList = TopicCardList

class TopicDetailsAllReply(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DETAILS_TOP_INFO_FIELD_NUMBER: builtins.int
    TOPIC_ACTIVITIES_FIELD_NUMBER: builtins.int
    TOPIC_CARD_LIST_FIELD_NUMBER: builtins.int
    FUNCTIONAL_CARD_FIELD_NUMBER: builtins.int
    @property
    def details_top_info(self) -> global___DetailsTopInfo:
        """"""
        pass
    @property
    def topic_activities(self) -> global___TopicActivities:
        """"""
        pass
    @property
    def topic_card_list(self) -> global___TopicCardList:
        """"""
        pass
    @property
    def functional_card(self) -> global___FunctionalCard:
        """"""
        pass
    def __init__(self,
        *,
        details_top_info: typing.Optional[global___DetailsTopInfo] = ...,
        topic_activities: typing.Optional[global___TopicActivities] = ...,
        topic_card_list: typing.Optional[global___TopicCardList] = ...,
        functional_card: typing.Optional[global___FunctionalCard] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["details_top_info",b"details_top_info","functional_card",b"functional_card","topic_activities",b"topic_activities","topic_card_list",b"topic_card_list"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["details_top_info",b"details_top_info","functional_card",b"functional_card","topic_activities",b"topic_activities","topic_card_list",b"topic_card_list"]) -> None: ...
global___TopicDetailsAllReply = TopicDetailsAllReply

class TopicDetailsAllReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_ID_FIELD_NUMBER: builtins.int
    SORT_BY_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    LOCAL_TIME_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    NEED_REFRESH_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    topic_id: builtins.int
    """"""

    sort_by: builtins.int
    """"""

    offset: typing.Text
    """"""

    page_size: builtins.int
    """"""

    local_time: builtins.int
    """"""

    @property
    def player_args(self) -> bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """"""
        pass
    need_refresh: builtins.int
    """"""

    source: typing.Text
    """"""

    def __init__(self,
        *,
        topic_id: builtins.int = ...,
        sort_by: builtins.int = ...,
        offset: typing.Text = ...,
        page_size: builtins.int = ...,
        local_time: builtins.int = ...,
        player_args: typing.Optional[bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs] = ...,
        need_refresh: builtins.int = ...,
        source: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["player_args",b"player_args"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["local_time",b"local_time","need_refresh",b"need_refresh","offset",b"offset","page_size",b"page_size","player_args",b"player_args","sort_by",b"sort_by","source",b"source","topic_id",b"topic_id"]) -> None: ...
global___TopicDetailsAllReq = TopicDetailsAllReq

class TopicDetailsFoldReply(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_CARD_LIST_FIELD_NUMBER: builtins.int
    FOLD_COUNT_FIELD_NUMBER: builtins.int
    @property
    def topic_card_list(self) -> global___TopicCardList:
        """"""
        pass
    fold_count: builtins.int
    """"""

    def __init__(self,
        *,
        topic_card_list: typing.Optional[global___TopicCardList] = ...,
        fold_count: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["topic_card_list",b"topic_card_list"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fold_count",b"fold_count","topic_card_list",b"topic_card_list"]) -> None: ...
global___TopicDetailsFoldReply = TopicDetailsFoldReply

class TopicDetailsFoldReq(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPIC_ID_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    LOCAL_TIME_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    FROM_SORT_BY_FIELD_NUMBER: builtins.int
    topic_id: builtins.int
    """"""

    offset: typing.Text
    """"""

    page_size: builtins.int
    """"""

    local_time: builtins.int
    """"""

    @property
    def player_args(self) -> bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """"""
        pass
    from_sort_by: builtins.int
    """"""

    def __init__(self,
        *,
        topic_id: builtins.int = ...,
        offset: typing.Text = ...,
        page_size: builtins.int = ...,
        local_time: builtins.int = ...,
        player_args: typing.Optional[bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs] = ...,
        from_sort_by: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["player_args",b"player_args"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["from_sort_by",b"from_sort_by","local_time",b"local_time","offset",b"offset","page_size",b"page_size","player_args",b"player_args","topic_id",b"topic_id"]) -> None: ...
global___TopicDetailsFoldReq = TopicDetailsFoldReq

class TopicInfo(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    DISCUSS_FIELD_NUMBER: builtins.int
    FAV_FIELD_NUMBER: builtins.int
    DYNAMICS_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    JUMP_URL_FIELD_NUMBER: builtins.int
    BACKCOLOR_FIELD_NUMBER: builtins.int
    IS_FAV_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATE_SOURCE_FIELD_NUMBER: builtins.int
    SHARE_PIC_FIELD_NUMBER: builtins.int
    SHARE_FIELD_NUMBER: builtins.int
    LIKE_FIELD_NUMBER: builtins.int
    SHARE_URL_FIELD_NUMBER: builtins.int
    IS_LIKE_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""

    name: typing.Text
    """"""

    uid: builtins.int
    """"""

    view: builtins.int
    """"""

    discuss: builtins.int
    """"""

    fav: builtins.int
    """"""

    dynamics: builtins.int
    """"""

    state: builtins.int
    """"""

    jump_url: typing.Text
    """"""

    backcolor: typing.Text
    """"""

    is_fav: builtins.bool
    """"""

    description: typing.Text
    """"""

    create_source: builtins.int
    """"""

    share_pic: typing.Text
    """"""

    share: builtins.int
    """"""

    like: builtins.int
    """"""

    share_url: typing.Text
    """"""

    is_like: builtins.bool
    """"""

    def __init__(self,
        *,
        id: builtins.int = ...,
        name: typing.Text = ...,
        uid: builtins.int = ...,
        view: builtins.int = ...,
        discuss: builtins.int = ...,
        fav: builtins.int = ...,
        dynamics: builtins.int = ...,
        state: builtins.int = ...,
        jump_url: typing.Text = ...,
        backcolor: typing.Text = ...,
        is_fav: builtins.bool = ...,
        description: typing.Text = ...,
        create_source: builtins.int = ...,
        share_pic: typing.Text = ...,
        share: builtins.int = ...,
        like: builtins.int = ...,
        share_url: typing.Text = ...,
        is_like: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backcolor",b"backcolor","create_source",b"create_source","description",b"description","discuss",b"discuss","dynamics",b"dynamics","fav",b"fav","id",b"id","is_fav",b"is_fav","is_like",b"is_like","jump_url",b"jump_url","like",b"like","name",b"name","share",b"share","share_pic",b"share_pic","share_url",b"share_url","state",b"state","uid",b"uid","view",b"view"]) -> None: ...
global___TopicInfo = TopicInfo

class TopicSortByConf(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEFAULT_SORT_BY_FIELD_NUMBER: builtins.int
    ALL_SORT_BY_FIELD_NUMBER: builtins.int
    SHOW_SORT_BY_FIELD_NUMBER: builtins.int
    default_sort_by: builtins.int
    """"""

    @property
    def all_sort_by(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SortContent]:
        """"""
        pass
    show_sort_by: builtins.int
    """"""

    def __init__(self,
        *,
        default_sort_by: builtins.int = ...,
        all_sort_by: typing.Optional[typing.Iterable[global___SortContent]] = ...,
        show_sort_by: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["all_sort_by",b"all_sort_by","default_sort_by",b"default_sort_by","show_sort_by",b"show_sort_by"]) -> None: ...
global___TopicSortByConf = TopicSortByConf

class TopicThreePoint(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DYN_THREE_POINT_ITEMS_FIELD_NUMBER: builtins.int
    @property
    def dyn_three_point_items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThreePointItem]:
        """"""
        pass
    def __init__(self,
        *,
        dyn_three_point_items: typing.Optional[typing.Iterable[global___ThreePointItem]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dyn_three_point_items",b"dyn_three_point_items"]) -> None: ...
global___TopicThreePoint = TopicThreePoint

class TrafficCard(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    JUMP_URL_FIELD_NUMBER: builtins.int
    ICON_URL_FIELD_NUMBER: builtins.int
    BASE_PIC_FIELD_NUMBER: builtins.int
    BENEFIT_POINT_FIELD_NUMBER: builtins.int
    CARD_DESC_FIELD_NUMBER: builtins.int
    JUMP_TITLE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """"""

    jump_url: typing.Text
    """"""

    icon_url: typing.Text
    """"""

    base_pic: typing.Text
    """"""

    benefit_point: typing.Text
    """"""

    card_desc: typing.Text
    """"""

    jump_title: typing.Text
    """"""

    def __init__(self,
        *,
        name: typing.Text = ...,
        jump_url: typing.Text = ...,
        icon_url: typing.Text = ...,
        base_pic: typing.Text = ...,
        benefit_point: typing.Text = ...,
        card_desc: typing.Text = ...,
        jump_title: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_pic",b"base_pic","benefit_point",b"benefit_point","card_desc",b"card_desc","icon_url",b"icon_url","jump_title",b"jump_title","jump_url",b"jump_url","name",b"name"]) -> None: ...
global___TrafficCard = TrafficCard

class User(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UID_FIELD_NUMBER: builtins.int
    FACE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NAME_DESC_FIELD_NUMBER: builtins.int
    uid: builtins.int
    """"""

    face: typing.Text
    """"""

    name: typing.Text
    """"""

    name_desc: typing.Text
    """"""

    def __init__(self,
        *,
        uid: builtins.int = ...,
        face: typing.Text = ...,
        name: typing.Text = ...,
        name_desc: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["face",b"face","name",b"name","name_desc",b"name_desc","uid",b"uid"]) -> None: ...
global___User = User
