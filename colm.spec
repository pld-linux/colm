Summary:	The Colm Programming Language - COmputer Language Manipulation
Summary(pl.UTF-8):	Język programowania Colm do operacji na językach komputerowych
Name:		colm
Version:	0.14.7
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://www.colm.net/files/colm/%{name}-%{version}.tar.gz
# Source0-md5:	073b11234fe64a281874b4466c0c25ee
URL:		http://www.colm.net/
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Colm (COmputer Language Manipulation) is a programming language
designed for the analysis and transformation of computer languages.
Colm is influenced primarily by TXL (<http://www.txl.ca/>). It is in
the family of program transformation languages.

%description -l pl.UTF-8
Colm (COmputer Language Manipulation - operacje na języku
komputerowym) to język programowania zaprojektowany do analizy i
przekształceń języków komputerowych. Colm jest zainspirowany głównie
przez TXL (<http://www.txl.ca/>). Jest to rodzina języków
transformacji programów.

%package devel
Summary:	Header files for COLM libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek COLM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for COLM libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek COLM.

%package static
Summary:	Static COLM libraries
Summary(pl.UTF-8):	Statyczne biblioteki COLM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static COLM libraries.

%description static -l pl.UTF-8
Statyczne biblioteki COLM.

%package doc
Summary:	Documentation for COLM
Summary(pl.UTF-8):	Dokumentacja do pakietu COLM
Group:		Documentation
BuildArch:	noarch

%description doc
Documentation for COLM.

%description doc -l pl.UTF-8
Dokumentacja do pakietu COLM.

%package -n vim-syntax-colm
Summary:	Vim syntax file for COLM
Summary(pl.UTF-8):	Plik składni Vima dla pakietu COLM
Group:		Documentation
BuildArch:	noarch

%description -n vim-syntax-colm
Vim syntax file for COLM.

%description -n vim-syntax-colm -l pl.UTF-8
Plik składni Vima dla pakietu COLM.

%prep
%setup -q

%build
%configure \
	--datadir=%{_datadir}/colm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependensies (beside libstdc++)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
%{__mv} $RPM_BUILD_ROOT%{_docdir}/colm/colm.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/colm
%attr(755,root,root) %{_bindir}/colm-wrap
%attr(755,root,root) %{_libdir}/libcolm-%{version}.so
%attr(755,root,root) %{_libdir}/libfsm-%{version}.so
%{_datadir}/colm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolm.so
%attr(755,root,root) %{_libdir}/libfsm.so
%{_includedir}/aapl
%{_includedir}/colm
%{_includedir}/libfsm

%files static
%defattr(644,root,root,755)
%{_libdir}/libcolm.a
%{_libdir}/libfsm.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/colm

%files -n vim-syntax-colm
%defattr(644,root,root,755)
%{_datadir}/vim/vimfiles/syntax/colm.vim
