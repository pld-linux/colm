# TODO: install vim file
Summary:	The Colm Programming Language - COmputer Language Manipulation
Summary(pl.UTF-8):	Język programowania Colm do operacji na językach komputerowych
Name:		colm
Version:	0.12.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.complang.org/colm/%{name}-%{version}.tar.gz
# Source0-md5:	079a1ed44f71d48a349d954096c8e411
URL:		http://www.complang.org/colm/
BuildRequires:	libstdc++-devel
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/colm
%{_includedir}/colm
%{_libdir}/libcolmd.a
%{_libdir}/libcolmp.a
