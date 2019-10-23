import  os,sys,pytest
import  allure
sys.path.append(os.getcwd())



class Test_allure:
    def setup(self):
        pass
    def teardown(self):
        pass



    @pytest.mark.parametrize("a",[1,2,3])
    @pytest.allure.severity(pytest.allure.severity_level.CRITIVCAL)
    @allure.step('woshiceshibuzou001')
    def test_al(self,a):
        allure.attach('miaoshi','woshiceshibu001232')
        assert a != 2

if __name__ == '__main__':
    pytest.main()