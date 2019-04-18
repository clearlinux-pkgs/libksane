#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libksane
Version  : 19.04.0
Release  : 4
URL      : https://download.kde.org/stable/applications/19.04.0/src/libksane-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/libksane-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/libksane-19.04.0.tar.xz.sig
Summary  : An image scanning library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: libksane-data = %{version}-%{release}
Requires: libksane-lib = %{version}-%{release}
Requires: libksane-license = %{version}-%{release}
Requires: libksane-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev
BuildRequires : sane-backends-dev

%description
# KSane
## Introduction
SANE Library interface for KDE
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
%setup -q -n libksane-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555624899
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555624899
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksane
cp COPYING %{buildroot}/usr/share/package-licenses/libksane/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libksane/COPYING-CMAKE-SCRIPTS
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libksane/COPYING.LIB
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
/usr/lib64/libKF5Sane.so.5
/usr/lib64/libKF5Sane.so.5.55.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksane/COPYING
/usr/share/package-licenses/libksane/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/libksane/COPYING.LIB

%files locales -f libksane.lang
%defattr(-,root,root,-)

