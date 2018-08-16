# Package needs to stay arch specific (due to nagios plugins location), but
# there's nothing to extract debuginfo from
%global debug_package %{nil}

%define nagios_plugins_dir %{_libdir}/nagios/plugins

Name:       nagios-plugins-fts
Version:    3.5.0
Release:    2%{?dist}
Summary:    Nagios probes to be run remotely against FTS3 machines
License:    ASL 2.0
Group:      Applications/Internet
URL:        https://svnweb.cern.ch/trac/fts3
# The source of this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
Source0:   https://grid-deployment.web.cern.ch/grid-deployment/dms/fts3/tar/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires:  cmake

Requires:   nagios%{?_isa}
Requires:   python%{?_isa}
Requires:   python-pycurl%{?_isa}

%description
This package provides the nagios probes for FTS3. Usually they are installed
in the nagios host, and they will contact the remote services running in the
FTS3 machines.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake . -DCMAKE_INSTALL_PREFIX=/

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/nagios/objects/fts3-template.cfg
%{nagios_plugins_dir}/fts
%doc LICENSE README.md

%changelog
* Thu Aug 16 2018 Andrea Manzi <amanzi@cern.ch> - 3.5.0-2
- fixes for new nagios systax and use of REST instead of SOAP interface

* Tue Nov 12 2013 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 3.2.0-1
- Initial build

