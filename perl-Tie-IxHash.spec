#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Tie
%define		pnam	IxHash
Summary:	Tie::IxHash - ordered associative arrays for Perl
Summary(pl.UTF-8):	Tie::IxHash - uporządkowane tablice asocjacyjne dla Perla
Name:		perl-Tie-IxHash
Version:	1.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CH/CHORNY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8393f2ced231533c3e714abad582f291
URL:		http://search.cpan.org/dist/Tie-IxHash/
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

%description -l pl.UTF-8
Ten moduł Perla jest implementacją haszy, które zachowują kolejność, w
jakiej elementy były dodawane. Kolejność nie ulega zmianie kiedy
modyfikowane są wartości odpowiadające istniejącym kluczom w obiekcie
IxHash. Elementy mogą być także ustawiane w zadanej kolejności. Znane
operacje na tablicach perlowych mogą być także wykonywane na typie
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
%{_mandir}/man3/Tie::IxHash.3pm*
