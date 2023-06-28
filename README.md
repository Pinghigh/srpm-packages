Warning: 教练配的系统太烂导致系统没有 oom 就寄掉了，相应的，虚拟机 fedora 用的 btrfs，一断电全寄了恢复不过来，于是回归 arch（还是 arch 流畅），此仓库暂时性 Archive。

# srpm-packages
一些自己写/改的 rpm 构建包，以 src.rpm + spec 形式发布

现在在学校的虚拟机使用 fedora rawhide,不得已碰了下 rpm 打包...

- `dust`: 从 [RPM Sphere](https://github.com/rpmsphere/source/) ~~偷~~ 改的，扔掉了一些不必要的 cargo 配置，并添加了 O3 与 CPU 特异化、thin-LTO 编译标志。

- `gotop`: 来源同上，但是实际上大部分东西是自己写的，因为更新到新分支之后不能再用 `make` 构建而是直接使用了 `go build`。添加了 `x86-64-v3` 标志，可以自己改 `GOAMD64` 换成别的。
