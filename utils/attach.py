import allure
from allure_commons.types import AttachmentType
import os


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot',
                  attachment_type=AttachmentType.PNG, extension='.png')

def add_xml_data(browser):
    xml_data = browser.driver.page_source
    allure.attach(
        xml_data,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML
    )

