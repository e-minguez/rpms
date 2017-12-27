%global gist 800baff655380d619156
%global commit 5078ca3fd102684199427e3957aed6406c833238

Name:      discover-session-dbus-address
Version:   0.1
Release:   20171226
Summary:   Script to export dbus session
Group:     Development/Tools
License:   Unknown
URL:       http://askubuntu.com/questions/457016/how-to-change-gsettings-via-remote-shell
BuildArch: noarch
Source0:  https://gist.github.com/paalfe/%{gist}/archive/%{commit}.zip

%description
Script to export dbus session

%prep
%setup -n %{gist}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 discover_session_bus_address.sh %{buildroot}%{_bindir}/discover-session-dbus-address

%files
%{_bindir}/*

%changelog
* Wed Dec 27 2017 Eduardo Minguez <edu@redhat.com> - 0.1-20171226
- First version
