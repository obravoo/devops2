import validadorrut


class TestCalculator:

    def test_compare_valid_ruts_int_string(self):
        val1 = validadorrut.valida(180612890)
        val2 = validadorrut.valida('180612890')

        assert val1 == val2

    def test_compare_invalid_ruts_int_string(self):
        val1 = validadorrut.valida(180612891)
        val2 = validadorrut.valida('180612891')

        assert val1 == val2

    def test_compare_valid_ruts_with_dash_and_dots(self):
        val1 = validadorrut.valida('18.061.289-0')
        val2 = validadorrut.valida('18.061.289-0')

        assert val1 == val2

    def test_compare_invalid_ruts_with_dash_and_dots(self):
        val1 = validadorrut.valida('18.061.289-1')
        val2 = validadorrut.valida('18.961.289-0')

        assert val1 == val2

    def test_invalid_long_ruts(self):
        val1 = validadorrut.valida('181286128911')
        val2 = validadorrut.valida('181238381220')

        assert val1 == val2
