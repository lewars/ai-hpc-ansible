# Molecule Tests for NVIDIA Role

This directory contains Molecule test scenarios for the NVIDIA role, which automates the installation and configuration of NVIDIA drivers and CUDA Toolkit.

## Test Scenarios

### 1. Default (RHEL/Rocky Linux)
Tests the role with a Red Hat Enterprise Linux / Rocky Linux 9 virtual machine.

To run:
```
molecule test
```

### 2. Ubuntu
Tests the role with an Ubuntu 24.10 virtual machine.

To run:
```
molecule test -s ubuntu
```

## Test Configuration

The tests use QEMU/KVM directly using the `qemu-system-x86_64` command to create virtual machines. The virtual machines are configured using cloud-init.

### Base Images

- RHEL/Rocky: `Rocky-9-GenericCloud-Base.latest.x86_64.qcow2`
- Ubuntu: `ubuntu-24.10-server-cloudimg-amd64.img`

By default, the base images will be downloaded from their respective repositories. You can set the `base_image_download` variable to `false` and provide a local path in `base_image_local_path` to use local images.

### VM Configuration

- Memory: 4096 MB
- CPU: 4 cores
- Storage: 20 GB
- SSH Port: 2222

### User Configuration

- Username: `molecule`
- Password: None (SSH key authentication)

## Test Execution

The test sequence includes:
1. Dependency installation
2. Linting
3. VM creation
4. Preparation (installing prerequisites)
5. Role execution
6. Idempotence check
7. Verification
8. Cleanup

## Mock Testing

Since real GPU hardware may not be available in CI/CD environments, the tests use mock files and directories to simulate NVIDIA driver and CUDA Toolkit installation. This allows testing the role's installation logic without actual hardware.

For real hardware testing, modify the verify tests to check for actual NVIDIA devices and drivers.

## Customization

You can modify the following files to customize the tests:
- `molecule.yml`: Change VM configuration, test sequence, etc.
- `create.yml`: Modify VM creation process
- `prepare.yml`: Add or modify prerequisites
- `converge.yml`: Modify role variables for testing
- `verify.yml` and `../tests/test_nvidia.py`: Change verification tests
