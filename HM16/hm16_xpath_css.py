
from selenium.webdriver import Chrome


def test_web_page():
    driver_chrome = Chrome('chromedriver.exe')
    driver_chrome.maximize_window()
    driver_chrome.get('https://netpeaksoftware.com/')

    xpath

    logo_NS_locator = "//*[@class='navbar-brand']//a"
    seo_analytics_for_all = '//div[contains(text(),'SEO analytics for all')]'
    multisearch_locator = '//input[@id='q']'
    header_locator = '//*[@id='header']'
    x_close_header_banner = '//button[contains(text(),'Accept')]'

    multi_header = '//input[@id='q']/ancestor::div[@class='multi-header']'
    all_page_locator = '//*[@class='home-page__head__left__bages__item']/../../../ancestor::div[@id='app']'
    brands_locator = '//*[@class='home-page__companies__list']/ancestor::div[@class='home-page__companies__wrap']'
    img_of_posts = '//*@class='post-tile__img''
    name_of_founder = '//div[contains(text(),'Alex Wise')]/../child::div[@class='home-page__wise__badge__name']'

    founder_locator = '//div[contains(text(),'Alex Wise')]/../child::div[@class='home-page__wise__badge__post']'
    x_close_miltisearch = '//input[@id='q']/following::div[@class='multi-icon multi-closeIcon']'
    prodyct_feache_locator = '//*[@class='home-page__companies__list']/following::div[@class='NS-photoTab--wrap flex align-fs NS-product__features__item first']'
    blok_powerfull_locator = '//div[contains(text(),'Crawl 500,000 URLs in just 2.5 hours with Netpeak ')]/../ancestor::div[@class='NS-collapseBlock__area']'
    section_ns_locator = '//div[contains(text(),'stands with Ukraine')]/ancestor-or-self::section[@class='home-page__stands']'

    straight_from_our_users_locator = '//h2[contains(text(),'Straight from our users')]/ancestor-or-self::h2[@class='home-page__reviews__title home-page__reviews__title__en']'
    button_tak_survey_locator = '//button[contains(text(),'Take a Survey')]'
    uptitle_take_survey_locator = '//button[contains(text(),'Take a Survey')]/../child::h2[@class='switcher_cta__title']'
    title_tell_us_locator = '//h2[contains(text(),'Tell us more about your needs so that we can tailo')]'
    photo_founder_locator = '//div[contains(text(),'Founder & CEO, Netpeak Software')]/../../child::img[@src='https://frontend.netpeaksoftware.com/dist/wise.png?d5a7e6afc01d856aa79ae170b3ec4051']'

    anothert_way_photo_founder_locator = '//div[contains(text(),'Founder & CEO, Netpeak Software')]/../../../child::div[@class='home-page__wise__badge']'
    link_iprospect_locator = '//*[@href='https://www.iprospect.com/fr/fr/']'
    posts_blog = '//p[contains(text(),'I highly value Netpeak Spider for its speed and th')]/../../../following::div[@class='content-container tile-block--main']'
    view_all_posts_locator = '//p[contains(text(),'I highly value Netpeak Spider for its speed and th')]/../../../following::div[@class='content-container tile-block--main']/../child::div[@class='show-more text-center container--wrap']'
    block_with_buttons_start_trial_locator = '//div[contains(text(),'Free trial, no credit card required')]/../child::div[@class='home-page__cta__button__wrap']'

    button_free_download = '//*[contains(@class,'fa m-r-1 fa-download')]/ancestor::a[@id='try_it_for_free_first' and 'NS-button NS-button__greenblueClear auth_link NS-button__gift' and @style='margin-right: 40px;']'
    pricing_footer = '//*[contains(@href,'/pricing')]/ancestor::li[@class='menu-footer-item']'
    baner_locator2 = '//*[contains(@class, 'autumn-banner-popup__logo relative')]/ancestor::a[@id='banner-easter']'
    baner_locator = '//a[@id='banner-easter']'
    link_leartn_more_about = '//*[contains(@href, '/screaming-frog-alternative') and @class='spider_advantages__link']'

    css

    banener_locator = '//a[@id='banner-easter']'
    banner_css = '#banner-easter'

    multisearch = '//input[@id='q']'
    multisearch_css = '#q'

    link_leartn_more_about = '//*[contains(@href, '/screaming-frog-alternative') and @class='spider_advantages__link']'
    link_leartn_more_about_css = '.spider_advantages__link '

    baner_locator = '//a[@id='banner-easter']'
    baner_locator_css = '#banner-easter'

    photo_founder_locator = '//div[contains(text(),'Founder & CEO, Netpeak Software')]/../../child::img[@src='https://frontend.netpeaksoftware.com/dist/wise.png?d5a7e6afc01d856aa79ae170b3ec4051']'
    photo_founder_locator_css = '.home-page__wise__badge__img'

    testimonials_locator = '//div[@id='testimonialsContent']'
    testimonials_locator = '#testimonialsContent'

    author_emma_locator = '//span[contains(text(),'Emma Ramsey')]'
    author_emma_css = '[title='Emma Ramsey']'

    post_tools_locator = '//a[contains(@href,'/blog/tools-and-tactics-for-a-successful-content-strategy') and @target='_self' and @class= 'fake-link__block post-a']'
    post_tools_css = 'a[href^='/blog/tools-and-tactics-for-a-successful-content-strategy']'

    title_tell_us_locator = '//h2[contains(text(),'Tell us more about your needs so that we can tailo')]'
    title_tell_us_css = 'switcher_cta__title'

    button_tak_survey_locator = '//button[contains(text(),'Take a Survey')]'
    button_tak_survey_css = 'XcbUQCRE'
