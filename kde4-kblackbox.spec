%define		_state		stable
%define		orgname		kblackbox
%define		qtver		4.8.0

Summary:	A little logical game for KDE
Summary(pl.UTF-8):	Prosta gra logiczna
Summary(pt_BR.UTF-8):	Versão do jogo Blackbox do Emacs para KDE
Name:		kde4-%{orgname}
Version:	4.12.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	93652023245083238c8242ac2532fb3c
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBlackbox is a game of hide and seek played on an grid of boxes. Your
opponent (the Random number generator, in this case) has hidden
several balls within this box. By shooting rays into the box and
observing where they emerge it is possible to deduce the positions of
the hidden balls. The fewer rays you use to find the balls, the better
(the lower) your score.

%description -l pl.UTF-8
KBlackbox to gra w ukrywanie i szukanie rozgrywana na siatce pudełek.
Przeciwnik (w tym wypadku generator liczb losowych) ukrył kilka piłek
w tym pudełku. Poprzez strzelanie promieniami w pudełko i obserwowanie
jak się wynurzają można wydedukować położenie ukrytych piłek. Im mniej
promieni użyje się do znalezienia piłek, tym lepszy (mniejszy) jest
wynik.

%description -l pt_BR.UTF-8
Versão do jogo Blackbox do Emacs para KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_desktopdir}/kde4/kblackbox.desktop
%{_datadir}/apps/kblackbox
%{_iconsdir}/*/*/apps/kblackbox.png
