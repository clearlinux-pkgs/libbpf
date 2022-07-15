#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libbpf
Version  : 0.8.1
Release  : 12
URL      : https://github.com/libbpf/libbpf/archive/v0.8.1/libbpf-0.8.1.tar.gz
Source0  : https://github.com/libbpf/libbpf/archive/v0.8.1/libbpf-0.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libbpf-lib = %{version}-%{release}
Requires: libbpf-license = %{version}-%{release}
BuildRequires : elfutils-dev
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(zlib)

%description
This is a mirror of [bpf-next Linux source
tree](https://kernel.googlesource.com/pub/scm/linux/kernel/git/bpf/bpf-next)'s
`tools/lib/bpf` directory plus its supporting header files.

%package dev
Summary: dev components for the libbpf package.
Group: Development
Requires: libbpf-lib = %{version}-%{release}
Provides: libbpf-devel = %{version}-%{release}
Requires: libbpf = %{version}-%{release}

%description dev
dev components for the libbpf package.


%package lib
Summary: lib components for the libbpf package.
Group: Libraries
Requires: libbpf-license = %{version}-%{release}

%description lib
lib components for the libbpf package.


%package license
Summary: license components for the libbpf package.
Group: Default

%description license
license components for the libbpf package.


%prep
%setup -q -n libbpf-0.8.1
cd %{_builddir}/libbpf-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657893313
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
pushd src
make  %{?_smp_mflags}
popd


%install
export SOURCE_DATE_EPOCH=1657893313
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libbpf
cp %{_builddir}/libbpf-0.8.1/LICENSE.LGPL-2.1 %{buildroot}/usr/share/package-licenses/libbpf/91c66db733cf0ff2b3216ec4223b940daf6b26d4
pushd src
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/bpf/bpf.h
/usr/include/bpf/bpf_core_read.h
/usr/include/bpf/bpf_endian.h
/usr/include/bpf/bpf_helper_defs.h
/usr/include/bpf/bpf_helpers.h
/usr/include/bpf/bpf_tracing.h
/usr/include/bpf/btf.h
/usr/include/bpf/libbpf.h
/usr/include/bpf/libbpf_common.h
/usr/include/bpf/libbpf_legacy.h
/usr/include/bpf/libbpf_version.h
/usr/include/bpf/skel_internal.h
/usr/include/bpf/usdt.bpf.h
/usr/include/bpf/xsk.h
/usr/lib64/libbpf.so
/usr/lib64/pkgconfig/libbpf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbpf.so.0
/usr/lib64/libbpf.so.0.8.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libbpf/91c66db733cf0ff2b3216ec4223b940daf6b26d4
