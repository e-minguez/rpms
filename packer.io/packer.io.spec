Name: packer.io
Version: 1.1.3
Release: 1%{?dist}
Summary: Create machine and container images for multiple platforms
Group: Development/Tools
License: MPLv2.0
URL: https://www.packer.io/

Source0: https://releases.hashicorp.com/packer/%{version}/packer_%{version}_linux_amd64.zip

%description
Packer is a tool for creating machine and container images for
multiple platforms from a single source configuration.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
unzip -o %{SOURCE0} -d %{buildroot}%{_bindir}

# Rename to packerio since packer conflicts with Fedora
pushd %{buildroot}%{_bindir}
  mv packer packerio
popd

%files
%{_bindir}/*

%changelog
* Tue Dec 19 2017 Eduardo Minguez <edu@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Thu May 05 2016 Josef Strzibny <strzibny@strzibny.name> - 0.10.0-1
- Update to 0.10.0

* Tue Oct 27 2015 Josef Stribny <jstribny@redhat.com> - 0.8.6-1
- Initial package

