Name: ct
Version: 0.9.0
Release: 1%{?dist}
Summary: The Config Transpiler ("ct" for short) is the utility responsible for transforming a human-friendly Container Linux Config into a JSON file.
Group: Development/Tools
License: Apache License 2.0
URL: https://github.com/coreos/container-linux-config-transpiler
ExclusiveArch:  x86_64
Source0: https://github.com/coreos/container-linux-config-transpiler/releases/download/v%{version}/ct-v%{version}-%{_arch}-unknown-linux-gnu

%description
The Config Transpiler ("ct" for short) is the utility responsible for transforming a human-friendly Container Linux Config into a JSON file. This resulting file can be provided to a Container Linux machine when it first boots to provision the machine.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/ct

%files
%{_bindir}/*

%changelog
* Thu Jan 10 2019 Eduardo Minguez <edu@redhat.com> - 0.9.0-1
- First version
