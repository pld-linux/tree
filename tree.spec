Summary:	A utility which displays a tree view of the contents of directories
Summary(de.UTF-8):	Druckt eine Ansicht einer Dateihierarchie
Summary(fr.UTF-8):	Affiche une arborescence de répertoires
Summary(pl.UTF-8):	Narzędzie wyświetlające zawartość katalogów w postaci drzewka
Summary(tr.UTF-8):	Bir dizin ağacının görünümünü listeler
Name:		tree
Version:	1.8.0
Release:	2
License:	GPL v2+
Group:		Applications/File
Source0:	http://mama.indstate.edu/users/ice/tree/src/%{name}-%{version}.tgz
# Source0-md5:	715191c7f369be377fc7cc8ce0ccd835
URL:		http://mama.indstate.edu/users/ice/tree/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tree utility recursively displays the contents of directories in a
tree-like format. Tree is basically a UNIX port of the tree DOS
utility.

%description -l de.UTF-8
Dieses Programm ist im Prinzip ein UNIX-Port des äußerst praktischen
DOS-Utility-Programms tree, das eine Darstellung des gewünschten
Verzeichnisbaums ausgibt, zusammen mit den Dateien, die ihm gehören.
Beinhaltet auch Unterstützung für 'color ls'-artige Auflistungen.

%description -l fr.UTF-8
Ce programme est à la base un portage sous UNIX de l'utilitaire DOS
'tree', qui affiche l'arbrescence d'un répertoire spécifié. Il inclue
un support pour des listings de style 'color ls'.

%description -l pl.UTF-8
Narzędzie tree rekursywnie wyświetla zawartość katalogów w formacie
drzewka. Jest to uniksowy port programu tree znanego z DOS.

%description -l tr.UTF-8
Bu program kullanışlı bir DOS aracı olan tree'nin UNIX'e taşınmış
biçimidir. Bir dizin ağacının görünümünü içinde yer alan altdizinler
ve dosyalarla beraber listeler.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} $(getconf LFS_CFLAGS)" \
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
%doc CHANGES INSTALL LICENSE README TODO
%attr(755,root,root) %{_bindir}/tree
%{_mandir}/man1/tree.1*
