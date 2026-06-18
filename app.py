#


import streamlit as st
from groq import Groq

# 1. Secure Page Configuration
st.set_page_config(page_title="Law of Africa", page_icon="⚖️")

# 2. Master Header & Brand Identity
st.title("⚖️ Law of Africa: Intelligence Engine")
st.success("⚡ **Stop spending 10 hours researching OHADA law. Get a comprehensive, highly accurate legal brief in 10 seconds.**")
st.divider()

# 3. System State Initialization (Accounts & Payments Database Simulator)
if "user_accounts" not in st.session_state:
    st.session_state.user_accounts = {"admin": "admin123"} 
if "paid_users" not in st.session_state:
    st.session_state.paid_users = []
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None
if "free_queries_used" not in st.session_state:
    st.session_state.free_queries_used = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Background Security Check for AI Engine
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=groq_api_key)
except Exception:
    st.error("System Status: Security Vault Keys Missing. Please check settings.")
    st.stop()


# 4. THE AUTHENTICATION & ACCESS PORTAL
if st.session_state.logged_in_user is None:
    st.subheader("🔐 Secure User Portal")
    auth_action = st.radio("Choose Action:", ["Login to Account", "Create New Account"])
    
    if auth_action == "Create New Account":
        st.markdown("### Create Your Legal Intelligence Profile")
        new_username = st.text_input("Choose a Username / Email:")
        new_password = st.text_input("Create a Secure Password:", type="password")
        
        if st.button("Register Account 📝"):
            if new_username == "" or new_password == "":
                st.error("Fields cannot be left blank.")
            elif new_username in st.session_state.user_accounts:
                st.error("This username is already registered.")
            else:
                st.session_state.user_accounts[new_username] = new_password
                st.success("Account created successfully! Please switch to 'Login to Account' above.")
                
    elif auth_action == "Login to Account":
        st.markdown("### Secure Login")
        login_username = st.text_input("Username / Email:")
        login_password = st.text_input("Password:", type="password")
        
        if st.button("Log In 🔓"):
            if login_username in st.session_state.user_accounts and st.session_state.user_accounts[login_username] == login_password:
                st.session_state.logged_in_user = login_username
                st.success(f"Welcome back, {login_username}!")
                st.rerun()
            else:
                st.error("Invalid username or password.")
                
    st.stop() 


# 5. THE MULTI-METHOD PAYMENT PORTAL
current_user = st.session_state.logged_in_user
is_premium_user = current_user in st.session_state.paid_users

if not is_premium_user and st.session_state.free_queries_used >= 3:
    st.error(f"🛑 Account Status: Subscription Expired for user [{current_user}]. Premium Access Required.")
    
    st.markdown("### 🌎 Select Your Jurisdiction & Calculate Rate")
    region = st.radio("Where are you currently practicing law?", ["Select Region...", "Within Africa ($100/mo)", "International (Outside Africa) ($200/mo)"])
    
    if region != "Select Region...":
        rate = 100 if region == "Within Africa ($100/mo)" else 200
        yearly_total = rate * 12
        
        st.info(f"📋 **Official Invoice Generated for {current_user}**\n* Total Due: **${yearly_total} USD / Year**")
        
        st.markdown("### 💳 Integrated Payment Gateway")
        payment_method = st.selectbox("Select Your Preferred Payment Method:", [
            "Select Method...", 
            "Credit / Debit Card (Visa, Mastercard)", 
            "Mobile Money (M-Pesa, Orange, MTN, Telecel)", 
            "Direct Bank Wire / Transfer",
            "Apple Pay / Google Pay"
        ])
        
        if payment_method != "Select Method...":
            st.write(f"Processing via secure **{payment_method}** pipeline...")
            
            if "Card" in payment_method:
                st.text_input("Card Number:", placeholder="4000 1234 5678 9010")
                st.text_input("Expiry / CVV:", placeholder="MM/YY |  123")
            elif "Mobile" in payment_method:
                st.text_input("Enter Mobile Money Phone Number:", placeholder="+234...")
            else:
                st.write("Please send funds to the corporate account and paste your transaction reference ID below:")
                st.text_input("Transaction Reference ID:")
                
            if st.button(f"Authorize Custom Payment of ${yearly_total} USD 🚀"):
                st.session_state.paid_users.append(current_user)
                st.success("Payment Captured Successfully! Your account is now Premium.")
                st.rerun()
                
    st.stop() 


# 6. THE PREMIUM CONVERSATIONAL UI TERMINAL
st.write(f"👤 Active Profile: **{current_user}** | Account Tier: " + ("**PREMIUM 🟢**" if is_premium_user else "**FREE TRIAL 🎁**"))
if st.sidebar.button("Log Out Officially 🚪"):
    st.session_state.logged_in_user = None
    st.rerun()

# Draw the Past Conversation 
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Sleek Bottom Chat Input
user_query = st.chat_input("Enter your premium query here...")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    with st.chat_message("assistant"):
        with st.spinner("Processing deep-context analysis..."):
            try:
                messages_for_ai = [{"role": "system", "content": "You are an expert in African corporate law. Detail everything out comprehensively with titles and bullet points."}]
                messages_for_ai.extend(st.session_state.chat_history)

                chat_completion = client.chat.completions.create(
                    messages=messages_for_ai,
                    model="llama-3.3-70b-versatile",
                    max_tokens=6000, 
                )
                
                ai_response = chat_completion.choices[0].message.content
                st.markdown(ai_response)
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                
                if not is_premium_user:
                    st.session_state.free_queries_used += 1
                    st.rerun()
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
### 📋 PART 2 (Copy this and paste it right below Part 1)

```python
# =========================================================================
# 4. BACKGROUND VAULT KEY EXTRACTION FOR AI ARCHITECTURE
# =========================================================================
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
    ai_client = Groq(api_key=groq_api_key)
except Exception:
    st.error("System Status: Security Vault Keys Missing. Please check your system settings.")
    st.stop()

# =========================================================================
# 5. USER SEGMENTATION & ACCESS GATE (PERMANENT DB LOOKUP)
# =========================================================================
if st.session_state.logged_in_user is None:
    st.subheader("🔐 Secure User Portal")
    auth_action = st.radio("Choose Action:", ["Login to Account", "Create New Account"])
    
    if auth_action == "Create New Account":
        st.markdown("### Create Your Legal Intelligence Profile")
        new_username = st.text_input("Choose a Username / Email:").strip()
        new_password = st.text_input("Create a Secure Password:", type="password").strip()
        
        if st.button("Register Account 📝"):
            if not new_username or not new_password:
                st.error("Fields cannot be left blank.")
            elif not db_df.empty and new_username in db_df['username'].astype(str).values:
                st.error("This username is already permanently registered.")
            else:
                # Append new user to the secure spreadsheet matrix
                new_profile = pd.DataFrame([{"username": new_username, "password": new_password, "status": "Free Trial"}])
                updated_db = pd.concat([db_df, new_profile], ignore_index=True)
                db_conn.update(worksheet="users", data=updated_db)
                
                trigger_admin_alert("New User Registration Created", new_username)
                st.success("Account permanently registered in cloud database! Please switch to 'Login to Account' above.")
                st.balloons()
                
    elif auth_action == "Login to Account":
        st.markdown("### Secure Login")
        login_username = st.text_input("Username / Email:").strip()
        login_password = st.text_input("Password:", type="password").strip()
        
        if st.button("Log In 🔓"):
            if db_df.empty:
                st.error("No registered accounts found in cloud storage database.")
            else:
                # Perform continuous data validation match against database records
                matched_user = db_df[(db_df['username'].astype(str) == login_username) & (db_df['password'].astype(str) == login_password)]
                
                if not matched_user.empty:
                    st.session_state.logged_in_user = login_username
                    trigger_admin_alert("User Logged In Successfully", login_username)
                    st.success(f"Access Granted. Welcome back, {login_username}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password credentials.")
                    
    st.stop()

# =========================================================================
# 6. APP CONTENT AREA (UNLOCKED UPON SUCCESSFUL PERMANENT LOGIN)
# =========================================================================
current_user = st.session_state.logged_in_user

# Extract user profile state directly from database records to check payment status
user_row = db_df[db_df['username'].astype(str) == current_user]
user_status = user_row['status'].values[0] if not user_row.empty else "Free Trial"

is_premium_user = (user_status == "Premium")

# Grant 5 full initial testing queries gracefully to your fresh testers
if not is_premium_user and st.session_state.free_queries_used >= 5:
    st.error(f"🛑 Account Status: Subscription Expired for user [{current_user}]. Premium Access Required.")
    st.markdown("### 🌎 Select Your Jurisdiction & Calculate Rate")
    region = st.radio("Where are you currently practicing law?", ["Select Region...", "Within Africa ($100/mo)", "International (Outside Africa) ($200/mo)"])
    
    if region != "Select Region...":
        st.info(f"Payment Processing Interface Initiated for {region}. Please contact Admin to whitelist profile.")
    st.stop()

# Profile Tier Metadata Banner
st.sidebar.markdown(f"👤 **Active Profile:** `{current_user}`")
st.sidebar.markdown(f"💼 **Account Tier:** `{user_status.upper()}`")
if not is_premium_user:
    st.sidebar.markdown(f"📊 **Free Evaluation Inquiries Remaining:** `{5 - st.session_state.free_queries_used}`")

if st.sidebar.button("Log Out 🚪"):
    st.session_state.logged_in_user = None
    st.rerun()

# Display ongoing interaction history layout UI frames
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Chat Interface Logic Block
if user_input := st.chat_input("Enter your premium legal query here..."):
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("🔍 *Analyzing system matrix and compiling legal brief...*")
        
        try:
            chat_completion = ai_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are the premium Law of Africa Intelligence Engine, an elite expert AI trained in African legal frameworks, constitutional architectures, statutory interpretations, case law history, and commercial OHADA guidelines. Provide exhaustive, structured legal briefs with clear sections."},
                    {"role": "user", "content": user_input}
                ],
                model="llama3-8b-8192",
            )
            ai_response = chat_completion.choices[0].message.content
            response_placeholder.markdown(ai_response)
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            
            if not is_premium_user:
                st.session_state.free_queries_used += 1
                
        except Exception as e:
            response_placeholder.markdown(f"⚠️ Generation Error: Engine computation timeout. Details: {str(e)}")
```
