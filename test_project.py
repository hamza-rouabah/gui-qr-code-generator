from project import get_os, handle_error, generate_qr_code
import pytest
def main():
    test_get_os()
    test_get_os_with_params()
    test_handle_error()
    test_generate_qr_code()

def test_get_os():
    import platform
    assert get_os() == platform.system()
    
def test_get_os_with_params():
    with pytest.raises(TypeError):
        get_os('no parameter needed')

def test_handle_error():
    with pytest.raises(TypeError):
        handle_error()

def test_generate_qr_code():
    with pytest.raises(TypeError):
        generate_qr_code()