%define _rpmfilename %%{NAME}.%%{ARCH}.rpm

Name:           fedy-release
BuildArch:      noarch
Version:        5.0.0
Release:        0
License:        GPL-3
Group:          System Environment/Base
Summary:        Fedy Repository Configuration

URL:            https://www.folkswithhats.org
Vendor:         Fedy
Packager:       <https://www.folkswithhats.org/>

Obsoletes: folkswithhats-release

Requires:       system-release >= %{version}

%description
Folks With Hats repositories contain distributable software for Fedora.

%install
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/yum.repos.d
cat << EOF >>%{buildroot}%{_sysconfdir}/yum.repos.d/fedy.repo
[fedy]
name=Fedy Repository
baseurl=https://dl.folkswithhats.org/fedora/\$releasever/
enabled=1
metadata_expire=1d
gpgcheck=0
EOF


%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/fedy.repo

%changelog
* Sun Apr 22 2018 Benjamin Denhartog <ben@sudoforge.com> - 5.0.0
- Rename package {folkswithhats=>fedy}-release
- Rename repofile {folkswithhats=>fedy}.repo
* Thu Nov 16 2017 Benjamin Denhartog <ben@sudoforge.com> - 4.0.0
- Force static package name to simplify client installation
* Wed Jul 19 2017 Benjamin Denhartog <ben@sudoforge.com> - 3.0.0
- Update base repository URI to https://dl.folkswithhats.org/fedora
- change repository name from "Repository for Fedy" to "Folks With Hats Repository"
* Thu Mar 16 2017 Benjamin Denhartog <ben@sudoforge.com> - 2.0.0
- Update repository URL
- Remove skip_if_unavailable configuration setting, changing behavior to False
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

