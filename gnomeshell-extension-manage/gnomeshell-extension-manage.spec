%global lastcommit d14e5d
%global lastcommitlong d14e5d8e267c8e4a157178556ae2d6563fc015c3

Name:      gnomeshell-extension-manage
Version:   0.1
Release:   20171226git%{lastcommit}
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
* Wed Dec 27 2017 Eduardo Minguez <edu@redhat.com> - 0.1-20171226
- First version
