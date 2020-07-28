from selenium import webdriver
import selenium
from time import sleep

username = "foodie_tahaa"
passwords = "i love my 4 ex"

class Instagram:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome("F:\\Chromedriver.exe")
        self.driver.get("http://instagram.com")
        self.username=username
        self.password=password

    def Login(self):
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    def auto_follow(self):
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()
            sleep(3)
            self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[2]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[3]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[4]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[5]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[6]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[7]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[8]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[9]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[10]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[11]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[12]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[13]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[14]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[15]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[16]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[17]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[18]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[19]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[20]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[21]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[22]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[23]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[24]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[25]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[26]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[27]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[28]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[29]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[30]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[31]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[32]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[33]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[34]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[35]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[36]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[37]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[38]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[39]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[40]/div[3]/button").click()
            sleep(0.87)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[2]/div/div/div[41]/div[3]/button").click()
            
    def user_follower(self,user_follow):
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(user_follow)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div").click()
        sleep(10)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        for i in range(20,60):
            sleep(4)
            self.driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button").click()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)) \
            .click()
        sleep(4)

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]") \
            .click()
        followers = self._get_names()

        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]") \
            .click()
        following = self._get_names()

        not_following_back = [user for user in following if user not in followers]
        root=tk.Tk()
        def getname(nfb):
            pass


        lb=tk.Label(root,command=lambda : getname(not_following_back))
        lb.pack()
        root.mainloop()

        print(not_following_back)

    def _get_names(self):
        sleep(4)
        # sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        # self.driver.execute_script('arguments[0].scrollIntoView()', #sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                            return arguments[0].scrollHeight;
                            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button") \
            .click()
        return names

insta=Instagram(username,password)
insta.Login()
insta.auto_follow()
#insta.get_unfollowers()
#insta.user_follower("")