%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	IxHash
Summary:	Tie-IxHash perl module
Summary(pl):	Modu³ perla Tie-IxHash
Name:		perl-Tie-IxHash
Version:	1.21
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-IxHash perl module.

%description -l pl
Modu³ perla Tie-IxHash.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/IxHash.pm
%{_mandir}/man3/*
