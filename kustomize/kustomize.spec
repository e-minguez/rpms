Name: kustomize
Version: 3.5.3
Release: 1%{?dist}
Summary: Customization of kubernetes YAML configurations 
Group: Development/Tools
License: Apache License 2.0
URL: https://github.com/kubernetes-sigs/kustomize
ExclusiveArch: x86_64
Source0: https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv%{version}/kustomize_v%{version}_linux_amd64.tar.gz

%global debug_package %{nil}

%description
kustomize lets you customize raw, template-free YAML files for multiple purposes, leaving the original YAML untouched and usable as is.

%prep
%setup -c

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 kustomize %{buildroot}%{_bindir}

%files
%{_bindir}/*

%changelog
* Thu Jan 9 2020 Eduardo Minguez <edu@redhat.com> - 3.5.3-1
- First version
