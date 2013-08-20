Summary:	Computer-aided translation tool for KDE
Name:		lokalize
Version:	4.11.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(hunspell)
Requires:	kdesdk-strigi-analyzers
Requires:	qt4-database-plugin-sqlite
# Needed by some lokalize scripts (mga #10583, bko #181145)
Requires:	kross-interpreters-python
Suggests:	python-translate

%description
Lokalize is a computer-aided translation system that focuses on productivity
and performance. Translator does only creative work (of delivering message
in his/her mother language in laconic and easy to understand form). Lokalize
implies paragraph-by-paragraph translation approach (when translating
documentation) and message-by-message approach (when translating GUI).

%files
%{_kde_bindir}/lokalize
%{_kde_applicationsdir}/lokalize.desktop
%{_kde_appsdir}/lokalize
%{_kde_datadir}/config.kcfg/lokalize.kcfg
%{_kde_iconsdir}/*/*/apps/lokalize.*
%{_kde_docdir}/*/*/lokalize

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
