# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .configurable_transformation_names import ConfigurableTransformationNames
from .transformation_category_names import TransformationCategoryNames


class ConfigurableTransformationDefinition(pydantic.BaseModel):
    """
    Schema for a transformation definition.
    """

    label: str = pydantic.Field(
        description="The label field will be used to display the name of the component in the UI"
    )
    json_schema: typing.Dict[str, typing.Any] = pydantic.Field(
        description="The json_schema field can be used by clients to determine how to construct the component"
    )
    configurable_transformation_type: ConfigurableTransformationNames = pydantic.Field(
        description="The name field will act as the unique identifier of TransformationDefinition objects"
    )
    transformation_category: TransformationCategoryNames = pydantic.Field(
        description="The transformation_category field will be used to group transformations in the UI"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
