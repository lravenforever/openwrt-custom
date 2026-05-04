#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: check_config.py <openwrt/.config>", file=sys.stderr)
    sys.exit(2)

config = Path(sys.argv[1]).read_text(encoding="utf-8", errors="ignore")
lines = set(line.strip() for line in config.splitlines())

required_groups = [
    ("x86_64 generic target", ["CONFIG_TARGET_x86_64_DEVICE_generic=y"]),
    ("GRUB EFI image", ["CONFIG_GRUB_EFI_IMAGES=y"]),
    ("LuCI", ["CONFIG_PACKAGE_luci=y"]),
    ("LuCI package manager for OpenWrt 25.12 apk", ["CONFIG_PACKAGE_luci-app-package-manager=y"]),
    ("Argon theme", ["CONFIG_PACKAGE_luci-theme-argon=y"]),
    ("OpenAppFilter / OAF", ["CONFIG_PACKAGE_luci-app-oaf=y"]),
    ("AdGuardHome backend", ["CONFIG_PACKAGE_adguardhome=y"]),
    ("AdGuardHome LuCI", ["CONFIG_PACKAGE_luci-app-adguardhome=y"]),
    ("DDNS-GO LuCI", ["CONFIG_PACKAGE_luci-app-ddns-go=y"]),
    ("EQOS Plus", ["CONFIG_PACKAGE_luci-app-eqosplus=y"]),
    ("Netdata backend", ["CONFIG_PACKAGE_netdata=y"]),
    ("Netdata LuCI", ["CONFIG_PACKAGE_luci-app-netdata=y"]),
    ("Time control", ["CONFIG_PACKAGE_luci-app-nft-timecontrol=y", "CONFIG_PACKAGE_luci-app-timecontrol=y"]),
    ("NLBWMon", ["CONFIG_PACKAGE_luci-app-nlbwmon=y"]),
    ("Statistics", ["CONFIG_PACKAGE_luci-app-statistics=y"]),
    ("TTYD", ["CONFIG_PACKAGE_luci-app-ttyd=y"]),
]

missing = []
for name, alternatives in required_groups:
    if not any(item in lines for item in alternatives):
        missing.append((name, alternatives))

if missing:
    print("Some requested packages were not selected after make defconfig:")
    for name, alternatives in missing:
        print(f"- {name}: expected one of {', '.join(alternatives)}")
    print("\nThis usually means a package source did not clone correctly, the package name changed, or the package is incompatible with the selected OpenWrt target/version.")
    sys.exit(1)

print("All required package selections survived make defconfig.")
