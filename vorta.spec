%global srcname vorta
%global debug_package %{nil}

Name:           %{srcname}
Version:        0.8.10
Release:        5%{?dist}
Summary:        A GUI for Borg Backup
License:        GPLv3
URL:            https://vorta.borgbase.com/
Source0:        https://github.com/borgbase/vorta/archive/v%{version}.tar.gz
Patch0:         prune.patch

Requires:       python3-appdirs
Requires:       python3-paramiko
Requires:       python3-peewee
Requires:       python3-psutil
Requires:       python3-qt5
Requires:       python3-secretstorage
Requires:       borgbackup

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python-rpm-macros

%description
Vorta is a backup client for macOS and Linux desktops. 
It integrates the mighty BorgBackup with your desktop environment 
to protect your data from disk failure, ransomware and theft

%prep

%autosetup -p1 -n %{srcname}-%{version} 

%build
%py3_build

%install
%py3_install
install -D %{_builddir}/%{srcname}-%{version}/build/lib/vorta/assets/icons/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.borgbase.Vorta.svg
install -D %{_builddir}/%{srcname}-%{version}/package/icon-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/com.borgbase.Vorta-symbolic.svg
install -D %{_builddir}/%{srcname}-%{version}/src/vorta/assets/metadata/com.borgbase.Vorta.desktop %{buildroot}%{_datadir}/applications/com.borgbase.Vorta.desktop


%files
#%doc RELEASE.md
#%license LICENSE
%{python3_sitelib}/*
%{_bindir}/vorta
%{_datadir}/*

%changelog
* Sun Mar 19 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 0.8.10-5
- setuptools back to build time dependencies

* Sun Mar 19 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 0.8.10-4
- Fix dependencies

* Mon Feb 20 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 0.8.10-3
- Bumpt to version 0.8.10
- Add prune patch fix

* Fri Nov 04 2022 Sergi Jimenez <tripledes@fedoraproject.org> - 0.8.8-1
- Bumpt to version 0.8.8

* Thu Aug 25 2022 Sergi Jimenez <tripledes@fedoraproject.org> - 0.8.7-2
- Bump version to 0.8.7
- Switch to noarch
- Cleanups

* Fri Feb 19 2021 Guilherme Cardoso <gjc@ua.pt> 0.7.3-1
- Improve build dependencies for OpenSuse buildroots
- Relax a little on distribution packages needed for building

* Sun Jan 31 2021 Guilherme Cardoso <gjc@ua.pt> 0.7.2-1
- Fix vorta icon.svg source path
- Add missing buildrequires: python3-pip and python3-setuptools_git

* Sat Jan 2 2021 Guilherme Cardoso <gjc@ua.pt> 0.7.1-1
- Initial release
