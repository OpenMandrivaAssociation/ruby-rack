# Generated from rack-1.1.0.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	rack

Summary:	A modular Ruby webserver interface

Name:		ruby-%{rbname}

Version:	1.1.0
Release:	5
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://rack.rubyforge.org
Source0:	%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Rack provides minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.rubyforge.org.

%package	doc
Summary:	Documentation for %{name}

Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install
rm -f %{buildroot}%{_bindir}/rackup

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rackup
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/KNOWN-ISSUES
%{ruby_gemdir}/gems/%{rbname}-%{version}/README
%{ruby_gemdir}/gems/%{rbname}-%{version}/SPEC


