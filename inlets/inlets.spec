Name:           inlets
Release:        1%{?dist}
Summary:        Expose your local endpoints to the Internet
Version:        2.7.3
License:        MIT
URL:            https://github.com/inlets/inlets
Source0:        https://github.com/inlets/inlets/releases/download/%{version}/inlets
Source1:        inlets.service
Source2:        default-inlets
ExclusiveArch:  x86_64

%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
Expose your local endpoints to the Internet

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -d %{buildroot}/etc/default
install -d %{buildroot}%{_unitdir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/inlets
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/inlets.service
install -p -m 0644 %{SOURCE2} %{buildroot}/etc/default/inlets

%files
%{_bindir}/inlets
%{_unitdir}/inlets.service
/etc/default/inlets

%post
%systemd_post inlets.service

%preun
%systemd_preun inlets.service

%postun
%systemd_postun inlets.service

%changelog
* Fri Jun 19 2020 Eduardo Minguez Perez <e.minguez@gmail.com> - 2.7.3-1
- Bump version to 2.7.3

* Thu Jan 2 2020 Eduardo Minguez Perez <e.minguez@gmail.com> - 2.6.3-1
- Initial package
