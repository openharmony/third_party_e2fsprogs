Name:           e2fsprogs
Version:        1.46.4
Release:        7
Summary:        Second extended file system management tools
License:        GPLv2+ and LGPLv2 and MIT
URL:            http://e2fsprogs.sourceforge.net/
Source0:        https://www.kernel.org/pub/linux/kernel/people/tytso/%{name}/v%{version}/%{name}-%{version}.tar.xz

Patch1:		0001-e2fsprogs-set-hugefile-from-4T-to-1T-in-hugefile-tes.patch
Patch2:		0002-libss-add-newer-libreadline.so.8-to-dlopen-path.patch
Patch3:		0003-tests-update-expect-files-for-f_mmp_garbage.patch
Patch4:		0004-tests-update-expect-files-for-f_large_dir-and-f_larg.patch
Patch5:		0005-resize2fs-resize2fs-disk-hardlinks-will-be-error.patch
Patch6:		0006-e2fsck-exit-journal-recovery-when-find-EIO-ENOMEM-er.patch
Patch7:		0007-e2fsck-exit-journal-recovery-when-jounral-superblock.patch
Patch8:		0008-e2fsck-add-env-param-E2FS_UNRELIABLE_IO-to-fi.patch
Patch9:		0009-e2mmpstatus.8.in-detele-filesystem-can-be-UUID-or-LA.patch		
Patch10:	0010-tests-update-expect-file-for-u_direct_io.patch
Patch11:	0011-libext2fs-don-t-old-the-CACHE_MTX-while-doing-I-O.patch
Patch12:	0012-tests-skip-m_rootdir_acl-if-selinux-is-not-disabled.patch


BuildRequires:  gcc pkgconfig texinfo
BuildRequires:  fuse-devel libblkid-devel libuuid-devel
BuildRequires:  audit
Recommends:	%{name}-help = %{version}-%{release}

Provides:       e2fsprogs-libs%{?_isa} e2fsprogs-libs
Obsoletes:      e2fsprogs-libs
Provides:       libcom_err%{?_isa} libcom_err
Obsoletes:      libcom_err
Provides:       libss%{?_isa} libss
Obsoletes:      libss

%description
The e2fsprogs package consists of a lot of tools for users to create,
check, modify, and correct any inconsistencies in second extended file
system.

%package devel
Summary: Second extended file system libraries and headers
License: GPLv2 and LGPLv2 and MIT
Requires: e2fsprogs = %{version}-%{release}
Requires: gawk
Requires: pkgconfig
Requires(post): info
Requires(preun): info
Provides: libcom_err-devel%{?_isa} libcom_err-devel
Obsoletes: libcom_err-devel
Provides: libss-devel%{?_isa} libss-devel
Obsoletes: libss-devel
Provides: e2fsprogs-static{?_isa} e2fsprogs-static
Obsoletes: e2fsprogs-static

%description devel
This package provides libraries and header files to develop
second extended file system userspace programs.

%package help
Summary: man files for e2fsprogs
Requires: man
BuildArch: noarch

%description help
This packages includes man files for e2fsprogs.

%prep
%autosetup -n %{name}-%{version} -p1


%build
%configure CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
           --enable-elf-shlibs --enable-nls --disable-uuidd --disable-fsck \
           --disable-e2initrd-helper --disable-libblkid --disable-libuuid \
           --enable-quota --with-root-prefix=/usr
%make_build V=1

%install
make install install-libs DESTDIR=%{buildroot} INSTALL="%{__install} -p" \
    root_sbindir=%{_sbindir} root_libdir=%{_libdir}
chmod +w %{buildroot}%{_libdir}/*.a

%find_lang %{name}

rm -f %{buildroot}/etc/cron.d/e2scrub_all
rm -f %{buildroot}%{_libdir}/e2fsprogs/e2scrub_all_cron

%check
make fullcheck

%ldconfig_scriptlets

%post devel
if [ -f %{_infodir}/libext2fs.info.gz ]; then
   /sbin/install-info %{_infodir}/libext2fs.info.gz %{_infodir}/dir || :
fi

%preun devel
if [ $1 = 0 -a -f %{_infodir}/libext2fs.info.gz ]; then
   /sbin/install-info --delete %{_infodir}/libext2fs.info.gz %{_infodir}/dir || :
fi
exit 0

%files -f %{name}.lang
%doc README RELEASE-NOTES
%license NOTICE
%config(noreplace) /etc/mke2fs.conf
%config(noreplace) /etc/e2scrub.conf
%{_bindir}/chattr
%{_bindir}/fuse2fs
%{_bindir}/lsattr
%{_libdir}/e2fsprogs/e2scrub_fail
%{_libdir}/libe2p.so.*
%{_libdir}/libext2fs.so.*
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*
%{_sbindir}/*
%{_udevrulesdir}/*.rules
%{_unitdir}/e2scrub*

%files devel
%{_bindir}/compile_et
%{_bindir}/mk_cmds
%{_datadir}/et
%{_datadir}/ss
%{_infodir}/libext2fs.info*
%{_includedir}/e2p
%{_includedir}/ext2fs
%{_includedir}/et
%{_includedir}/com_err.h
%{_includedir}/ss
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.a

%files help
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
* Thu Feb 17 2022 zhanchengbin <zhanchengbin1@huawei.com> - 1.46.4-7
- tests: skip m_rootdir_acl if selinux is not disabled

* Wed Feb 9 2022 zhanchengbin <zhanchengbin1@huawei.com> - 1.46.4-6
- libext2fs: don't old the CACHE_MTX while doing I/O

* Thu Feb 8 2022 zhanchengbin <zhanchengbin1@huawei.com> - 1.46.4-5
- tests: update expect file for u_direct_io

* Wed Mar 2 2022 zhanchengbin <zhanchengbin1@huawei.com> - 1.46.4-4
- e2mmpstatus.8.in: detele filesystem can be UUID or LABEL in manpage 

* Thu Feb 24 2022 zhanchengbin <zhanchengbin1@huawei.com> - 1.46.4-3
- adapt patchs from openEuler-20.03-LTS

* Thu Jan 27 2022 zhanchengbin <zhanchengbin1@huawei.com> - 1.46.4-2
- replace License in spec

* Sat Nov 27 2021 zhanchengbin <zhanchengbin1@huawei.com> - 1.46.4-1
- update package to v1.46.4.

* Mon Nov 15 2021 zhanchengbin <zhanchengbin1@huawei.com> - 1.45.6-7
- DESC: integrate community patches.

* Sun Sep 13 2021 lixiaokeng <lixiaokeng@huawei.com> - 1.45.6-6
- DESC: add newer libreadline.so.8 to dlopen path

* Fri Aug 20 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.45.6-5
- DESC: add necessary BuildRequires audit

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.45.6-4
- DESC: delete -Sgit from %autosetup, and delete BuildRequires git

* Wed Dec 16 2020 yanglongkang <yanglongkang@huawei.com> - 1.45.6-3
- Set help package as install require

* Fri Oct 30 2020 Zhiqiang Liu <lzhq28@mail.ustc.edu.cn> - 1.45.6-2
- backport upstream patches-epoch2 to fix some problems

* Wed Jul 15 2020 Zhiqiang Liu <lzhq28@mail.ustc.edu.cn> - 1.45.6-1
- rebuild package

* Wed Jul 1 2020 Wu Bo <wubo009@163.com> - 1.45.3-5
- rebuild package

* Mon Feb 3 2020 luoshijie <luoshijie1@huawei.com> - 1.45.3-4
- Type:cves
- ID:CVE-2019-5094
- SUG:restart
- DESC:backport patch to fix CVE-2019-5094.

* Wed Jan 22 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.45.3-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:change path to remove no used file.

* Wed Jan 22 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.45.3-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix local rpmbuild error.

* Mon Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.45.3-1
- Type:cves
- ID:CVE-2019-5188
- SUG:restart
- DESC:backport patch to fix CVE-2019-5188.

* Mon Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.45.3-0
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update package from 1.44.3 to 1.45.3.

* Mon Jan 13 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.44.3-8
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update spec.

* Wed Sep 18 2019 luoshijie <luoshijie1@huawei.com> - 1.44.3-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify spec file to follow spec rules.

* Fri Sep 6 2019 luoshijie <luoshijie1@huawei.com> - 1.44.3-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:openEuler Debranding

* Tue Aug 20 2019 luoshijie <luoshijie1@huawei.com> - 1.44.3-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:rename patch name

* Wed Jul 10 2019 zhangyujing <zhangyujing1@huawei.com> - 1.44.3-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:e2freefrag: fix memory leak in scan_online()
       create_inode: fix potential memory leak in path_append()
       mke2fs: fix check for absurdly large devices

* Fri Mar 15 2019 zhangyujing <zhangyujing1@huawei.com> - 1.44.3-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:blkid avoid FPE crash when probing a HFS superblock
       AOSP e2fsdroid Fix crash with invalid command line a
       e2fsck fix fd leak in reserve_stdio_fds
       libext2fs fix uninitialized length in rep_strdup
       tune2fs fix dereference of freed memory after journa
       libe2p avoid segfault when s_nr_users is too high
       e2freefrag fix free blocks count during live scan

* Wed Jan 23 2019 wangxiao <wangxiao65@huawei.com> - 1.44.3-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:disable the metadata_csum creat by mke2fs -t ext4 by default
- Package init

