# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.22
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1LimitedPriorityLevelConfiguration(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'assured_concurrency_shares': 'int',
        'limit_response': 'V1beta1LimitResponse'
    }

    attribute_map = {
        'assured_concurrency_shares': 'assuredConcurrencyShares',
        'limit_response': 'limitResponse'
    }

    def __init__(self, assured_concurrency_shares=None, limit_response=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1LimitedPriorityLevelConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assured_concurrency_shares = None
        self._limit_response = None
        self.discriminator = None

        if assured_concurrency_shares is not None:
            self.assured_concurrency_shares = assured_concurrency_shares
        if limit_response is not None:
            self.limit_response = limit_response

    @property
    def assured_concurrency_shares(self):
        """Gets the assured_concurrency_shares of this V1beta1LimitedPriorityLevelConfiguration.  # noqa: E501

        `assuredConcurrencyShares` (ACS) configures the execution limit, which is a limit on the number of requests of this priority level that may be exeucting at a given time.  ACS must be a positive number. The server's concurrency limit (SCL) is divided among the concurrency-controlled priority levels in proportion to their assured concurrency shares. This produces the assured concurrency value (ACV) --- the number of requests that may be executing at a time --- for each such priority level:              ACV(l) = ceil( SCL * ACS(l) / ( sum[priority levels k] ACS(k) ) )  bigger numbers of ACS mean more reserved concurrent requests (at the expense of every other PL). This field has a default value of 30.  # noqa: E501

        :return: The assured_concurrency_shares of this V1beta1LimitedPriorityLevelConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._assured_concurrency_shares

    @assured_concurrency_shares.setter
    def assured_concurrency_shares(self, assured_concurrency_shares):
        """Sets the assured_concurrency_shares of this V1beta1LimitedPriorityLevelConfiguration.

        `assuredConcurrencyShares` (ACS) configures the execution limit, which is a limit on the number of requests of this priority level that may be exeucting at a given time.  ACS must be a positive number. The server's concurrency limit (SCL) is divided among the concurrency-controlled priority levels in proportion to their assured concurrency shares. This produces the assured concurrency value (ACV) --- the number of requests that may be executing at a time --- for each such priority level:              ACV(l) = ceil( SCL * ACS(l) / ( sum[priority levels k] ACS(k) ) )  bigger numbers of ACS mean more reserved concurrent requests (at the expense of every other PL). This field has a default value of 30.  # noqa: E501

        :param assured_concurrency_shares: The assured_concurrency_shares of this V1beta1LimitedPriorityLevelConfiguration.  # noqa: E501
        :type: int
        """

        self._assured_concurrency_shares = assured_concurrency_shares

    @property
    def limit_response(self):
        """Gets the limit_response of this V1beta1LimitedPriorityLevelConfiguration.  # noqa: E501


        :return: The limit_response of this V1beta1LimitedPriorityLevelConfiguration.  # noqa: E501
        :rtype: V1beta1LimitResponse
        """
        return self._limit_response

    @limit_response.setter
    def limit_response(self, limit_response):
        """Sets the limit_response of this V1beta1LimitedPriorityLevelConfiguration.


        :param limit_response: The limit_response of this V1beta1LimitedPriorityLevelConfiguration.  # noqa: E501
        :type: V1beta1LimitResponse
        """

        self._limit_response = limit_response

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V1beta1LimitedPriorityLevelConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1LimitedPriorityLevelConfiguration):
            return True

        return self.to_dict() != other.to_dict()
