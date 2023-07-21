#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
if [ -d "e2fsprogs" ];then
    exit 0
fi
tar xvf e2fsprogs-1.46.4.tar.xz
cd $1/e2fsprogs
patch -p1 < $1/0001-e2fsprogs-set-hugefile-from-4T-to-1T-in-hugefile-tes.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0002-libss-add-newer-libreadline.so.8-to-dlopen-path.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0003-tests-update-expect-files-for-f_mmp_garbage.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0004-tests-update-expect-files-for-f_large_dir-and-f_larg.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0005-resize2fs-resize2fs-disk-hardlinks-will-be-error.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0006-e2fsck-exit-journal-recovery-when-find-EIO-ENOMEM-er.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0007-e2fsck-exit-journal-recovery-when-jounral-superblock.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0008-e2fsck-add-env-param-E2FS_UNRELIABLE_IO-to-fi.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0009-e2mmpstatus.8.in-detele-filesystem-can-be-UUID-or-LA.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0010-tests-update-expect-file-for-u_direct_io.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0011-libext2fs-don-t-old-the-CACHE_MTX-while-doing-I-O.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/0012-tests-skip-m_rootdir_acl-if-selinux-is-not-disabled.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/1001-image-make.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/1002-add-header-file-to-musl-compile-mk2efs.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/1003-add-dac-config.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/1004-modify-code-to-compile.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/1005-read-vfat-chinese-label.patch --fuzz=0 --no-backup-if-mismatch
exit 0
