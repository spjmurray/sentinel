# Copyright 2017 DataCentred Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sentinel.api.controllers.volume.v2 import root as v2


class VolumeController(object):
    def __init__(self):
        self.v2 = v2.VolumeV2Controller()


class Service(object):
    service_name = u'cinderv2'
    service_type = u'volumev2'
    service_endpoint = u'/volume/v2'

    @staticmethod
    def controller():
        return VolumeController()

# vi: ts=4 et:

