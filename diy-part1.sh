#!/bin/bash
set -e

# Official OpenWrt already provides the default feeds:
# packages, luci, routing, telephony.
# To reduce duplicate package conflicts on official OpenWrt 25.12.2,
# this build does not add broad third-party feeds here.
# Standalone third-party packages are cloned in diy-part2.sh.
