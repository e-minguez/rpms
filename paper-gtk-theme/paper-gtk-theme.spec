#
# Spec file for package paper-gtk-theme
#
# Copyright (c) 2016 Sam Hewitt
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
%global lastcommit 770aba4
%global lastcommitlong 770aba45a6441f9af4d02e04c0acc237533d341f

Name:           paper-gtk-theme
Version:        2.1.0
Release:        20171226git%{lastcommit}
License:        GPL-3.0+
Summary:        Paper Theme Suite
Url:            https://snwh.org/paper
Group:          System/GUI/Other
Source0:        https://github.com/snwh/%{name}/archive/%{lastcommitlong}.tar.gz
BuildRequires:  automake
BuildArch:      noarch
Requires:       gtk2-engines

%description
Paper is a modern desktop theme suite. Its design is mostly flat with a minimal use of shadows for depth.

%prep
%setup -qn %{name}-%{lastcommit}

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Paper/ $RPM_BUILD_ROOT%{_datadir}/themes/

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%{_datadir}/themes/Paper

%changelog
* Tue Dec 26 2017 Eduardo Minguez <edu@redhat.com> - 2.1.0-20171226git770aba4
- First version
