#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	IxHash
Summary:	Tie::IxHash - ordered associative arrays for Perl
Summary(pl):	Tie::IxHash - uporz�dkowane tablica asocjacyjne dla Perla
Name:		perl-Tie-IxHash
Version:	1.21
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	567ddc13081596b52cfe3d82218cb264
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module implements Perl hashes that preserve the order in
which the hash elements were added. The order is not affected when
values corresponding to existing keys in the IxHash are changed. The
elements can also be set to any arbitrary supplied order. The familiar
perl array operations can also be performed on the IxHash.

%description -l pl
Ten modu� Perla jest implementacj� haszy, kt�re zachowuj� kolejno��, w
jakiej elementy by�y dodawane. Kolejno�� nie ulega zmianie kiedy
modyfikowane s� warto�ci odpowiadaj�ce istniej�cym kluczom w obiekcie
IxHash. Elementy mog� by� tak�e ustawiane w zadanej kolejno�ci. Znane
operacje na tablicach perlowych mog� by� tak�e wykonywane na typie
IxHash.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/IxHash.pm
%{_mandir}/man3/*
