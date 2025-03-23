# AI-HPC-Ansible

Ansible playbooks and roles for installing and configuring NVIDIA drivers, CUDA Toolkit, Pyxis, and Enroot on HPC environments running Red Hat 9 and Ubuntu 24.10.

## Overview

This project provides a set of Ansible roles to automate the installation and configuration of:

- NVIDIA drivers and CUDA Toolkit
- Pyxis (Slurm container plugin)
- Enroot (Unprivileged container utility)

The roles support both online and offline (local RPM) installation methods, making it suitable for secured environments without internet access.

## Requirements

- Ansible 2.12+
- Python 3.9+
- QEMU/KVM (for Molecule testing)



## Supported Environments

- **Red Hat 9**
- **Ubuntu 24.10**

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-hpc-ansible.git
cd ai-hpc-ansible
```

2. Install dependencies:

```bash
task deps
```

3. Deploy to lab environment (default):

```bash
task deploy:lab
```

## Environment-Specific Configurations

- **lab**: Default testing environment
- **dev**: Development environment
- **prod**: Production environment

Set environment-specific variables in `inventory/group_vars/[environment]/main.yml`.

## Testing

This project uses Molecule with QEMU/KVM for testing roles:

```bash
# Test all roles
task test:all

# Test a specific role
task test:nvidia
task test:pyxis
task test:enroot
```

## Offline Installation

For environments without internet access, the roles support installing from local RPM files:

- NVIDIA Driver RPM: `https://us.download.nvidia.com/tesla/570.124.06/nvidia-driver-local-repo-rhel9-570.124.06-1.0-1.x86_64.rpm`
- CUDA Toolkit RPM: `https://developer.download.nvidia.com/compute/cuda/12.8.1/local_installers/cuda-repo-rhel9-12-8-local-12.8.1_570.124.06-1.x86_64.rpm`

Configure the paths to local RPMs in your inventory variables.
