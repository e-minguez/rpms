# eminguez's RPM

This repository contains a series of rpms or tools I use.
The generated packages are available here https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/

## Structure

SPEC location | Role | Status | Package build location
------------ | ------------- | ------------ | ------------
[kustomize/](kustomize/) | kustomize package | [![kustomize build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/kustomize/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/kustomize/) | [kustomize package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/kustomize/)
[file-to-machineconfig/](file-to-machineconfig/) | file-to-machineconfig package | [![file-to-machineconfig build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/file-to-machineconfig/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/file-to-machineconfig/) | [file-to-machineconfig package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/file-to-machineconfig/)
[filetranspiler/](filetranspiler/) | filetranspiler package | [![filetranspiler build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/filetranspiler/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/filetranspiler/) | [filetranspiler package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/filetranspiler/)
[inlets/](inlets/) | inlets package | [![inlets build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/inlets/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/inlets/) | [inlets package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/inlets/)
[stern/](stern/) | stern package | [![stern build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/stern/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/stern/) | [stern package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/stern/)
[operator-sdk/](operator-sdk/) | Operator SDK package | [![operator-sdk build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/operator-sdk/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/operator-sdk/) | [operator-sdk package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/operator-sdk/)
[gnomeshell-extension-manage/](gnomeshell-extension-manage/) | gnomeshell-extension-manage package | [![gnomeshell-extension-manage build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/gnomeshell-extension-manage/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/gnomeshell-extension-manage/) | [gnomeshell-extension-manage package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/gnomeshell-extension-manage/)
[discover-session-dbus-address/](discover-session-dbus-address/) | discover-session-dbus-address package | [![discover-session-dbus-address build status](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/discover-session-dbus-address/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/discover-session-dbus-address/) | [discover-session-dbus-address package](https://copr.fedorainfracloud.org/coprs/eminguez/eminguez-RPMs/package/discover-session-dbus-address/)
[scripts/](scripts/) | Scripts | none

## Changelog

### Nov 30 2020

* Terraform and packer removed, use the official repository instead:

```bash
# s/fedora/RHEL/g if using RHEL/CentOS
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo dnf install terraform packer -y
```

* `ct` repo is archived. Removing the `ct` package as well.

## Credits

https://hobo.house/2017/09/03/automate-rpm-builds-from-git-sources-using-copr/
https://copr.fedorainfracloud.org/coprs/jstribny/packer/
