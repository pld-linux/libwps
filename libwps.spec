Summary:	A library for importing MS Works documents
Summary(pl.UTF-8):	Biblioteka importu dokumentów MS Works
Name:		libwps
Version:	0.4.9
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwps/%{name}-%{version}.tar.xz
# Source0-md5:	b49670696446f4e11cafa49ec566d54c
Patch0:		%{name}-include.patch
URL:		http://libwps.sourceforge.net/
BuildRequires:	autoconf >= 0.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	doxygen
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwps is a Microsoft Works file format import filter based on top of
the librevenge (which is already used in three word processors).
Currently, libwps can import all word processing Microsoft Works
formats since about 1995 with some success and some spreadsheet
Microsoft Works.

%description -l pl.UTF-8
libwps jest filtrem importu plików w formacie Microsoft Works,
opartymm na bibliotece librevenge (używanej już w trzech procesorach
tekstu). Obecnie libwps potrafi importować wszystkie formaty tekstowe
Microsoft Works od około 1995 roku oraz niektóre arkusze kalkulacyjne
Microsoft Works.

%package devel
Summary:	Header files for libwps library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwps
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for libwps library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwps.

%package static
Summary:	Static libwps library
Summary(pl.UTF-8):	Statyczna biblioteka libwps
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwps library.

%description static -l pl.UTF-8
Statyczna biblioteka libwps.

%package apidocs
Summary:	API documentation for libwps library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libwps
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libwps library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libwps.

%package tools
Summary:	Tools to transform Works Documents into other formats
Summary(pl.UTF-8):	Narzędzia przekształcające dokumenty MS Works na inne formaty
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Works Documents (WPS) into other formats. Currently
supported: html, raw, text.

%description tools -l pl.UTF-8
Narzędzia przekształcające dokumenty MS Works (WPS) do innych
formatów. Obecnie obsługiwane: html, raw, tekst.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# packaged as %doc in -devel
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libwps-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwps-0.4.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwps-0.4.so
%{_includedir}/libwps-0.4
%{_pkgconfigdir}/libwps-0.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwps-0.4.a

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wks2csv
%attr(755,root,root) %{_bindir}/wks2raw
%attr(755,root,root) %{_bindir}/wks2text
%attr(755,root,root) %{_bindir}/wps2html
%attr(755,root,root) %{_bindir}/wps2raw
%attr(755,root,root) %{_bindir}/wps2text
