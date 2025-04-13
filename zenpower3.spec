%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     zenpower3
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Zenpower3 is a Linux kernel driver for reading temperature, voltage(SVI2), current(SVI2) and power(SVI2) for AMD Zen family CPUs
License:  GPLv2
URL:      https://github.com/AliEmreSenel/zenpower3

Source0:  https://raw.githubusercontent.com/AliEmreSenel/zenpower3/refs/heads/master/LICENSE

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Zenpower3 is a Linux kernel driver for reading temperature, voltage(SVI2), current(SVI2) and power(SVI2) for AMD Zen family CPUs, now with Zen 3 support! 

%build
install -D -m 0644 %{SOURCE0} %{buildroot}%{_datarootdir}/licenses/zenpower3/LICENSE

%files
%license LICENSE

%changelog
{{{ git_dir_changelog }}}
