%define upstream_name    ExtUtils-Command
%define upstream_version 1.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Utilities to replace common UNIX commands in Makefiles etc
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-Command-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildArch:	noarch

%description
Thin wrapper around ExtUtils::Command. See the ExtUtils::Command manpage
for a description of available commands.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.170.0-2mdv2011.0
+ Revision: 657438
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1
+ Revision: 643379
- update to new version 1.17

* Thu Jul 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 396580
- import perl-ExtUtils-Command


* Thu Jul 16 2009 cpan2dist 1.16-1mdv
- initial mdv release, generated with cpan2dist

