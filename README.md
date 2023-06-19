# srpm-packages
一些自己写/改的 rpm 构建包，以 src.rpm 形式发布

现在在学校的虚拟机使用 fedora rawhide,不得已碰了下 rpm 打包...

- `dust-%{version}.src.rpm` 从 [RPM Sphere](https://github.com/rpmsphere/source/) ~~偷~~ 改的，扔掉了一些不必要的 cargo 配置，并添加了 O3 与 CPU 特异化、thin-LTO 编译标志。
