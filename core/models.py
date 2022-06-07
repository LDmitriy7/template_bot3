import mongoengine as me


class CallbackButton(me.Document):
    id: str = me.StringField(primary_key=True)
    text: str = me.StringField()
    data: str = me.StringField()
    args: dict = me.DictField()
