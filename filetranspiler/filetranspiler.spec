Name: filetranspiler
Version: 1.1.0
Release: 1%{?dist}
Summary: Creates an update Ignition json file with additions from a fake root
Group: Development/Tools
License: Apache License 2.0
URL: https://github.com/ashcrow/filetranspiler
Source0: https://github.com/ashcrow/filetranspiler/archive/%{version}.zip

%global debug_package %{nil}

%description
Creates an update Ignition json file with additions from a fake root

%prep
%setup -q -n filetranspiler-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 filetranspile %{buildroot}%{_bindir}

%files
%{_bindir}/*

%changelog
* Fri Jan 3 2020 Eduardo Minguez <edu@redhat.com> - 1.1.0-1
- First version
