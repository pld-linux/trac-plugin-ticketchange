%define		trac_ver	0.10
Summary:	Ticket Comments Change Plugin
Name:		trac-plugin-ticketchange
Version:	0
Release:	2
License:	BSD-like
Group:		Applications/WWW
# Source0Download:	http://trac-hacks.org/changeset/latest/ticketchangeplugin?old_path=/&filename=ticketchangeplugin&format=zip
Source0:	ticketchangeplugin.zip
# Source0-md5:	7c21c57730434992bf0e7aca47fdaa0c
URL:		http://trac-hacks.org/wiki/TicketChangePlugin
BuildRequires:	python-devel
Requires:	trac >= %{trac_ver}
Requires:	trac-plugin-ticketdelete
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ticket Comments Change Plugin.

%prep
%setup -q -n ticketchangeplugin

%build
cd %{trac_ver}
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd %{trac_ver}
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
