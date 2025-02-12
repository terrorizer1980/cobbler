import pytest

from cobbler.api import CobblerAPI
from cobbler.items.distro import Distro
from cobbler.items.item import Item
from tests.conftest import does_not_raise


def test_item_create():
    # Arrange
    test_api = CobblerAPI()

    # Act
    titem = Item(test_api)

    # Assert
    assert isinstance(titem, Item)


def test_make_clone():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act & Assert
    with pytest.raises(NotImplementedError):
        titem.make_clone()


@pytest.mark.skip
def test_from_dict():
    # Arrange
    titem = Item()

    # Act
    titem.from_dict()
    # Assert
    assert False


def test_uid():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    titem.uid = "uid"

    # Assert
    assert titem.uid == "uid"


def test_children():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    titem.children = []

    # Assert
    assert titem.children == []


def test_get_children():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    result = titem.get_children()

    # Assert
    assert result == []


@pytest.mark.skip
def test_get_descendatns():
    # Arrange
    titem = Item()

    # Act
    titem.get_descendants()
    # Assert
    assert False


@pytest.mark.skip
def test_get_conceptual_parent():
    # Arrange
    titem = Item()

    # Act
    titem.get_conceptual_parent()
    # Assert
    assert False


def test_name():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    titem.name = "testname"

    # Assert
    assert titem.name == "testname"


def test_comment():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    titem.comment = "my comment"

    # Assert
    assert titem.comment == "my comment"


@pytest.mark.skip
def test_set_owners():
    # Arrange
    titem = Item()

    # Act
    titem.set_owners()
    # Assert
    assert False


@pytest.mark.skip
def test_set_kernel_options():
    # Arrange
    titem = Item()

    # Act
    titem.set_kernel_options_post()
    # Assert
    assert False


@pytest.mark.skip
def test_set_kernel_options_post():
    # Arrange
    titem = Item()

    # Act
    titem.set_kernel_options()
    # Assert
    assert False


@pytest.mark.skip
def test_set_autoinstall_meta():
    # Arrange
    titem = Item()

    # Act
    titem.set_autoinstall_meta()
    # Assert
    assert False


@pytest.mark.skip
def test_set_mgmt_classes():
    # Arrange
    titem = Item()

    # Act
    titem.set_mgmt_classes()
    # Assert
    assert False


@pytest.mark.skip
def test_set_mgmt_parameters():
    # Arrange
    titem = Item()

    # Act
    titem.set_mgmt_parameters()
    # Assert
    assert False


def test_template_files():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    titem.template_files = {}

    # Assert
    assert titem.template_files == {}


def test_boot_files():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    titem.boot_files = {}

    # Assert
    assert titem.boot_files == {}


def test_fetchable_files():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    titem.fetchable_files = {}

    # Assert
    assert titem.fetchable_files == {}


@pytest.mark.skip
def test_sort_key():
    # Arrange
    titem = Item()

    # Act
    titem.sort_key()
    # Assert
    assert False


@pytest.mark.skip
def test_find_match():
    # Arrange
    titem = Item()

    # Act
    titem.find_match()
    # Assert
    assert False


@pytest.mark.skip
def test_find_match_signle_key():
    # Arrange
    titem = Item()

    # Act
    titem.find_match_single_key()
    # Assert
    assert False


@pytest.mark.skip
def test_dump_vars():
    # Arrange
    titem = Item()

    # Act
    titem.dump_vars()
    # Assert
    assert False


@pytest.mark.skip
def test_set_depth():
    # Arrange
    titem = Item()

    # Act
    titem.set_depth()
    # Assert
    assert False


@pytest.mark.skip
def test_set_ctime():
    # Arrange
    titem = Item()

    # Act
    titem.set_ctime()
    # Assert
    assert False


@pytest.mark.parametrize("value,expected_exception", [
    (0.0, does_not_raise()),
    (0, pytest.raises(TypeError)),
    ("", pytest.raises(TypeError))
])
def test_mtime(value, expected_exception):
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    with expected_exception:
        titem.mtime = value

        # Assert
        assert titem.mtime == value


@pytest.mark.skip
def test_parent():
    # Arrange
    titem = Item()

    # Act
    titem.parent = ""
    # Assert
    assert False


@pytest.mark.skip
def test_check_if_valid():
    # Arrange
    titem = Item()

    # Act
    titem.check_if_valid()

    # Assert
    assert False


def test_to_dict():
    # Arrange
    test_api = CobblerAPI()
    titem = Item(test_api)

    # Act
    result = titem.to_dict()

    # Assert
    assert isinstance(result, dict)


def test_serialize():
    # Arrange
    kernel_url = "http://10.0.0.1/custom-kernels-are-awesome"
    test_api = CobblerAPI()
    titem = Distro(test_api)
    titem.remote_boot_kernel = kernel_url

    # Act
    result = titem.serialize()

    # Assert
    assert titem.remote_boot_kernel == kernel_url
    assert titem.remote_grub_kernel.startswith("(http,")
    assert "remote_grub_kernel" not in result
