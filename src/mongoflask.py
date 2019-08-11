from datetime import date, datetime

import isodate as iso
from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter
from http import HTTPStatus


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)

def find_restaurants(mongo, _id=None):
    query = {}
    result = ''
    if _id:
        # Added "try" to catch invalid values for ObjectId
        try:
            query["_id"] = (ObjectId(_id))
        except Exception as e:
            return 'ID Error: Not valid ID specified'

        # With "find_one" I get a json object
        result = mongo.db.restaurant.find_one(query)
        # Testing 'result' value for return 204 status code
        if result is None:
            result = '', HTTPStatus.NO_CONTENT

    else:
        result = list(mongo.db.restaurant.find(query))

    return result
