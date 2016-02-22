%{?scl:%scl_package nodejs-github-url-from-git}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-github-url-from-git
Version:        1.4.0
Release:        2%{?dist}
Summary:        Parse a GitHub git URL and return the GitHub repository URL

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          Development/Libraries
#No license file included, "MIT" indicated in README and package.json
#A copy of the MIT license based on the version included with express, another
#node module by the same author, is included in Source1, and has been sent
#upstream: https://github.com/visionmedia/github-url-from-git/pull/5
License:        MIT
URL:            https://github.com/visionmedia/node-github-url-from-git
Source0:        http://registry.npmjs.org/github-url-from-git/-/github-url-from-git-%{version}.tgz
Source1:        https://raw.github.com/tchollingsworth/node-github-url-from-git/154fb09296b79637e25952638782995ad6812612/LICENSE
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

#for tests
#BuildRequires:  %{?scl_prefix}npm(mocha)
#BuildRequires:  %{?scl_prefix}npm(should)
#BuildRequires:  %{?scl_prefix}npm(better-assert)

%description
%{summary}.

%prep
%setup -q -n package

#copy LICENSE file into %%_builddir so it works with %%doc
cp %{SOURCE1} LICENSE

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/github-url-from-git
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/github-url-from-git

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
#mocha test.js --reporter spec --require should

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/github-url-from-git
%doc Readme.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.0-2
- rebuilt

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.4.0-1
- New upstream release 1.4.0

* Wed Dec 11 2013 Tomas Hrcka <thrcka@redhat.com> - 1.1.1-2.1
- enable scl support

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-2
- restrict to compatible arches

* Sun Jun 02 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- initial package
