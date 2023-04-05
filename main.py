import tkinter as tk
import os
import sys
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
import time
import random
import mysql.connector
import pkg_resources
import threading
import configparser

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.set_window_size(1920, 1080)

def Randomsleep():
    _sleep = random.randint(60, 120)
    time.sleep(_sleep)

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, "resources", relative_path)

def show_login_form():
    window = tk.Tk()
    window.title("Login")
    window.geometry("505x698")
    img_path = pkg_resources.resource_filename(__name__, "resources/img/instabotify.png")
    logo = tk.PhotoImage(file=img_path)
    tk.Label(window, image=logo).grid(row=0, column=0, columnspan=2)

    tk.Label(window, text="Username").grid(row=1, column=0)
    tk.Label(window, text="Password").grid(row=2, column=0)

    username = tk.Entry(window)
    password = tk.Entry(window, show="*")

    username.grid(row=1, column=1)
    password.grid(row=2, column=1)

    def check_credentials():
        # Connect to the MySQL server
        cnx = mysql.connector.connect(
            host="db4free.net",
            user="igpreium",
            password="igpreium",
            database="igpremium"
        )

        # Query the users table
        cursor = cnx.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        params = (username.get(), password.get())
        cursor.execute(query, params)
        result = cursor.fetchone()

        if result is not None:
            messagebox.showinfo("Login", "Login successful!")
            window.destroy()
            show_home_screen()
        else:
            messagebox.showerror("Login", "Invalid username or password")

        cursor.close()
        cnx.close()

    tk.Button(window, text="Login", command=check_credentials).grid(row=3, column=0, columnspan=2)



    info_text = "InstaBotify is a simple yet effective Instagram Bot"
    tk.Label(window, text=info_text).grid(row=4, column=0, columnspan=2)
    dc = "To get help and stay up to date, please join this discord:"
    dcl = "https://discord.gg/ezffH3fRdk"
    discord_link = tk.Label(window, text=dc)
    discord_link.grid(row=5, column=0, columnspan=2)
    dcl = tk.Label(window, text=dcl, fg="blue", cursor="hand2")
    dcl.grid(row=6, column=0, columnspan=2)
    dcl.bind("<Button-1>", lambda e: webbrowser.open_new("https://discord.gg/ezffH3fRdk"))
    window.mainloop()



def show_home_screen():

    home_screen = tk.Tk()
    home_screen.title("Instagram Bot - Home")

    tk.Label(home_screen, text="Welcome to Instabotify!").grid(row=0, column=0, columnspan=2)

    def login():
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        try:
            button = driver.find_element(
                By.XPATH, '//button[text()="Only allow essential cookies"]'
            )
            button.click()
        except:
            print("Button 'Only allow essential cookies' not found. Skipping.")
            pass
        time.sleep(3)

    def follow():
        time.sleep(5)
        scroll = driver.find_element(By.XPATH, "/html")
        while True:
            for _ in range(2):
                time.sleep(5)
                driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight", scroll
                )
            fbuttons = driver.find_elements(By.XPATH, '//div[text()="Follow"]')
            try:
                for button in fbuttons:
                    if button.text == "Follow":
                        button.click()
                        print("Followed!")
                        Randomsleep()
            except:
                print("Can't find follow button, all people already followed?")
                time.sleep(3)

    def page_follow():
        time.sleep(3)
        scroll = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]",)
        while True:
            for _ in range(2):
                time.sleep(5)
                driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight", scroll
                )
            fbuttons = driver.find_elements(By.CSS_SELECTOR, "._aano div div button")
            try:
                for button in fbuttons:
                    if button.text == "Follow":
                        button.click()
                        print("Followed!")
                        Randomsleep()
            except:
                print("Can't find follow button, all people already followed?")
                time.sleep(3)
        


    def unfollow():
        scroll3 = driver.find_element(By.XPATH, "/html")
        while True:
            for _ in range(2):
                time.sleep(5)
                driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight", scroll3
                )
            ubuttons = driver.find_elements(By.CSS_SELECTOR, "._aano div div button")
            try:
                for button in ubuttons:
                    if button.text == "Following":
                        button.click()
                        time.sleep(3)
                        s = driver.find_element(By.XPATH, '//button[text()="Unfollow"]')
                        s.click()
                        print("UnFollowed!")
                        Randomsleep()
            except:
                print("Can't find unfollow button, all people already followed?")
                time.sleep(3)
        

   
    def logout():
        driver.get("https://www.instagram.com/")
        time.sleep(6)
        try:
            menu_button = driver.find_element(By.XPATH, '//button[@class="wpO6b"]')
            menu_button.click()
            time.sleep(2)
        except:
            print("Menu button not found. Already logged out?")
            return

        try:
            logout_button = driver.find_element(By.XPATH, '//div[text()="Log Out"]')
            logout_button.click()
            time.sleep(2)
        except:
            print("Logout button not found. Already logged out?")
            return
    def post_follow():
        follow_window = tk.Tk()
        follow_window.title("Post Follow")
        tk.Label(follow_window, text="Enter postcode: ").grid(row=0, column=0)
        postcode_entry = tk.Entry(follow_window)
        postcode_entry.grid(row=0, column=1)

        def follow_with_postcode():
            postcode = postcode_entry.get()
            driver.get(f"https://www.instagram.com/p/{postcode}/liked_by/")
            follow()

        tk.Button(follow_window, text="Start Following", command=follow_with_postcode).grid(row=1, column=0,columnspan=2)

    def page_follow_box():
        follow_window = tk.Tk()
        follow_window.title("Follow everyone from IG page")
        tk.Label(follow_window, text="Enter page IG username: ").grid(row=0, column=0)
        postcode_entry = tk.Entry(follow_window)
        postcode_entry.grid(row=0, column=1)

        def page_follow_input():
            username = postcode_entry.get()
            driver.get(f"https://www.instagram.com/{username}/followers/")
            page_follow()

        tk.Button(follow_window, text="Start Following", command=page_follow_input).grid(row=1, column=0,columnspan=2)

 # Buttons
    tk.Label(home_screen, text="Please Log-in to Instagram first to use functions").grid(row=1, column=0, columnspan=2)

    tk.Button(home_screen, text="Login to Instagram", command=lambda: threading.Thread(target=login).start()).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(home_screen, text="Log out", command=lambda: threading.Thread(target=logout).start()).grid(row=2, column=1, padx=10, pady=10)
    tk.Button(home_screen, text="Post Follow", command=lambda: threading.Thread(target=post_follow).start()).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(home_screen, text="Page Follow", command=lambda: threading.Thread(target=page_follow_box).start()).grid(row=3, column=1, padx=10, pady=10)
    tk.Button(home_screen, text="Unfollow", command=lambda: threading.Thread(target=unfollow).start()).grid(row=5, column=0, padx=10, pady=10, columnspan=2)


    error_message = tk.StringVar()
    tk.Label(home_screen, textvariable=error_message).grid(row=6, column=0, columnspan=2)

    home_screen.mainloop()

def logout():
    global is_logged_in
    is_logged_in = False
    driver.get("https://www.instagram.com/accounts/logout/")
    time.sleep(2)
    driver.quit()
    show_login_form()

def main():
    global driver
    show_login_form()

if __name__ == "__main__":
    main()