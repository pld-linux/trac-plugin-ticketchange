%define		trac_ver	0.12
Summary:	Change ticket comments in Trac
Name:		trac-plugin-ticketchange
Version:	0.0.4
Release:	6
License:	BSD
Group:		Applications/WWW
# svn export http://trac-hacks.org/svn/ticketchangeplugin/0.11 ticketchangeplugin
Source0:	ticketchangeplugin.tar.bz2
# Source0-md5:	2ba34c00b96da755230a9c7916fe575e
URL:		http://trac-hacks.org/wiki/TicketChangePlugin
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	trac = %{trac_ver}
Requires:	trac-plugin-ticketdelete
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a web interface to change ticket comments in Trac.

%prep
%setup -q -n ticketchangeplugin

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
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	Don't forget to enable ticketdelete in conf/trac.ini:

	[components]
	ticketchange.* = enabled
EOF
#' - vim
fi

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/ticketchange
%{py_sitescriptdir}/TracTicketChange-*.egg-info
