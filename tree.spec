Summary: A utility which displays a tree view of the contents of directories.
Name: tree
Version: 1.2
Release: 6
Group: Applications/File
Copyright: GPL
Source: ftp://sunsite.unc.edu/pub/Linux/Incoming/tree-1.2.tgz
Patch: tree-1.0-misc.patch
Prefix: /usr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the tree DOS
utility.

Install tree if you think it would be useful to view the contents of
specified directories in a tree-like format.

%prep
%setup -q
#%patch -p1

%build
rm -f tree
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make	BINDIR=$RPM_BUILD_ROOT/usr/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/man/man1 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/tree
/usr/man/man1/tree.1
%doc README
