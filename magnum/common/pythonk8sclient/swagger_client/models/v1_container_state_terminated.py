# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1ContainerStateTerminated(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'exit_code': 'int',
            'signal': 'int',
            'reason': 'str',
            'message': 'str',
            'started_at': 'str',
            'finished_at': 'str',
            'container_id': 'str'
        }

        self.attribute_map = {
            'exit_code': 'exitCode',
            'signal': 'signal',
            'reason': 'reason',
            'message': 'message',
            'started_at': 'startedAt',
            'finished_at': 'finishedAt',
            'container_id': 'containerID'
        }

        self._exit_code = None
        self._signal = None
        self._reason = None
        self._message = None
        self._started_at = None
        self._finished_at = None
        self._container_id = None

    @property
    def exit_code(self):
        """
        Gets the exit_code of this V1ContainerStateTerminated.
        exit status from the last termination of the container

        :return: The exit_code of this V1ContainerStateTerminated.
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """
        Sets the exit_code of this V1ContainerStateTerminated.
        exit status from the last termination of the container

        :param exit_code: The exit_code of this V1ContainerStateTerminated.
        :type: int
        """
        self._exit_code = exit_code

    @property
    def signal(self):
        """
        Gets the signal of this V1ContainerStateTerminated.
        signal from the last termination of the container

        :return: The signal of this V1ContainerStateTerminated.
        :rtype: int
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """
        Sets the signal of this V1ContainerStateTerminated.
        signal from the last termination of the container

        :param signal: The signal of this V1ContainerStateTerminated.
        :type: int
        """
        self._signal = signal

    @property
    def reason(self):
        """
        Gets the reason of this V1ContainerStateTerminated.
        (brief) reason from the last termination of the container

        :return: The reason of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1ContainerStateTerminated.
        (brief) reason from the last termination of the container

        :param reason: The reason of this V1ContainerStateTerminated.
        :type: str
        """
        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this V1ContainerStateTerminated.
        message regarding the last termination of the container

        :return: The message of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1ContainerStateTerminated.
        message regarding the last termination of the container

        :param message: The message of this V1ContainerStateTerminated.
        :type: str
        """
        self._message = message

    @property
    def started_at(self):
        """
        Gets the started_at of this V1ContainerStateTerminated.
        time at which previous execution of the container started

        :return: The started_at of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this V1ContainerStateTerminated.
        time at which previous execution of the container started

        :param started_at: The started_at of this V1ContainerStateTerminated.
        :type: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        """
        Gets the finished_at of this V1ContainerStateTerminated.
        time at which the container last terminated

        :return: The finished_at of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """
        Sets the finished_at of this V1ContainerStateTerminated.
        time at which the container last terminated

        :param finished_at: The finished_at of this V1ContainerStateTerminated.
        :type: str
        """
        self._finished_at = finished_at

    @property
    def container_id(self):
        """
        Gets the container_id of this V1ContainerStateTerminated.
        container's ID in the format 'docker://<container_id>'

        :return: The container_id of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this V1ContainerStateTerminated.
        container's ID in the format 'docker://<container_id>'

        :param container_id: The container_id of this V1ContainerStateTerminated.
        :type: str
        """
        self._container_id = container_id

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
