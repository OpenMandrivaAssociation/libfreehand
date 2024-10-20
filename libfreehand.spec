%define api 0.1
%define major 1
%define libname %mklibname freehand %{api} %{major}
%define devname %mklibname freehand -d

Name: libfreehand
Version: 0.1.2
Release: 5
Source0: http://dev-www.libreoffice.org/src/%{name}/libfreehand-%{version}.tar.bz2
Summary: Library providing ability to import Adobe/Macromedia drawings
URL: https://libfreehand.sf.net/
License: MPL 2.0
Group: System/Libraries
Patch0: 0001-Add-missing-semicolon-to-fix-build-with-icu-65.1.patch
BuildRequires: doxygen
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(cppunit)
BuildRequires: boost-devel
BuildRequires: gperf

%description
Libfreehand is library providing ability to interpret and import
Adobe/Macromedia drawings into various applications.

You can find it being used in libreoffice.

%package -n %{libname}
Summary: Library providing ability to import Adobe/Macromedia drawings
Group: System/Libraries

%description -n %{libname}
Libfreehand is library providing ability to interpret and import
Adobe/Macromedia drawings into various applications.

You can find it being used in libreoffice.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
aclocal
automake -a
autoheader
autoconf
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%configure --disable-werror

%build
%make_build

%install
%make_install

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_docdir}/%{name}
