%define		pre	b3
Summary:	A utility which displays a tree view of the contents of directories
Summary(de):	Druckt eine Ansicht einer Dateihierarchie
Summary(fr):	Affiche une arborescence de répertoires
Summary(pl):	Narzêdzie wy¶wietlaj±ce zawarto¶æ katalogów w postaci drzewka
Summary(tr):	Bir dizin aðacýnýn görünümünü listeler
Name:		tree
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://mama.indstate.edu/linux/tree/%{name}-%{version}%{pre}.tgz
# Source0-md5:	93110789bcd48f633c2ea1d1b3835dac
Patch1:		%{name}-gcc34.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tree utility recursively displays the contents of directories in a
tree-like format. Tree is basically a UNIX port of the tree DOS
utility.

%description -l de
Dieses Programm ist im Prinzip ein UNIX-Port des äußerst praktischen
DOS-Utility-Programms tree, das eine Darstellung des gewünschten
Verzeichnisbaums ausgibt, zusammen mit den Dateien, die ihm gehören.
Beinhaltet auch Unterstützung für 'color ls'-artige Auflistungen.

%description -l fr
Ce programme est à la base un portage sous UNIX de l'utilitaire DOS
'tree', qui affiche l'arbrescence d'un répertoire spécifié. Il inclue
un support pour des listings de style 'color ls'.

%description -l pl
Narzêdzie tree rekursywnie wy¶wietla zawarto¶æ katalogów w formacie
drzewka. Jest to uniksowy port programu tree znanego z DOS.

%description -l tr
Bu program kullanýþlý bir DOS aracý olan tree'nin UNIX'e taþýnmýþ
biçimidir. Bir dizin aðacýnýn görünümünü içinde yer alan altdizinler
ve dosyalarla beraber listeler.

%prep
%setup -q
%patch1 -p1

%build
rm -f tree-1.4
%{__make} CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tree
%{_mandir}/man1/*
