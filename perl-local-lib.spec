#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	local
%define	pnam	lib
Summary:	local::lib - create and use a local lib/ for perl modules with PERL5LIB
#Summary(pl.UTF-8):	
Name:		perl-local-lib
Version:	2.000029
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/H/HA/HAARG/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e35cd5075574b6cd2057e2e15002056e
URL:		https://metacpan.org/dist/local-lib
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
local::lib allows for the bootstrapping and usage of a directory
containing Perl modules outside of Perl's @INC. This makes it easier
to ship an application with an app-specific copy of a Perl module,
or collection of modules. Useful in cases like when an upstream
maintainer hasn't applied a patch to a module of theirs that you need
for your application.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/lib
%dir %{perl_vendorlib}/POD2/DE
%dir %{perl_vendorlib}/POD2/PT_BR
%{perl_vendorlib}/local
%{perl_vendorlib}/lib/core
%{perl_vendorlib}/POD2/DE/local
%{perl_vendorlib}/POD2/PT_BR/local
%{_mandir}/man3/*
