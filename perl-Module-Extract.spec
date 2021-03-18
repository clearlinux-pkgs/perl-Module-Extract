#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Extract
Version  : 0.01
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Module-Extract-0.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Module-Extract-0.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-extract-perl/libmodule-extract-perl_0.01-2.debian.tar.xz
Summary  : Base class for working with Perl distributions
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-Module-Extract-license = %{version}-%{release}
Requires: perl-Module-Extract-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Archive::Extract)
BuildRequires : perl(Module::Install)

%description
NAME
Module::Extract - Base class for working with Perl distributions
SYNOPSIS
Creating a Module::Extract subclass.

%package dev
Summary: dev components for the perl-Module-Extract package.
Group: Development
Provides: perl-Module-Extract-devel = %{version}-%{release}
Requires: perl-Module-Extract = %{version}-%{release}

%description dev
dev components for the perl-Module-Extract package.


%package license
Summary: license components for the perl-Module-Extract package.
Group: Default

%description license
license components for the perl-Module-Extract package.


%package perl
Summary: perl components for the perl-Module-Extract package.
Group: Default
Requires: perl-Module-Extract = %{version}-%{release}

%description perl
perl components for the perl-Module-Extract package.


%prep
%setup -q -n Module-Extract-0.01
cd %{_builddir}
tar xf %{_sourcedir}/libmodule-extract-perl_0.01-2.debian.tar.xz
cd %{_builddir}/Module-Extract-0.01
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Module-Extract-0.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-Extract
cp %{_builddir}/Module-Extract-0.01/LICENSE %{buildroot}/usr/share/package-licenses/perl-Module-Extract/f11692fc652e231edd2a23a60c72d9be8a840e0c
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Module-Extract/08ecb5a8fbad7bec172ab81d182eccb00b4ec63a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Extract.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-Extract/08ecb5a8fbad7bec172ab81d182eccb00b4ec63a
/usr/share/package-licenses/perl-Module-Extract/f11692fc652e231edd2a23a60c72d9be8a840e0c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Module/Extract.pm
