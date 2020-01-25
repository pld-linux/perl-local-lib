#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	local
%define	pnam	lib
Summary:	local::lib - create and use a local lib/ for perl modules with PERL5LIB
#Summary(pl.UTF-8):	
Name:		perl-local-lib
Version:	1.008004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AP/APEIRON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6244fa9d77e818594acbaf572aece326
URL:		http://search.cpan.org/dist/local-lib/
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
%{perl_vendorlib}/local
%{_mandir}/man3/*
