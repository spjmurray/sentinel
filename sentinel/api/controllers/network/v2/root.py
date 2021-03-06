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

from sentinel.api.controllers.network.v2 import floatingips
from sentinel.api.controllers.network.v2 import quotas


class NetworkV2Controller(object):
    def __init__(self):
        self.floatingips = floatingips.NetworkV2FloatingipsController()
        self.quotas = quotas.NetworkV2QuotasController()

# vi: ts=4 et:
