%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	IxHash
Summary:	Tie::IxHash - ordered associative arrays for Perl
Summary(pl):	Tie::IxHash - uporz±dkowane tablica asocjacyjne dla Perla
Name:		perl-Tie-IxHash
Version:	1.21
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module implements Perl hashes that preserve the order in
which the hash elements were added. The order is not affected when
values corresponding to existing keys in the IxHash are changed. The
elements can also be set to any arbitrary supplied order. The familiar
perl array operations can also be performed on the IxHash.

%description -l pl
Ten modu³ Perla jest implementacj± haszy, które zachowuj± kolejno¶æ, w
jakiej elementy by³y dodawane. Kolejno¶æ nie ulega zmianie kiedy
modyfikowane s± warto¶ci odpowiadaj±ce istniej±cym kluczom w obiekcie
IxHash. Elementy mog± byæ tak¿e ustawiane w zadanej kolejno¶ci. Znane
operacje na tablicach perlowych mog± byæ tak¿e wykonywane na typie
IxHash.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Tie/IxHash.pm
%{_mandir}/man3/*
