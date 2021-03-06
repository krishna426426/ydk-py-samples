#!/usr/bin/env python
#
# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Encode configuration for model Cisco-IOS-XR-ip-domain-cfg.

usage: cd-encode-xr-ip-domain-cfg-21-ydk.py [-h] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urlparse import urlparse

from ydk.services import CodecService
from ydk.providers import CodecServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ip_domain_cfg \
    as xr_ip_domain_cfg
import logging


def config_ip_domain(ip_domain):
    """Add config data to ip_domain object."""
    vrf = ip_domain.vrfs.Vrf()
    vrf.vrf_name = "default"
    # host name "east"
    ipv6_host = vrf.ipv6_hosts.Ipv6Host()
    ipv6_host.host_name = "east"
    ipv6_host.address.append("2001:db8::1")
    vrf.ipv6_hosts.ipv6_host.append(ipv6_host)
    # host name "west"
    ipv6_host = vrf.ipv6_hosts.Ipv6Host()
    ipv6_host.host_name = "west"
    ipv6_host.address.append("2001:db8::2")
    vrf.ipv6_hosts.ipv6_host.append(ipv6_host)
    # host name "north"
    ipv6_host = vrf.ipv6_hosts.Ipv6Host()
    ipv6_host.host_name = "north"
    ipv6_host.address.append("2001:db8::3")
    ipv6_host.address.append("2001:db8::4")
    vrf.ipv6_hosts.ipv6_host.append(ipv6_host)
    # host name "south"
    ipv6_host = vrf.ipv6_hosts.Ipv6Host()
    ipv6_host.host_name = "south"
    ipv6_host.address.append("2001:db8::5")
    ipv6_host.address.append("2001:db8::6")
    vrf.ipv6_hosts.ipv6_host.append(ipv6_host)
    ip_domain.vrfs.vrf.append(vrf)


if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    args = parser.parse_args()

    # log debug messages if verbose argument specified
    if args.verbose:
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s"))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # create codec provider
    provider = CodecServiceProvider(type="xml")

    # create codec service
    codec = CodecService()

    ip_domain = xr_ip_domain_cfg.IpDomain()  # create object
    config_ip_domain(ip_domain)  # add object configuration

    # encode and print object
    print(codec.encode(provider, ip_domain))

    exit()
# End of script
