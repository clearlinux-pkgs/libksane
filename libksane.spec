#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libksane
Version  : 22.12.3
Release  : 49
URL      : https://download.kde.org/stable/release-service/22.12.3/src/libksane-22.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.3/src/libksane-22.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.3/src/libksane-22.12.3.tar.xz.sig
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
BuildRequires : ki18n-dev
BuildRequires : ksanecore-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwallet-dev
BuildRequires : kwidgetsaddons-dev
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
%setup -q -n libksane-22.12.3
cd %{_builddir}/libksane-22.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677776697
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1677776697
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksane
cp %{_builddir}/libksane-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libksane/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libksane-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/libksane/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/libksane-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libksane/b9c8ec07abddb6bfbe08cb87aa8f68c2c2a1152f || :
cp %{_builddir}/libksane-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksane/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libksane-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksane/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build
%make_install
popd
%find_lang libksane

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/16x16/actions/black-white.png
/usr/share/icons/hicolor/16x16/actions/color.png
/usr/share/icons/hicolor/16x16/actions/gray-scale.png

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KSane/KSaneWidget
/usr/include/KF5/KSane/ksane_export.h
/usr/include/KF5/KSane/ksanewidget.h
/usr/include/KF5/ksane_version.h
/usr/lib64/cmake/KF5Sane/KF5SaneConfig.cmake
/usr/lib64/cmake/KF5Sane/KF5SaneConfigVersion.cmake
/usr/lib64/cmake/KF5Sane/KF5SaneTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Sane/KF5SaneTargets.cmake
/usr/lib64/libKF5Sane.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Sane.so.22.12.3
/usr/lib64/libKF5Sane.so.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksane/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/libksane/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/libksane/b9c8ec07abddb6bfbe08cb87aa8f68c2c2a1152f
/usr/share/package-licenses/libksane/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f libksane.lang
%defattr(-,root,root,-)

