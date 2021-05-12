%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Computer-aided translation tool for KDE
Name:		lokalize
Version:	21.04.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
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
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(hunspell)
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

%files -f %{name}.lang
%{_bindir}/lokalize
%{_datadir}/applications/org.kde.lokalize.desktop
%{_datadir}/metainfo/org.kde.lokalize.appdata.xml
%{_datadir}/config.kcfg/lokalize.kcfg
%{_iconsdir}/hicolor/*/apps/*.*[gz]
%{_datadir}/kxmlgui5/lokalize/*.rc
%{_datadir}/lokalize
%{_datadir}/knotifications5/lokalize.notifyrc
%{_datadir}/qlogging-categories5/lokalize.categories

#----------------------------------------------------------------------------

%prep
%autosetup -p1

find . -name "*.py" |xargs 2to3 -w

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
