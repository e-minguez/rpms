Name: operator-sdk
Version: 0.13.0
Release: 1%{?dist}
Summary: SDK for building Kubernetes applications. Provides high level APIs, useful abstractions, and project scaffolding.
Group: Development/Tools
License: Apache License 2.0
URL: https://github.com/operator-framework/operator-sdk
ExclusiveArch: x86_64
Source0: https://github.com/operator-framework/operator-sdk/releases/download/v%{version}/operator-sdk-v%{version}-x86_64-linux-gnu

%description
The Operator SDK is a framework that uses the controller-runtime library to make writing operators easier by providing: High level APIs and abstractions to write the operational logic more intuitively, Tools for scaffolding and code generation to bootstrap a new project fast & Extensions to cover common operator use cases

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/operator-sdk

%files
%{_bindir}/*

%changelog
* Thu Jan 2 2020 Eduardo Minguez <edu@redhat.com> - 0.13.0-1
- Bump version to 0.13.0

* Fri Jun 21 2019 Eduardo Minguez <edu@redhat.com> - 0.8.1-1
- First version
