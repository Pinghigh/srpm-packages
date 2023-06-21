%undefine _missing_build_ids_terminate_build

Name:     gotop
Version:  4.2.0
Release:  1
Summary:  A terminal based graphical activity monitor inspired by gtop and vtop
License:  Expat(MIT)
Group:    System/Utility
URL:      https://github.com/xxxserxxx/gotop
Source0:  https://github.com/xxxserxxx/gotop/archive/refs/tags/v%{version}.tar.gz
BuildRequires: go-rpm-macros
BuildRequires: golang

%description
Another terminal based graphical activity monitor, inspired by gtop and vtop, this time written in Go!

%prep
%setup -q
 
%build
echo %{version}
export CGO_ENABLED=0
export GOAMD64="v3"
go build \
    -gcflags "all=-trimpath=${PWD}" \
    -asmflags "all=-trimpath=${PWD}" \
    -ldflags "-X main.Version=v%{version} -extldflags '${LDFLAGS} -s -w'" \
    -buildmode=pie \
    ./cmd/gotop
go run ./cmd/gotop --create-manpage > gotop.8
gzip gotop.8

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.8.gz %{buildroot}%{_mandir}/%{name}.8.gz
install -Dm644 layouts/htop %{buildroot}%{_sysconfdir}/%{name}/htop
#install -Dm644 LICENSE %{buildroot}%{_datadir}/%{name}/LICENSE

%files
%license LICENSE
%_bindir/%{name}
%_mandir/%{name}.8.gz
%_sysconfdir/%{name}/htop

%changelog
* Tue Jun 20 2023 Tibrella Dai <pinghigh24678@outlook.com> 4.2.0
- Switch to the branch being maintained and add some optimization

* Wed Dec 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuilt for Fedora
