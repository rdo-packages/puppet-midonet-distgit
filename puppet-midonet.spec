%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppet-midonet

Name:           puppet-midonet
# Bumped epoch after repo movement from github.com/midonet to github.com/openstack
Epoch:          1
Version:        1.1.0
Release:        1%{?dist}
Summary:        Configure and install MidoNet components
License:        ASL 2.0

URL:            https://github.com/midonet/puppet-midonet

Source0:        https://github.com/openstack/%{upstream_name}/archive/%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-module-data
Requires:       puppet-inifile
Requires:       puppet-zookeeper
Requires:       puppet-cassandra
#Requires:       puppet-apt
Requires:       puppet-java
Requires:       puppet-tomcat
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Configure and install MidoNet components

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/midonet/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/midonet/



%files
%{_datadir}/openstack-puppet/modules/midonet/


%changelog
* Mon Feb 13 2017 Alfredo Moralejo <amoralej@redhat.com> 1:1.1.0-1
- Update to 1.1.0


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-midonet/commit/?id=9954ca784eb36935b51d5367d2d486d3caa03a07
