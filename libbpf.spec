#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libbpf
Version  : 0.0.5
Release  : 1
URL      : https://github.com/libbpf/libbpf/archive/v0.0.5.tar.gz
Source0  : https://github.com/libbpf/libbpf/archive/v0.0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: libbpf-lib = %{version}-%{release}
BuildRequires : elfutils-dev
BuildRequires : pkgconfig(libelf)

%description
This is a mirror of [bpf-next linux tree](https://kernel.googlesource.com/pub/scm/linux/kernel/git/bpf/bpf-next)'s
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

%description lib
lib components for the libbpf package.


%prep
%setup -q -n libbpf-0.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571346126
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
pushd src
make  %{?_smp_mflags}
popd


%install
export SOURCE_DATE_EPOCH=1571346126
rm -rf %{buildroot}
pushd src
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/bpf/bpf.h
/usr/include/bpf/btf.h
/usr/include/bpf/libbpf.h
/usr/include/bpf/libbpf_util.h
/usr/include/bpf/xsk.h
/usr/lib64/libbpf.so
/usr/lib64/pkgconfig/libbpf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbpf.so.0
/usr/lib64/libbpf.so.0.0.5
