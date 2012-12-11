%define upstream_name    Term-Size-Any
%define upstream_version 0.002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Retrieve terminal size
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Term::Size::Perl)
BuildRequires: perl-devel

BuildArch: noarch

%description
This is a unified interface to retrieve terminal size. It loads one module
of a list of known alternatives, each implementing some way to get the
desired terminal information. This loaded module will actually do the job
on behalf of 'Term::Size::Any'.

Thus, 'Term::Size::Any' depends on the availability of one of these
modules:

    Term::Size           (soon to be supported)
    Term::Size::Perl
    Term::Size::ReadKey  (soon to be supported)
    Term::Size::Win32

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.1.0-3mdv2011.0
+ Revision: 655221
- rebuild for updated spec-helper

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.1.0-2mdv2011.0
+ Revision: 505275
- rebuild using %%perl_convert_version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.001-1mdv2010.0
+ Revision: 376260
- adding missing buildrequires:
- import perl-Term-Size-Any


* Fri May 15 2009 cpan2dist 0.001-1mdv
- initial mdv release, generated with cpan2dist

