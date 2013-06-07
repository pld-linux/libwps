Summary:	A library for importing MS Works documents
Summary(pl.UTF-8):	Biblioteka importu dokumentów MS Works
Name:		libwps
Version:	0.2.9
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwps/%{name}-%{version}.tar.xz
# Source0-md5:	95ae3908111b1ab8a3e3caed1807b5be
URL:		http://libwps.sourceforge.net/
BuildRequires:	autoconf >= 0.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libwpd >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwps is a Microsoft Works file format import filter based on top of
the libwpd (which is already used in three word processors).
Currently, libwps is a new project, but it imports all Works formats
since about 1995 with some success.

%description -l pl.UTF-8
libwps jest filtrem importu plików w formacie MS Works, bazującym na
bibliotece libwpd używanej już w trzech procesorach tekstu. Obecnie
libwps jest nowym projektem, jednakże od ok. roku 1995 jest z pewnym
sukcesem używany do importowania wszystkich formatów MS Works.

%package devel
Summary:	Header files for libwps library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwps
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libwpd-devel >= 0.9

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
%doc CREDITS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_libdir}/libwps-0.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwps-0.2.so.2

%files devel
%defattr(644,root,root,755)
%doc docs/doxygen/html
%attr(755,root,root) %{_libdir}/libwps-0.2.so
%{_includedir}/libwps-0.2
%{_pkgconfigdir}/libwps-0.2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwps-0.2.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wps2html
%attr(755,root,root) %{_bindir}/wps2raw
%attr(755,root,root) %{_bindir}/wps2text
