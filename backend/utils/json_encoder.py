from json import dumps
from datetime import datetime, date, time
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [
                x
                for x in dir(obj)
                if not x.startswith("_")
                and x not in (
                    "metadata",
                    "query",
                    "query_class",
                    "registry",
                )
            ]:
                data = obj.__getattribute__(field)
                try:
                    dumps(data)
                    fields[field] = data
                except TypeError:
                    if isinstance(data, list):
                        fields[field] = [self.default(item) for item in data]
                    elif isinstance(data.__class__, DeclarativeMeta):
                        fields[field] = self.default(data)
                    elif isinstance(data, datetime) or isinstance(data, date) or isinstance(data, time):
                        fields[field] = str(data)
                    else:
                        fields[field] = None
            return fields

        return super().default(obj)
