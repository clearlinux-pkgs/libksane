#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libksane
Version  : 24.08.0
Release  : 69
URL      : https://download.kde.org/stable/release-service/24.08.0/src/libksane-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/libksane-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/libksane-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: libksane-data = %{version}-%{release}
Requires: libksane-lib = %{version}-%{release}
Requires: libksane-license = %{version}-%{release}
Requires: libksane-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : ksanecore-dev
BuildRequires : sane-backends-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KSane
## Introduction
SANE Library Qt-based interface
## Authors
See AUTHORS file for details.

%package data
Summary: data components for the libksane package.
Group: Data

%description data
data components for the libksane package.


%package dev
Summary: dev components for the libksane package.
Group: Development
Requires: libksane-lib = %{version}-%{release}
Requires: libksane-data = %{version}-%{release}
Provides: libksane-devel = %{version}-%{release}
Requires: libksane = %{version}-%{release}

%description dev
dev components for the libksane package.


%package lib
Summary: lib components for the libksane package.
Group: Libraries
Requires: libksane-data = %{version}-%{release}
Requires: libksane-license = %{version}-%{release}

%description lib
lib components for the libksane package.


%package license
Summary: license components for the libksane package.
Group: Default

%description license
license components for the libksane package.


%package locales
Summary: locales components for the libksane package.
Group: Default

%description locales
locales components for the libksane package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libksane-24.08.0
cd %{_builddir}/libksane-24.08.0
pushd ..
cp -a libksane-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724431203
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724431203
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksane
cp %{_builddir}/libksane-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libksane/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libksane-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/libksane/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/libksane-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libksane/b9c8ec07abddb6bfbe08cb87aa8f68c2c2a1152f || :
cp %{_builddir}/libksane-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksane/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libksane-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksane/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libksane
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/16x16/actions/black-white.png
/usr/share/icons/hicolor/16x16/actions/color.png
/usr/share/icons/hicolor/16x16/actions/gray-scale.png

%files dev
%defattr(-,root,root,-)
/usr/include/KSaneWidgets6/KSaneWidget
/usr/include/KSaneWidgets6/ksane_export.h
/usr/include/KSaneWidgets6/ksane_version.h
/usr/include/KSaneWidgets6/ksanewidget.h
/usr/lib64/cmake/KSaneWidgets6/KSaneWidgets6Config.cmake
/usr/lib64/cmake/KSaneWidgets6/KSaneWidgets6ConfigVersion.cmake
/usr/lib64/cmake/KSaneWidgets6/KSaneWidgets6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KSaneWidgets6/KSaneWidgets6Targets.cmake
/usr/lib64/libKSaneWidgets6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKSaneWidgets6.so.24.08.0
/usr/lib64/libKSaneWidgets6.so.24.08.0
/usr/lib64/libKSaneWidgets6.so.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksane/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/libksane/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/libksane/b9c8ec07abddb6bfbe08cb87aa8f68c2c2a1152f
/usr/share/package-licenses/libksane/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f libksane.lang
%defattr(-,root,root,-)

