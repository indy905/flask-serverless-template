import json
from datetime import datetime

from pynamodb.attributes import MapAttribute, UnicodeAttribute
from pynamodb.models import Model


class BaseModel(Model):
    class Meta:
        abstract = True

    created_date = UnicodeAttribute(default_for_new=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))
    updated_date = UnicodeAttribute(default_for_new=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))

    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def to_dict(self):
        ret_dict = {}
        for name, attr in self.attribute_values.items():
            ret_dict[name] = self._attr2obj(attr)

        return ret_dict

    def _attr2obj(self, attr):
        # compare with list class. It is not ListAttribute.
        if isinstance(attr, list):
            _list = []
            for l in attr:
                _list.append(self._attr2obj(l))
            return _list
        elif isinstance(attr, MapAttribute):
            _dict = {}
            for k, v in attr.attribute_values.items():
                _dict[k] = self._attr2obj(v)
            return _dict
        elif isinstance(attr, datetime):
            return attr.isoformat()
        else:
            return attr

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
