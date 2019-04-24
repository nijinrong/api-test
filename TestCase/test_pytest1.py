import allure

@allure.feature("测试功能二")
class Test_py:
    @allure.story("测试小功能3")
    def test_demo2(self):
        a = 1
        b = 1
        assert a == b

    @allure.story("测试小功能4")
    def test_demo3(self):
        a = 2
        b = 2
        assert a == b
