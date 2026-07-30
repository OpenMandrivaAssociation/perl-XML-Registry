%define upstream_name 	 XML-Registry
%define upstream_version 0.02
Name:		perl-%{upstream_name}
Version:	0.02
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/E/EI/EISEN/XML-Registry-0.02.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} - module for loading and saving an XML registry.

%prep
%setup -q -n %{upstream_name}-%{version}

%build

CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README MANIFEST Changes  examples
%{perl_vendorlib}/XML
%{_mandir}/*/*

