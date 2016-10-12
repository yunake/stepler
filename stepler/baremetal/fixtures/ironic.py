# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ironicclient import client as Client
import pytest

__all__ = [
    'ironic_client'
]


@pytest.fixture
def ironic_client(session):
    """Callable function fixture to get ironic client.

    Args:
        session (function): function to get keystone session

    Returns:
        ironicclient.v1.client.: instantiated ironic client
    """
    return Client.get_client('1', session=session)