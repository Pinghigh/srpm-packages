%undefine _debugsource_packages

Name:           dust
Version:        0.8.6
Release:        1
Summary:        A more intuitive version of du in rust
Group:          Text tools
License:        ASL
URL:            https://github.com/bootandy/dust
Source0:        https://github.com/bootandy/dust/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo

%global _missing_build_ids_terminate_build 0

%description
du + rust = dust. Like du but more intuitive.

%prep
%autosetup

%build
export CC=clang
export CXX=clang++
export LD=ld.lld
export AR=llvm-ar
export AS=llvm-as
export NM=llvm-nm
export STRIP=llvm-strip
export OBJCOPY=llvm-objcopy
export OBJDUMP=llvm-objdump
export READELF=llvm-readelf
export HOSTCC=clang
export HOSTCXX=clang++
export HOSTAR=llvm-ar
export HOSTLD=ld.lld
export CFLAGS="-O3 -funroll-loops -finline -march=native -mtune=native -flto=thin"
export LDFLAGS="--build-id=sha1"
RUSTFLAGS="-Copt-level=3 -Cembed-bitcode=y -Ctarget-cpu=native" CARGO_PROFILE_RELEASE_LTO="thin" cargo build --release

%install
%__mkdir_p %{buildroot}%{_bindir}
cp target/release/dust %{buildroot}%{_bindir}/

%files
%doc LICENSE README.md
%{_bindir}/dust

%changelog
* Mon Jun 19 2023 Tibrella Dai <pinghigh24678@outlook.com> 0.8.6
- Add some optimize
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.3
- Rebuilt for Fedora
* Tue May 12 2020 guillomovitch <guillomovitch> 0.5.1-1.mga8
+ Revision: 1583381
- imported package dust
