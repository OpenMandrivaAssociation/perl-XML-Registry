%define upstream_name 	 XML-Registry
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} - module for loading and saving an XML registry.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 408246
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-10mdv2009.0
+ Revision: 242268
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-8mdv2008.0
+ Revision: 23494
- rebuild


* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-7mdk
- Fix SPEC Using perl Policies
	- Source URL
- use mkrel

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.02-6mdk
- rebuid
- usr %%makeinstall_std
- own dir

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-5mdk
- rebuild for new auto{prov,req}

