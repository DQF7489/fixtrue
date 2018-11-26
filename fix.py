import pytest

#
# def before():
#     print("before被执行")
# 通过函数形式来运行fixture
# @pytest.mark.usefixtures()
@pytest.fixture(autouse=True)
def test_delete():
    print("删除成功")
class Test04():


    # 通过参数方式 运行 fixture
    # @pytest.fixture()
    def test_get(self):
        print("查询成功")
    # 通过函数形式运行 fixture

    def test_put(self):
        print("修改成功")
    def test_post(self):
        print("新增成功")
a = Test04()