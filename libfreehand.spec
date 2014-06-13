%define api 0.0
%define major 0
%define libname %mklibname freehand %{api} %{major}
%define devname %mklibname freehand -d

Name: libfreehand
Version: 0.0.0
Release: 3
Source0: http://dev-www.libreoffice.org/src/libfreehand-%{version}.tar.xz
Summary: Library providing ability to import Adobe/Macromedia drawings
URL: http://libfreehand.sf.net/
License: MPL 2.0
Group: System/Libraries
BuildRequires: doxygen
BuildRequires: pkgconfig(libwpd-0.9)
BuildRequires: pkgconfig(libwpg-0.2)
BuildRequires: pkgconfig(zlib)
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
%setup -q -n %{name}-%{version}
aclocal
automake -a
autoheader
autoconf
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_docdir}/%{name}