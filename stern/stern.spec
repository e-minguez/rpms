Name: stern
Version: 1.11.0
Release: 1%{?dist}
Summary: Multi pod and container log tailing for Kubernetes
Group: Development/Tools
License: Apache License 2.0
URL: https://github.com/wercker/stern
ExclusiveArch:  x86_64
Source0: https://github.com/wercker/stern/releases/download/%{version}/stern_linux_amd64

%description
Stern allows you to tail multiple pods on Kubernetes and multiple containers within the pod. Each result is color coded for quicker debugging.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/stern

%files
%{_bindir}/*

%changelog
* Fri Jan 3 2020 Eduardo Minguez <edu@redhat.com> - 1.11.0-1
- Bump version

* Fri Jun 21 2019 Eduardo Minguez <edu@redhat.com> - 1.10.0-1
- First version
