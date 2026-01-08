%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Computer-aided translation tool for KDE
Name:		lokalize
Version:	25.12.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(hunspell)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
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
%{_datadir}/lokalize
%{_datadir}/knotifications6/lokalize.notifyrc
%{_datadir}/qlogging-categories6/lokalize.categories
