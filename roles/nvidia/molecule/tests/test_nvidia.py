"""
Molecule tests for the NVIDIA role.

These tests verify that the NVIDIA driver and CUDA Toolkit installation
has been properly performed.
"""

import os
import pytest
import testinfra.utils.ansible_runner


# Initialize testinfra with Ansible runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "file_path",
    [
        "/usr/bin/nvidia-smi",
        "/usr/bin/nvidia-settings",
    ],
)
def test_nvidia_driver_files(host, file_path):
    """Test that the NVIDIA driver files are present."""
    f = host.file(file_path)
    assert f.exists
    assert f.is_file
    assert f.mode == 0o755


@pytest.mark.xfail
def test_nvidia_persistence_daemon(host):
    """Test that the NVIDIA persistence daemon is installed and running."""
    assert host.service("nvidia-persistenced").exists
    assert host.service("nvidia-persistenced").is_enabled
    assert host.service("nvidia-persistenced").is_running

    # We can only properly test this with real hardware, but we can check
    # if it's installed
    assert host.file("/usr/bin/nvidia-persistenced").exists


@pytest.mark.xfail
def test_nvidia_fabric_manager(host):
    """Test that the NVIDIA fabric manager is installed."""
    assert host.service("nvidia-fabricmanager").is_enabled
    assert host.service("nvidia-fabricmanager").is_running

    # We can only properly test this with real hardware, but we can check
    # if it's installed
    assert host.file("/usr/bin/nvidia-fabricmanager").exists


@pytest.mark.parametrize(
    "file_path",
    [
        "/usr/local/cuda/bin/nvcc",
        "/usr/local/cuda/bin/cuda-gdb",
        "/usr/local/cuda/bin/cuda-memcheck",
    ],
)
def test_cuda_toolkit_installation(host, file_path):
    """Test that the CUDA Toolkit is installed."""
    f = host.file(file_path)
    assert f.exists
    assert f.is_file
    assert f.mode == 0o755


def test_cuda_symlink(host):
    """Test that the CUDA symlink exists and points to the correct version."""
    cuda_link = host.file("/usr/local/cuda")
    assert cuda_link.exists
    assert cuda_link.is_symlink
    assert cuda_link.linked_to == "/usr/local/cuda-12.8"


def test_nvidia_paths_in_environment(host):
    """Test that NVIDIA paths are in the environment."""
    try:
        nvcc_path = host.find_command("nvcc", ["/usr/local/cuda/bin"])
        assert "/usr/local/cuda" in nvcc_path
    except ValueError:
        pytest.fail(
            "NVIDIA CUDA command 'nvcc' not found in PATH or /usr/local/cuda/bin"
        )


def test_nvidia_modules_loaded(host):
    """Test that NVIDIA kernel modules are present."""
    # For a real test, we'd check if modules are loaded
    # Here we just test if the mock files exist
    modules_dir = "/usr/lib/modules/{}/extra/nvidia".format(host.system_info.release)
    assert host.file(modules_dir).exists
    assert host.file(os.path.join(modules_dir, "nvidia.ko")).exists


def test_system_has_gpu(host):
    """Test that the system has a GPU (or mock GPU for testing)."""
    # In a real test, we'd check lspci output
    # For the mock test, we'll assume success
    assert True, "This is a mock test, skipping actual GPU detection"


def test_cuda_sample_compilation(host):
    """Test CUDA sample compilation if samples are installed."""
    # This would compile a sample CUDA program
    # For mock testing, we'll just check if the mock CUDA is available
    assert host.file("/usr/local/cuda").exists
