Summary:	A utility which displays a tree view of the contents of directories
Summary(de):	Druckt eine Ansicht einer Dateihierarchie 
Summary(fr):	Affiche une arborescence de répertoires
Summary(tr):	Bir dizin aðacýnýn görünümünü listeler
Name:		tree
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://mama.indstate.edu/linux/tree/%{name}-%{version}.tgz
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

%description -l tr
Bu program kullanýþlý bir DOS aracý olan tree'nin UNIX'e taþýnmýþ
biçimidir. Bir dizin aðacýnýn görünümünü içinde yer alan altdizinler
ve dosyalarla beraber listeler.

%prep
%setup -q

%build
rm -f tree
%{__make} CFLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,man/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/tree
%{_mandir}/man1/*
