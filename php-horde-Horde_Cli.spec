# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Cli
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Command Line Interface API
Name:		php-horde-Horde_Cli
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	cd4ff47371d00ea814c34f5aedf42dd0
URL:		http://pear.horde.org/package/Horde_Cli/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Horde_Cli:: API for basic command-line functionality/checks

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Horde_Cli/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Cli.php
%{php_pear_dir}/Horde/Cli
%{php_pear_dir}/data/Horde_Cli
