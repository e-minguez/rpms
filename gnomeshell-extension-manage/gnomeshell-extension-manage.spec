%global lastcommit 549b29
%global lastcommitlong 549b29327c05e00caa0c1c4d6d7dbf58d6f93da0

Name:      gnomeshell-extension-manage
Version:   0.1
Release:   20180122git%{lastcommit}
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
* Mon Jan 22 2018 Eduardo Minguez <edu@redhat.com> - 0.1-20180122
- Added "--version latest" support

* Wed Dec 27 2017 Eduardo Minguez <edu@redhat.com> - 0.1-20171226
- First version
