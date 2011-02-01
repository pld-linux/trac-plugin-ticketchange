%define		trac_ver	0.12
%define		plugin		ticketchange
Summary:	Change ticket comments in Trac
Name:		trac-plugin-%{plugin}
Version:	0.0.4
Release:	7
License:	BSD
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/ticketchangeplugin?old_path=/&format=zip#/%{plugin}-%{version}.zip
# Source0-md5:	f59788ca5f34354c0126f05d890862a7
URL:		http://trac-hacks.org/wiki/TicketChangePlugin
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.595
Requires:	trac >= %{trac_ver}
Requires:	trac-plugin-ticketdelete
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a web interface to change ticket comments in Trac.

%prep
%setup -qc
mv %{plugin}plugin/0.11/* .

%build
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner -o -e %{name} <<-'EOF'
Don't forget to enable ticketdelete in conf/trac.ini:

[components]
ticketchange.* = enabled
EOF
#'vim

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/ticketchange
%{py_sitescriptdir}/TracTicketChange-*.egg-info
