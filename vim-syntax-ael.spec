%define		syntax	ael
Summary:	ael.vim : Syntax for Asterisk Extension Language (AEL)
Name:		vim-syntax-%{syntax}
Version:	0.3
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	http://www.vim.org/scripts/download_script.php?src_id=12203#/%{syntax}.vim
# Source0-md5:	3342cdd2b14ddb6427e53b5855bb99c9
Source1:	filetype.vim
URL:		http://www.vim.org/scripts/script.php?script_id=1900
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Includes highlighting for most of the basic structure of AEL files.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
