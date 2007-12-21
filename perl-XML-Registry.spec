%define module 	XML-Registry
%define version 0.02
%define release %mkrel 8

Summary:	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
Url:		http://search.cpan.org/dist/%{module}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
%{module} - module for loading and saving an XML registry.

%prep
%setup -q -n %{module}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST Changes  examples
%{perl_vendorlib}/XML
%{_mandir}/*/*

