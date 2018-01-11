# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import copy

from tastypie.resources import Resource, fields, HttpResponse


class BaseJsonModel(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}
        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data


class MyTestResource(Resource):
    name = fields.CharField(attribute='name')

    class Meta:
        resource_name = 'test_resource'
        allow_methods = ['get']
        object_class = BaseJsonModel

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del (data_dict['meta'])
                # Rename the objects.
                # data_dict['testobjects'] = copy.copy(data_dict['objects'])
                # del (data_dict['objects'])

        return data_dict['objects'][0]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)

    def get_object_list(self, request):
        result = {'name': 'lee'}
        new_obj = BaseJsonModel()
        new_obj.name = result['name']
        rs = [new_obj]
        return rs

    def dehydrate(self, bundle):
        bundle.data['age'] = 10
        bundle.data.pop('resource_uri')
        return bundle
