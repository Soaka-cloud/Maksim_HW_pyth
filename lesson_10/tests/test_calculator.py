import allure

from pages.calculator_page import CalculatorPage


@allure.title("Сложение с задержкой на калькуляторе")
@allure.description("Проверка, что калькулятор вычисляет 7 + 8 = 15 "
                    "через 45 секунд после нажатия =")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(chrome_driver):
    calculator = CalculatorPage(chrome_driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator.set_delay("45")

    with allure.step("Нажать кнопки 7, +, 8, ="):
        for button in ["7", "+", "8", "="]:
            calculator.click_button(button)

    with allure.step("Дождаться появления результата 15"):
        calculator.wait_for_result("15")

    with allure.step("Проверить, что на экране отобразилось 15"):
        assert calculator.get_result() == "15"
