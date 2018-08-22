%global lastcommit 337028
%global lastcommitlong 337028595f0bc1a62cbcbba1dc1d162277dd7395

Name:      gnomeshell-extension-manage
Version:   2.4
Release:   20180822git%{lastcommit}
Summary:   Script to manage gnome shell extensions
Group:     Development/Tools
License:   Unknown
URL:       http://bernaerts.dyndns.org/linux/
BuildArch: noarch
Source0:  https://github.com/NicolasBernaerts/ubuntu-scripts/archive/%{lastcommitlong}.tar.gz

%description
Script to manage gnome shell extensions

%prep
%setup -n ubuntu-scripts-%{lastcommitlong}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 ubuntugnome/gnomeshell-extension-manage %{buildroot}%{_bindir}

%files
%{_bindir}/*

%changelog
* Wed Aug 22 2018 Eduardo Minguez <edu@redhat.com> - 2.4
- Bumped to proper script version

* Mon Jan 22 2018 Eduardo Minguez <edu@redhat.com> - 0.1-20180122
- Added "--version latest" support

* Wed Dec 27 2017 Eduardo Minguez <edu@redhat.com> - 0.1-20171226
- First version
