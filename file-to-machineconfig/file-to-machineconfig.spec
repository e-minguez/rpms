Name: file-to-machineconfig
Version: 0.0.4
Release: 1%{?dist}
Summary: Simple tool to convert files to MachineConfig
Group: Development/Tools
License: Apache License 2.0
URL: https://github.com/e-minguez/file-to-machineconfig
ExclusiveArch: x86_64
Source0: https://github.com/e-minguez/file-to-machineconfig/releases/download/%{version}/file-to-machineconfig-linux-amd64

%description
Simple tool to convert files to MachineConfig objects to be used with the machine-config-operator in Kubernetes/OpenShift

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/file-to-machineconfig

%files
%{_bindir}/*

%changelog
* Fri Jan 3 2020 Eduardo Minguez <edu@redhat.com> - 0.0.4-1
- First version
