from flaskr.config.ma import ma
from flaskr.models import Item


class ItemListResponseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item

    id = ma.auto_field()
    name = ma.auto_field()
    checked = ma.auto_field()


class ItemCreateRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item

    name = ma.auto_field(required=True)
    category_id = ma.auto_field(required=False)
