%define		modname bookmarks
Summary:	Drupal Bookmarks Module
Summary(pl.UTF-8):   Moduł zakładek dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.4
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	d67215435713a1b79ade414a4528ae5e
URL:		http://drupal.org/project/bookmarks
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules
%define		_htdocs		%{_drupaldir}/htdocs
%define		_podir		%{_drupaldir}/po/%{modname}
%define		_htmlmoddir	%{_htdocs}/modules/%{modname}

%description
Gives users with the 'access bookmark' permission their own private
bookmark block, allowing them to add any URL to the list. There is
also a quicklink feature that makes it a breeze to add the currently
viewed page to your site.

%description -l pl.UTF-8
Ten moduł daje użytkownikom z uprawnieniem "dostęp do zakładek" ich
własny blok zakładek, pozwalający im dodawać dowolne URL-e do listy.
Jest także właściwość "szybkich odnośników" umożliwiająca szybkie
dodanie aktualnie oglądaniej strony do własnego serwisu.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_moddir},%{_podir},%{_htmlmoddir}}

install *.module $RPM_BUILD_ROOT%{_moddir}
cp -a po/*.po $RPM_BUILD_ROOT%{_podir}
cp -a *.gif $RPM_BUILD_ROOT%{_htmlmoddir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
If you want to use localization, then you need to upload .po files
from %{_podir} via drupal locatization admin.

To create Bookmarks MySQL database tables import:
zcat %{_docdir}/%{name}-%{version}/%{modname}.mysql.gz | mysql drupal

EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt bookmarks.mysql
%{_moddir}/*.module
%{_podir}
%{_htmlmoddir}
