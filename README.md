# OpenWrt 25.12.2 x86_64 UEFI firmware build

This repository is ready for GitHub Actions compilation of an official OpenWrt 25.12.2 x86_64 generic firmware for standard UEFI BIOS x86 devices.

## Included target

- Source: official OpenWrt repository
- Version: `v25.12.2`
- Target: `x86/64 generic`
- Boot mode: UEFI GRUB image enabled with legacy GRUB image still enabled
- Recommended firmware file after build: `*generic-*-combined-efi.img.gz`
- Kernel/boot partition size: 32 MB
- Rootfs partition size: 1024 MB

For your described device, a standard x86 UEFI BIOS machine, this target is appropriate. After the build finishes, use the artifact whose filename contains `combined-efi.img.gz`; write the whole decompressed disk image to the target SSD/USB disk, not to a single partition.

## Main plugins included

The original orange `luci-app-accesscontrol-plus` selection has been replaced with OpenAppFilter because OAF is a closer match for app-aware parental control and traffic classification.

- `luci-app-oaf`
- `luci-app-adguardhome`
- `luci-app-ddns-go`
- `luci-app-eqosplus`
- `luci-app-netdata`
- `luci-app-nft-timecontrol` or `luci-app-timecontrol`
- `luci-app-nlbwmon`
- `luci-app-statistics`
- `luci-app-ttyd`
- `luci-theme-argon`

## Files

- `.github/workflows/openwrt-builder.yml` - GitHub Actions workflow.
- `.config` - x86_64 OpenWrt config with the selected plugins.
- `diy-part1.sh` - reserved for feed edits before `feeds update`.
- `diy-part2.sh` - clones third-party standalone packages into `package/custom`.
- `scripts/check_config.py` - fails early if requested package selections are dropped by `make defconfig`.

## Usage

1. Replace all files in your GitHub repository with the contents of this zip.
2. Push to GitHub.
3. Open **Actions** > **Build OpenWrt Firmware**.
4. Click **Run workflow**.
5. Download the finished artifact from the workflow run. For UEFI boot, use `openwrt-25.12.2-x86-64-generic-ext4-combined-efi.img.gz` or `openwrt-25.12.2-x86-64-generic-squashfs-combined-efi.img.gz` if both are produced.

Release creation is disabled by default. When manually running the workflow, set `release=true` if you want a GitHub Release to be created after a successful build.

## Notes

OpenWrt 25.12 uses `apk` instead of `opkg`, so this config uses `luci-app-package-manager` rather than `luci-app-opkg`.


## UEFI install reminder

The `combined-efi.img.gz` files are whole-disk images. Decompress first, then write the `.img` to the entire disk, for example `/dev/sdX` or `/dev/nvme0n1`, not to `/dev/sdX1` or `/dev/nvme0n1p1`.
