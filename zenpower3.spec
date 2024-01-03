%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     zenpower3
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Zenpower3 is a Linux kernel driver for reading temperature, voltage(SVI2), current(SVI2) and power(SVI2) for AMD Zen family CPUs
License:  GPLv2
URL:      https://git.exozy.me/a/zenpower3

Source0:  https://git.exozy.me/a/zenpower3/raw/branch/master/LICENSE

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Wine synchronization primitive driver

%build
install -D -m 0644 %{SOURCE0} %{buildroot}%{_datarootdir}/licenses/zenpower3/LICENSE

%files
%license LICENSE

%changelog
{{{ git_dir_changelog }}}
