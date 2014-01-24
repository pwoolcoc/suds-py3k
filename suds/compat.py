# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the 
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )

# ripped off from github.com/kennethreitz/requests.git

import sys

major, minor, _, _, _ = sys.version_info

try:
    import simplejson as json
except ImportError:
    import json

is_py2 = (major == 2)
is_py3 = (major == 3)

if is_py2:
    builtin_str = str
    bytes = str
    str = unicode
    unicode = unicode
    basestring = basestring
    long = long
    numeric_types = (int, float, long)
    from cookielib import CookieJar
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
    from urlparse import urlparse, urljoin
    from urllib2 import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, HTTPError

elif is_py3:
    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    long = int
    numeric_types = (int, float)
    from http.cookiejar import CookieJar
    from io import StringIO
    from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler
    from urllib.error import HTTPError
    from urllib.parse import urlparse, urljoin

