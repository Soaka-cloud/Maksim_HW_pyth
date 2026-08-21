from pages.calculator_page import CalculatorPage


def test_calculator(chrome_driver):
    calculator = CalculatorPage(chrome_driver)
    calculator.open()
    calculator.set_delay("45")

    for button in ["7", "+", "8", "="]:
        calculator.click_button(button)

    calculator.wait_for_result("15")
    assert calculator.get_result() == "15"
