# coding: utf-8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

import pprint
import re  # noqa: F401

import six


class Body(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'price': 'float',
        'id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'price': 'price',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, price=None, id=None, type=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501

        self._price = None
        self._id = None
        self._type = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def price(self):
        """Gets the price of this Body.  # noqa: E501

        petprice  # noqa: E501

        :return: The price of this Body.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Body.

        petprice  # noqa: E501

        :param price: The price of this Body.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def id(self):
        """Gets the id of this Body.  # noqa: E501

        petId  # noqa: E501

        :return: The id of this Body.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Body.

        petId  # noqa: E501

        :param id: The id of this Body.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Body.  # noqa: E501

        pettype  # noqa: E501

        :return: The type of this Body.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body.

        pettype  # noqa: E501

        :param type: The type of this Body.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
