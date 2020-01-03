%global lastcommit 9eb4ec
%global lastcommitlong 9eb4ec77141b1417d55f8accbfdc1258c9f03ed8

Name:      gnomeshell-extension-manage
Version:   2.4
Release:   20200103git%{lastcommit}
Summary:   Script to manage gnome shell extensions
Group:     Development/Tools
License:   Unknown
URL:       http://bernaerts.dyndns.org/linux/
BuildArch: noarch
Source0:  https://github.com/NicolasBernaerts/ubuntu-scripts/archive/%{lastcommitlong}.tar.gz

%description
Script to manage gnome shell extensions

%prep
%setup -q -n ubuntu-scripts-%{lastcommitlong}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 ubuntugnome/gnomeshell-extension-manage %{buildroot}%{_bindir}

%files
%{_bindir}/*

%changelog
* Fri Jan 3 2020 Eduardo Minguez <edu@redhat.com> - 2.4-20200103
- Bump version

* Wed Aug 22 2018 Eduardo Minguez <edu@redhat.com> - 2.4
- Bumped to proper script version

* Mon Jan 22 2018 Eduardo Minguez <edu@redhat.com> - 0.1-20180122
- Added "--version latest" support

* Wed Dec 27 2017 Eduardo Minguez <edu@redhat.com> - 0.1-20171226
- First version
