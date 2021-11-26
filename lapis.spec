Name:           lapis
Version:        0.1
Release:        1%{?dist}
Summary:        A simple RPM build system

License:        MIT
URL:            https://gitlab.ultramarine-linux.org/lapis/lapis-client
Source0:        https://gitlab.ultramarine-linux.org/lapis/lapis-client/-/archive/main/lapis-client-main.tar.gz

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
Requires:       python3-setuptools
Requires:       python3-typer
Requires:       python3-requests

%description
Lapis is an RPM build system inspired by Copr.

%prep
%autosetup -n lapis-client-main

rm -rf lapiscli/__pycache__

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{python3_sitelib}
install lapis -m 755 %{buildroot}%{_bindir}/lapis
cp -r lapiscli/ %{buildroot}%{python3_sitelib}
%files
%doc README.md

%{_bindir}/lapis
%{python3_sitelib}/lapiscli/

%changelog
* Fri Nov 26 2021 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial release
