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

register_rule(
    "agents/" + _("Agent Plugins"),
    "agent_config:windows_registry_key",
    Alternative(
        title = _("Windows Registry Key"),
        help = _("This will deploy the agent plugin <tt>windowsregistrykey</tt> "
                 "for checking Windows Registry Keys"),
        style = "dropdown",
        elements = [
            Dictionary(
                title = _("Deploy the Windows Registry Key plugin"),
                elements = [
                    ("interval", Age(
                        title = _("Run asynchronously"),
                        label = _("Interval for collecting data"),
                        default_value = 3600
                    )),
                   ( "paths",
                     ListOfStrings(
                        title = _("Paths of the Registry keys you want to check"),
                        help = _('Enter path patterns that will be searched for registry key values.'),
                        valuespec = TextAscii(
                            size = 120,
                        ),
                       allow_empty = False,

                     )
                   ),
                ],
                optional_keys = [ 'interval' ],
            ),
            FixedValue(None, title = _("Do not deploy the Windows Registry Key plugin"), totext = _("(disabled)") ),
        ]
    ),
)
