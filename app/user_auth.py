import os
import streamlit as st
import streamlit_authenticator as stauth
from dotenv import load_dotenv

load_dotenv()

def login_user():
    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")

    if not admin_username or not admin_password:
        st.error("❌ Missing credentials in .env file.")
        return False

    # ✅ Correct usage for latest Hasher implementation
    hashed_password = stauth.Hasher([admin_password]).generate()[0]

    credentials = {
        "usernames": {
            admin_username: {
                "name": "Admin",
                "password": hashed_password
            }
        }
    }

    authenticator = stauth.Authenticate(
        credentials,
        cookie_name="docutalk",
        key="abcdef",
        cookie_expiry_days=1
    )

    name, auth_status, _ = authenticator.login("Login", location="main")

    if auth_status:
        authenticator.logout("Logout", "sidebar")
        st.sidebar.success(f"✅ Welcome {name}!")
        return True
    elif auth_status is False:
        st.error("❌ Invalid username or password.")
    elif auth_status is None:
        st.warning("🔐 Please enter your credentials.")

    return False
