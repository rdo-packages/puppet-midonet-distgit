%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-midonet
%global commit bafa9e9bc3e683cd3ceb2650eb174cf707a2837e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-midonet
Version:        XXX
Release:        XXX
Summary:        Configure and install MidoNet components
License:        ASL 2.0

URL:            https://github.com/midonet/puppet-midonet

Source0:        https://github.com/midonet/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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

