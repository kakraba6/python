# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2016 BigML
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
from world import world

from bigml.api import HTTP_OK

#@step(r'I get the lda "(.*)"')
def i_get_the_lda(step, lda):
    resource = world.api.get_lda(lda)
    world.status = resource['code']
    assert world.status == HTTP_OK
    world.lda = resource['object']

#@step(r'I get the topic distribution "(.*)"')
def i_get_the_topic_distribution(step, topic_distribution):
    resource = world.api.get_topic_distribution(topic_distribution)
    world.status = resource['code']
    assert world.status == HTTP_OK
    world.topic_distribution = resource['object']
