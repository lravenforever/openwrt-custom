#!/bin/bash
set -e

mkdir -p package/custom

rm -rf package/custom/OpenAppFilter
rm -rf package/custom/ddns-go
rm -rf package/custom/luci-app-eqosplus
rm -rf package/custom/luci-app-timecontrol
rm -rf package/custom/luci-app-netdata
rm -rf package/custom/luci-theme-argon
rm -rf package/custom/luci-app-adguardhome

# OpenAppFilter: app-aware parental control / DPI filtering.
# v6.1.8 release is based on OpenWrt 25.12.2.
git clone --depth 1 --branch v6.1.8 https://github.com/destan19/OpenAppFilter.git package/custom/OpenAppFilter

# DDNS-GO LuCI plugin.
git clone --depth 1 https://github.com/sirpdboy/luci-app-ddns-go.git package/custom/ddns-go

# EQOS Plus, timed bandwidth control.
git clone --depth 1 https://github.com/sirpdboy/luci-app-eqosplus.git package/custom/luci-app-eqosplus

# Time Control / nft-timecontrol. The upstream package name can differ by branch,
# so .config includes both luci-app-nft-timecontrol and luci-app-timecontrol.
git clone --depth 1 https://github.com/sirpdboy/luci-app-timecontrol.git package/custom/luci-app-timecontrol

# Netdata LuCI integration.
git clone --depth 1 https://github.com/sirpdboy/luci-app-netdata.git package/custom/luci-app-netdata

# Argon theme.
git clone --depth 1 https://github.com/jerrykuku/luci-theme-argon.git package/custom/luci-theme-argon

# AdGuardHome LuCI integration.
git clone --depth 1 https://github.com/xptsp/luci-app-adguardhome.git package/custom/luci-app-adguardhome

# Optional default LAN IP change. Keep official default 192.168.1.1 by default.
# To change it, uncomment and edit the line below.
# sed -i 's/192.168.1.1/192.168.2.1/g' package/base-files/files/bin/config_generate
