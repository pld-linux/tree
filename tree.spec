%define		pre	b3
Summary:	A utility which displays a tree view of the contents of directories
Summary(de):	Druckt eine Ansicht einer Dateihierarchie
Summary(fr):	Affiche une arborescence de r�pertoires
Summary(pl):	Narz�dzie wy�wietlaj�ce zawarto�� katalog�w w postaci drzewka
Summary(tr):	Bir dizin a�ac�n�n g�r�n�m�n� listeler
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
Dieses Programm ist im Prinzip ein UNIX-Port des �u�erst praktischen
DOS-Utility-Programms tree, das eine Darstellung des gew�nschten
Verzeichnisbaums ausgibt, zusammen mit den Dateien, die ihm geh�ren.
Beinhaltet auch Unterst�tzung f�r 'color ls'-artige Auflistungen.

%description -l fr
Ce programme est � la base un portage sous UNIX de l'utilitaire DOS
'tree', qui affiche l'arbrescence d'un r�pertoire sp�cifi�. Il inclue
un support pour des listings de style 'color ls'.

%description -l pl
Narz�dzie tree rekursywnie wy�wietla zawarto�� katalog�w w formacie
drzewka. Jest to uniksowy port programu tree znanego z DOS.

%description -l tr
Bu program kullan��l� bir DOS arac� olan tree'nin UNIX'e ta��nm��
bi�imidir. Bir dizin a�ac�n�n g�r�n�m�n� i�inde yer alan altdizinler
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
