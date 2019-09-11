#!/usr/bin/env python3

""" Suspends the wicd daemon.

Sets a flag in the daemon that will stop it from monitoring network status.
Used for when a laptop enters hibernation/suspension.

"""

#
#   Copyright (C) 2007 - 2009 Adam Blackburn
#   Copyright (C) 2007 - 2009 Dan O'Reilly
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License Version 2 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import dbus
import dbus.service
import sys

try:
    bus = dbus.SystemBus()
    proxy_obj = bus.get_object('org.wicd.daemon', '/org/wicd/daemon')
    daemon = dbus.Interface(proxy_obj, 'org.wicd.daemon')
except Exception as e:
    print("Exception caught: %s" % str(e), file=sys.stderr)
    print('Could not connect to daemon.', file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    try:
        daemon.Disconnect()
        daemon.SetForcedDisconnect(False)
        daemon.SetSuspend(True)
    except Exception as e:
        print("Exception caught: %s" % str(e), file=sys.stderr)
        print('Error setting suspend.', file=sys.stderr)
        sys.exit(2)
