#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# windows_registry_key - Windows Registry Key
#
# Copyright (C) 2020 Sam Daenen <sam.daenen@continu-it.be>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from cmk.gui.i18n import _

register_check_parameters(
    subgroup_applications,
    "windows_registry_key",
    _("Parameters for Windows Registry Keys"),
    Dictionary(
        elements = [
            ('keyvalue',
             ListOfStrings(
                 title = _('Key Value(s) to match'),
                 )),
        ],
        help=_('Regular expressions matching the values of the registry key'),
    ),
    TextAscii(
        title = _("Registry Path"),
        allow_empty = False,
        help=_('Regular expressions matching the patch of the registry key.'
                '<b>Remember to escape backslashes in the path!!</b>'),
    ),
    'dict',
)
