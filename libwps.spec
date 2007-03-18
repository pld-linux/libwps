Summary:	A library for importing Works documents
Name:		libwps
Version:	0.1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libwps/%{name}-%{version}.tar.bz2
# Source0-md5:	996ea73e1a2c07e4074d227a43c00b2e
URL:		http://libwps.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwps is a Microsoft Works file format import filter based on top of
the libwpd (which is already used in three word processors).
Currently, libwps is a new project, but it imports all Works formats
since about 1995 with some success.

%package devel
Summary:	Header files for libwps library
Summary(pl):	Pliki nag³ówkowe biblioteki libwps
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libwps library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libwps.

%package static
Summary:	Static libwps library
Summary(pl):	Statyczna biblioteka libwps
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwps library.

%description static -l pl
Statyczna biblioteka libwps.

%package tools
Summary:	Tools to transform Works Documents into other formats
Summary(pl):	Narz¿dzia do przekszta¿cania dokumentów WordPerfecta na inne formaty
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Works Documents (WPS) into other formats. Currently
supported: html, raw, text.

%prep
%setup -q

%build
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS HACKING  README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/doxygen/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libwps*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wps2html
%attr(755,root,root) %{_bindir}/wps2raw
%attr(755,root,root) %{_bindir}/wps2text
