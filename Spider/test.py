from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import smtplib
from email.mime.text import MIMEText
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait


def send_email():
    # 设置服务器所需信息
    # qq邮箱服务器地址
    mail_host = 'smtp.qq.com'
    # qq用户名
    mail_user = '2738473607'
    # 密码(部分邮箱为授权码)
    mail_pass = 'rvfgtaybzjqoddhh'
    # 邮件发送方邮箱地址
    sender = '2738473607@qq.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['2196651181@qq.com']

    # 设置email信息
    # 邮件内容设置
    message = MIMEText('今日份打卡成功！', 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = '自动化打卡成功'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # 连接到服务器
        smtpObj.connect(mail_host, 465)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('发送邮件成功')
    except smtplib.SMTPException as e:
        print('发送邮件失败', e)

if __name__ == '__main__':
    # 模拟浏览器打开网站
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
    driver.get('https://jksb.v.zzu.edu.cn')

    sleep(5)
    driver.switch_to.frame('my_toprr')  # 需先跳转到iframe框架
    sleep(5)
    driver.find_element_by_name('uid').send_keys('202124100229')
    sleep(5)
    driver.find_element_by_name('upw').send_keys('2003TYCmiku@233')
    driver.find_element_by_name('smbtn').click()


    driver.switch_to.frame('zzj_top_6s')  # 需先跳转到iframe框架)
    driver.find_element_by_xpath('/ html / body / form / div / div[11] / div[3] / div[4]').click()
    sleep(10)

    driver.find_element_by_xpath('/html/body/form/div/div[7]/div[4]').click()
    sleep(10)
    send_email()
    print("打卡结束")
    sleep(10)  # 终端给你时间确认已经打卡成功
    driver.quit()