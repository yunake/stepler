"""
-----------------
Floating IPs page
-----------------
"""

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

from pom import ui
from selenium.webdriver.common.by import By

from ..base import PageBase
from stepler.horizon.app import ui as _ui


class FormAllocateIP(_ui.Form):
    """Form to allocate IP."""


@ui.register_ui(
    item_release=ui.UI(By.CSS_SELECTOR, '[id$="action_release"]'))
class DropdownMenu(_ui.DropdownMenu):
    """Dropdown menu of floating IP."""


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=DropdownMenu())
class RowFloatingIP(_ui.Row):
    """Row with floating ip."""


class TableFloatingIPs(_ui.Table):
    """Table with floating IPs."""

    row_cls = RowFloatingIP


@ui.register_ui(combobox_port=_ui.combobox_by_label("Port to be associated"),
                combobox_float_ip=_ui.combobox_by_label("IP Address"))
class FormAssociate(_ui.Form):
    """Form to associate."""


@ui.register_ui(
    button_allocate_ip=ui.Button(By.ID, 'floating_ips__action_allocate'),
    form_allocate_ip=FormAllocateIP(By.ID, 'associate_floating_ip_form'),
    form_associate=FormAssociate(
        By.CSS_SELECTOR, '[action*="floating_ips/associate"]'),
    table_floating_ips=TableFloatingIPs(By.ID, 'floating_ips'))
class PageFloatingIPs(PageBase):
    """Floating IPs page."""
    url = "/project/floating_ips/"
