Summary:	Computer-aided translation tool for KDE
Name:		lokalize
Version:	15.04.1
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
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(hunspell)
Requires:	kdesdk-strigi-analyzers
Requires:	qt5-qtbase-database-plugin-sqlite
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
%doc %{_docdir}/HTML/*/lokalize
%{_bindir}/lokalize
%{_datadir}/applications/org.kde.lokalize.desktop
%{_datadir}/config.kcfg/lokalize.kcfg
%{_iconsdir}/hicolor/*/apps/*.*[gz]
%{_datadir}/kxmlgui5/lokalize/*.rc
%{_datadir}/lokalize

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
