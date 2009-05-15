
%define realname   Term-Size-Any
%define version    0.001
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    No summary found
Source:     http://www.cpan.org/modules/by-module/Term/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Term::Size::Perl)


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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


