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


class V1VolumeMount(object):
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
        'mount_path': 'str',
        'mount_propagation': 'str',
        'name': 'str',
        'read_only': 'bool',
        'sub_path': 'str',
        'sub_path_expr': 'str'
    }

    attribute_map = {
        'mount_path': 'mountPath',
        'mount_propagation': 'mountPropagation',
        'name': 'name',
        'read_only': 'readOnly',
        'sub_path': 'subPath',
        'sub_path_expr': 'subPathExpr'
    }

    def __init__(self, mount_path=None, mount_propagation=None, name=None, read_only=None, sub_path=None, sub_path_expr=None, local_vars_configuration=None):  # noqa: E501
        """V1VolumeMount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mount_path = None
        self._mount_propagation = None
        self._name = None
        self._read_only = None
        self._sub_path = None
        self._sub_path_expr = None
        self.discriminator = None

        self.mount_path = mount_path
        if mount_propagation is not None:
            self.mount_propagation = mount_propagation
        self.name = name
        if read_only is not None:
            self.read_only = read_only
        if sub_path is not None:
            self.sub_path = sub_path
        if sub_path_expr is not None:
            self.sub_path_expr = sub_path_expr

    @property
    def mount_path(self):
        """Gets the mount_path of this V1VolumeMount.  # noqa: E501

        Path within the container at which the volume should be mounted.  Must not contain ':'.  # noqa: E501

        :return: The mount_path of this V1VolumeMount.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this V1VolumeMount.

        Path within the container at which the volume should be mounted.  Must not contain ':'.  # noqa: E501

        :param mount_path: The mount_path of this V1VolumeMount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mount_path is None:  # noqa: E501
            raise ValueError("Invalid value for `mount_path`, must not be `None`")  # noqa: E501

        self._mount_path = mount_path

    @property
    def mount_propagation(self):
        """Gets the mount_propagation of this V1VolumeMount.  # noqa: E501

        mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.  # noqa: E501

        :return: The mount_propagation of this V1VolumeMount.  # noqa: E501
        :rtype: str
        """
        return self._mount_propagation

    @mount_propagation.setter
    def mount_propagation(self, mount_propagation):
        """Sets the mount_propagation of this V1VolumeMount.

        mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.  # noqa: E501

        :param mount_propagation: The mount_propagation of this V1VolumeMount.  # noqa: E501
        :type: str
        """

        self._mount_propagation = mount_propagation

    @property
    def name(self):
        """Gets the name of this V1VolumeMount.  # noqa: E501

        This must match the Name of a Volume.  # noqa: E501

        :return: The name of this V1VolumeMount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1VolumeMount.

        This must match the Name of a Volume.  # noqa: E501

        :param name: The name of this V1VolumeMount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def read_only(self):
        """Gets the read_only of this V1VolumeMount.  # noqa: E501

        Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.  # noqa: E501

        :return: The read_only of this V1VolumeMount.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1VolumeMount.

        Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.  # noqa: E501

        :param read_only: The read_only of this V1VolumeMount.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def sub_path(self):
        """Gets the sub_path of this V1VolumeMount.  # noqa: E501

        Path within the volume from which the container's volume should be mounted. Defaults to \"\" (volume's root).  # noqa: E501

        :return: The sub_path of this V1VolumeMount.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this V1VolumeMount.

        Path within the volume from which the container's volume should be mounted. Defaults to \"\" (volume's root).  # noqa: E501

        :param sub_path: The sub_path of this V1VolumeMount.  # noqa: E501
        :type: str
        """

        self._sub_path = sub_path

    @property
    def sub_path_expr(self):
        """Gets the sub_path_expr of this V1VolumeMount.  # noqa: E501

        Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to \"\" (volume's root). SubPathExpr and SubPath are mutually exclusive.  # noqa: E501

        :return: The sub_path_expr of this V1VolumeMount.  # noqa: E501
        :rtype: str
        """
        return self._sub_path_expr

    @sub_path_expr.setter
    def sub_path_expr(self, sub_path_expr):
        """Sets the sub_path_expr of this V1VolumeMount.

        Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to \"\" (volume's root). SubPathExpr and SubPath are mutually exclusive.  # noqa: E501

        :param sub_path_expr: The sub_path_expr of this V1VolumeMount.  # noqa: E501
        :type: str
        """

        self._sub_path_expr = sub_path_expr

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
        if not isinstance(other, V1VolumeMount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VolumeMount):
            return True

        return self.to_dict() != other.to_dict()
