Name: packer.io
Version: 1.4.1
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
* Mon May 27 2019 David Sastre <d.sastre.medina@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Mon May 13 2019 David Sastre <d.sastre.medina@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Wed Mar 27 2019 David Sastre <d.sastre.medina@gmail.com> - 1.3.5-1
- Update to 1.3.5

* Thu Feb 21 2019 David Sastre <d.sastre.medina@gmail.com> - 1.3.4-1
- Update to 1.3.4

* Mon Jan 08 2019 David Sastre <d.sastre.medina@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Tue Nov 06 2018 Sergi Jimenez <tripledes@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Mon Apr 02 2018 Eduardo Minguez <edu@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Tue Dec 19 2017 Eduardo Minguez <edu@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Thu May 05 2016 Josef Strzibny <strzibny@strzibny.name> - 0.10.0-1
- Update to 0.10.0

* Tue Oct 27 2015 Josef Stribny <jstribny@redhat.com> - 0.8.6-1
- Initial package
