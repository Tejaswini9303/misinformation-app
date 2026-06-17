import streamlit as st
import time
import random
import requests
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import kagglehub
import base64

# --- KAGGLE TOKEN ---
os.environ["KAGGLE_API_TOKEN"] = "KGAT_86fd0210e029f746c2ae985878bca6b8"

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="DOS Misinformation Hub", page_icon="🌐", layout="wide")

# --- GLOBAL BACKGROUND SCRIPT ---
# 1. Helper function to convert your image (Cached so it runs lightning fast!)
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 2. Convert your local image (TYPE YOUR EXACT IMAGE NAME HERE)
img_base64 = get_base64_of_bin_file("attachments/01.png") 

# --- CUSTOM PALETTE & BACKGROUND CSS ---
st.markdown(f"""
<style>
    /* 1. Global Translucent Background applied to all pages */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(253, 251, 249, 0.88), rgba(240, 233, 228, 0.90)), url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 2. Sidebar Navy Gradient */
    [data-testid="stSidebar"] {{
        background-color: #202940 !important;
        background-image: linear-gradient(180deg, #202940 0%, #0d121f 100%);
    }}
    
    /* 3. Sidebar Text Color */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] div, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {{
        color: #F8F9FA !important; 
    }}

    /* 4. Clean up the navigation radio buttons */
    div.stRadio > div {{
        gap: 16px;
        font-weight: bold;
    }}

    /* 5. Flashcard Beautification (Shadows & Hover Animations) */
    div[data-testid="stExpander"] {{
        border: 2px solid #CAAA98; 
        border-radius: 12px;
        background-color: #FFFFFF;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05); 
        transition: all 0.3s ease-in-out; 
    }}
    
    div[data-testid="stExpander"]:hover {{
        box-shadow: 0px 10px 25px rgba(32, 41, 64, 0.2); 
        transform: translateY(-4px); 
        border-color: #202940; 
    }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
st.sidebar.markdown("Explore the Interactive Modules:")
page = st.sidebar.radio("", [
    "Misinformation Crisis", 
    "Deepfake Detective", 
    "Context Slider", 
    "Spot the Troll",
    "Fact-Checking API",
    "Cascade Analysis"
])

# ==========================================
# PAGE ROUTING
# ==========================================
if page == "Misinformation Crisis":
    
    st.title("The Misinformation Crisis")
    st.subheader("How False Information Shapes Digital Society")
    
    st.markdown("""
    Welcome to the Digital Objects and Society (DOS) Misinformation Hub. 
    Click on the flashcards below to explore the four core pillars of our research framework.
    """)
    
    st.divider()

    
    # Create a 2x2 grid for the Flashcards
    col1, col2 = st.columns(2)
    
    with col1:
        # FLASHCARD 1
        with st.expander("📚 Pillar 1: Mechanics of Spread"):
            st.markdown("""
            **Misinformation Through the Lens of Digital Objects** *The Three-Stage Pipeline:*
            
            * **Indexicalization:** Commencing with a baseline layer of reality (e.g., an unedited source video/image).
            * **Decontextualization:** Decoupling the asset from its original timeline/background to embed a false narrative.
            * **Re-indexicalization:** Decentralized viral spread driven by peer networks adding personal validation text.
            """)
            
        # FLASHCARD 2
        with st.expander("🧠 Pillar 2: Human Element & Consequences"):
            st.markdown("""
            * **Fitting What You Believe:** Fake news spreads easily because it tells people exactly what they already want to believe, so they don't bother questioning it.
            * **Algorithmic Boost:** Computer algorithms are built to push posts that get a lot of reactions, meaning dramatic and emotional content gets automatically promoted.
            * **The Popularity Trap:** When people see a post with thousands of likes and shares, they automatically assume it must be true.
            * **Over-Simplifying Things:** Complex topics (like science or politics) are broken down into overly simple, black-and-white stories that are easy to understand but misleading.
            * **Grouping the Audience:** It divides social media users into different groups based on how easily they fall for fake news or how likely they are to fight it.
            """)

    with col2:
        # FLASHCARD 3
        with st.expander("👁️ Pillar 3: Visual Misinformation"):
            st.markdown("""
            * **Human Detection Limits:** Human deepfake detection accuracy is barely above random chance (~63%), proving AI generation has surpassed organic perception.
            * **The Trust Paradox:** Basic "cheap fakes" are often trusted more than AI deepfakes because genuine footage instinctively triggers the brain's realism heuristic.
            * **Cognitive Exploitation:** Emotional narratives induce inattentional blindness, causing viewers to completely overlook obvious visual anomalies and background glitches.
            * **Forensic Indicators:** AI struggles with strict physics, making irregular pupil shapes and mismatched corneal reflections the most reliable forensic indicators.
            """)
            
        # FLASHCARD 4
        with st.expander("🛡️ Pillar 4: Fighting Back"):
            st.markdown("""
            * **Teach Before It Spreads:** Interactive media literacy training improves users' ability to identify false information.
            * **More Than Fact-Checking:** While corrections are helpful, they frequently fall short of the pace and reach of viral false information.
            * **Algorithms Matter:** The spread of false information can be considerably slowed by reducing algorithmic promotion of deceptive content.
            * **Shared Responsibility:** Platforms, governments, scholars, and users must work together to effectively moderate.
            * **No Single Solution:** Research continuously demonstrates that the most effective protection integrates platform governance, technology, education, and regulation.
            """)
            
    st.divider()
    st.caption("Use the sidebar on the left to explore the interactive technical modules for these pillars.")

# ==========================================
# PAGE 1: DEEPFAKE DETECTIVE
# ==========================================
elif page == "Deepfake Detective":
    st.title("🕵️ Deepfake Detective")
    st.markdown("""
    **Challenge:** AI generative models struggle with strict physics, human anatomy, and logical consistency. 
    Audit the images in the Case Files below and identify the primary visual glitch that proves they are synthetic.
    """)
    
    # Using tabs to create multiple quizzes
    tab1, tab2 = st.tabs(["Case File 1: The Portrait", "Case File 2: The Crowd"])
    
    with tab1:
        st.subheader("Case 1: Facial & Environmental Physics")
        st.image("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&auto=format&fit=crop&q=60", width=400, caption="Audit Subject A")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👁️ The Eyes", key="c1_eyes"):
                st.success("**Correct! Mismatched Corneal Reflections.** AI frequently generates completely different light patterns in the left and right eyes.")
            if st.button("👕 The Clothing/Textures", key="c1_cloth"):
                st.error("Incorrect. The textures here look normal.")
        with col2:
            if st.button("🧱 The Background", key="c1_back"):
                st.success("**Correct! Warped Physics.** While you focus on the face, you miss that the background architecture melts together.")
            if st.button("👂 The Ears", key="c1_ears"):
                st.error("Incorrect. The primary giveaways here are the eyes and the background.")

    with tab2:
        st.subheader("Case 2: Anatomical Rendering")
        # Placeholder for an AI image with bad hands
        st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&auto=format&fit=crop&q=60", width=400, caption="Audit Subject B")
        st.info("Hint: Don't look at the faces. Look at how people interact with their environment.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🖐️ The Hands and Fingers", key="c2_hands"):
                st.success("**Correct! Anatomical Failure.** Generative models frequently fail at counting. It is highly common to see 6 fingers, fused joints, or hands melting into objects.")
            if st.button("💡 The Lighting", key="c2_light"):
                st.error("Incorrect. AI is actually very good at mimicking studio lighting.")
        with col2:
            if st.button("👄 The Teeth", key="c2_teeth"):
                st.warning("Close, AI sometimes messes up teeth, but it's not the primary glitch here.")
            if st.button("👗 The Fabric Folds", key="c2_fabric"):
                st.error("Incorrect. Fabric drapes logically here.")


# ==========================================
# PAGE 2: CONTEXT SLIDER
# ==========================================

elif page == "Context Slider":
    st.title("✂️ The Context Slider")
    st.markdown("Teaches the danger of missing context and the **Realism Heuristic**.")
    zoom_level = st.slider("Drag slider to reveal full context", min_value=0, max_value=100, value=0)
    if zoom_level < 50:
        st.warning("Headline: 'Angry mob isolates and surrounds individual!'")
        st.image("https://images.unsplash.com/photo-1506869640319-fe1a24fd07dc?w=800&auto=format&fit=crop&q=60", caption="Manipulated View")
    else:
        st.success("**The Reality:** It's a collaborative team-building exercise, not an angry mob.")
        st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&auto=format&fit=crop&q=60", caption="Original View")

# ==========================================
# PAGE 3: SPOT THE TROLL
# ==========================================
elif page == "Spot the Troll":
    st.title("🧟 Spot the Troll Mini-Game")
    st.markdown("""
    Bot networks are the engines of the **"Out-of-Control" algorithmic governance** we researched. 
    Can you identify the malicious actors hiding among normal users?
    """)
    
    tab1, tab2, tab3 = st.tabs(["Round 1: The Outrage Bot", "Round 2: The Scammer", "Round 3: The Fake Expert"])
    
    # ROUND 1: Outrage Bot (Original)
    with tab1:
        st.subheader("Round 1: Political Amplification")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("👤 **@SarahReadsBooks** (Age: 4 Yrs | Posts: 2/wk)")
            if st.button("Flag as Troll", key="t1_1"): st.error("Normal user.")
        with col2:
            st.warning("👤 **@Patriot1234567** (Age: 3 Days | Posts: 150/day)")
            if st.button("Flag as Troll", key="t1_2"): 
                st.success("**Correct!** High volume, alphanumeric handle, high-anger keywords.")
        with col3:
            st.info("👤 **@TechNewsDaily** (Age: 8 Yrs | Posts: 5/day)")
            if st.button("Flag as Troll", key="t1_3"): st.error("Corporate account.")

    # ROUND 2: Crypto/Scam Bot
    with tab2:
        st.subheader("Round 2: Financial Disinformation")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.warning("👤 **@ElonMusk_Giveaway_Official**")
            st.markdown("* **Followers:** 14 | **Following:** 5,000\n* **Post:** 'Send 1 BTC to this link and I will send back 2 BTC! Airdrop live now! 🚀'")
            if st.button("Flag as Troll", key="t2_1"): 
                st.success("**Correct! Phishing Bot.** Look at the massive Follower/Following ratio imbalance. It aggressively tags trending names to steal money.")
        with col2:
            st.info("👤 **@GamerGuy99**")
            st.markdown("* **Followers:** 450 | **Following:** 400\n* **Post:** 'Can't believe the server lag tonight. Anyone else dropping frames?'")
            if st.button("Flag as Troll", key="t2_2"): st.error("Normal frustrated gamer.")
        with col3:
            st.info("👤 **@DigitalArtist_Jen**")
            st.markdown("* **Followers:** 12k | **Following:** 800\n* **Post:** 'Check out my new landscape painting process video! 🎨'")
            if st.button("Flag as Troll", key="t2_3"): st.error("Normal creator account.")

    # ROUND 3: Fake Expert
    with tab3:
        st.subheader("Round 3: Science/Health Misinformation")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("👤 **@CityHospital_Official**")
            st.markdown("* **Verified:** Yes\n* **Post:** 'Flu season is here. Walk-in clinic open until 8 PM tonight.'")
            if st.button("Flag as Troll", key="t3_1"): st.error("Normal institutional account.")
        with col2:
            st.info("👤 **@ScienceTeacher_Tom**")
            st.markdown("* **Verified:** No\n* **Post:** 'My 8th graders asked great questions about the solar system today.'")
            if st.button("Flag as Troll", key="t3_2"): st.error("Normal educator.")
        with col3:
            st.warning("👤 **@Dr_Health_Truth_MD**")
            st.markdown("* **Profile Pic:** Generic stock photo of a doctor.\n* **Post:** 'Doctors are hiding the TRUTH! This one natural root cures EVERYTHING. Buy my supplements here! 👇'")
            if st.button("Flag as Troll", key="t3_3"): 
                st.success("**Correct! Grifter/Fake Expert.** They use authority titles (Dr/MD) and stock photos to sell unverified cures via emotional manipulation (fear/secrecy).")

# ==========================================
# PAGE 4: FACT-CHECKING API (From factcheck.py)
# ==========================================
elif page == "Fact-Checking API":
    st.title("🔍 Live Fact-Checking API")
    st.markdown("Query the Google Fact Check Tools API to instantly verify claims against global independent fact-checkers.")
    
    API_KEY = "AIzaSyABlk9uFPe-pR_kmQLX6oFXfQgq5dnKaXI" # From your provided script
    
    query = st.text_input("Enter a claim to verify (e.g., 'moon landing is fake'):", "moon landing is fake")
    
    if st.button("Check Claim", type="primary"):
        with st.spinner("Querying global fact-checking databases..."):
            url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
            params = {"query": query, "key": API_KEY, "languageCode": "en"}
            
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                if "claims" not in data or not data["claims"]:
                    st.warning(f"No explicit fact-check records found for: '{query}'")
                else:
                    for idx, claim_item in enumerate(data["claims"], 1):
                        claim_text = claim_item.get("text", "N/A")
                        claimant = claim_item.get("claimant", "Unknown Source")
                        claim_date = claim_item.get("claimDate", "Unknown date")[:10]
                        
                        st.markdown(f"### [{idx}] Claim: *\"{claim_text}\"*")
                        st.caption(f"🗣️ Stated by **{claimant}** on {claim_date}")
                        
                        for review in claim_item.get("claimReview", []):
                            publisher = review.get("publisher", {}).get("name", "Unknown Publisher")
                            rating = review.get("textualRating", "No Rating Provided").upper()
                            review_url = review.get("url", "#")
                            
                            # Determine badge color based on rating
                            if any(word in rating for word in ["FALSE", "FAKE", "INCORRECT", "MISLEADING"]):
                                st.error(f"**{publisher} Verdict:** {rating}\n\n🔗 [Read Full Review]({review_url})")
                            elif any(word in rating for word in ["TRUE", "CORRECT", "ACCURATE"]):
                                st.success(f"**{publisher} Verdict:** {rating}\n\n🔗 [Read Full Review]({review_url})")
                            else:
                                st.warning(f"**{publisher} Verdict:** {rating}\n\n🔗 [Read Full Review]({review_url})")
                        st.divider()

            except Exception as e:
                st.error(f"API Connection Error: {e}")

# ==========================================
# PAGE 5: MISINFORMATION CASCADE (From cascade_viral_networks.py)
# ==========================================
elif page == "Cascade Analysis":
    st.title("🕸️ Viral Cascade & Network Analysis")
    st.markdown("Visualizing the spread of misinformation using the Kaggle 'viral-content-propagation-2026' dataset.")
    
    @st.cache_data
    def load_network_data():
        path = kagglehub.dataset_download("masanakashima/viral-content-propagation-2026")
        users_df = pd.read_csv(os.path.join(path, 'users.csv'))
        relations_df = pd.read_csv(os.path.join(path, 'relations.csv'))
        logs_df = pd.read_csv(os.path.join(path, 'propagation.csv'))
        
        logs_df['Action'] = logs_df['Action'].astype(str).str.strip().str.lower()
        users_df['Account_Type'] = users_df['Account_Type'].astype(str).str.strip()
        merged_logs = logs_df.merge(users_df[['User_ID', 'Account_Type']], on='User_ID', how='left')
        return users_df, relations_df, merged_logs

    with st.spinner("Processing 2026 Network Dataset via Kaggle..."):
        try:
            users_df, relations_df, merged_logs = load_network_data()
            
            # --- INFOGRAPHIC DASHBOARD ---
            st.subheader("📊 Infographic: Cascade Overview")
            
            # Data Calculations
            miso_logs = merged_logs[merged_logs['Account_Type'].str.lower() == 'bot'].sort_values(by='Step')
            if len(miso_logs) == 0: miso_logs = merged_logs.sort_values(by='Step')
            miso_tree = nx.from_pandas_edgelist(miso_logs, source='Tweet_ID', target='User_ID', create_using=nx.DiGraph())
            
            instant_sharers = merged_logs[merged_logs['Step'] == 0]['User_ID'].unique()
            G_base = nx.from_pandas_edgelist(relations_df, source='Source_User_ID', target='Target_User_ID')
            subgraph_instant = G_base.subgraph(instant_sharers)
            cliques = list(nx.find_cliques(subgraph_instant))
            largest_clique_size = len(max(cliques, key=len)) if cliques else 0
            
            # Metric Cards
            col1, col2, col3, col4 = st.columns(4)
            col1.metric(label="Total Infected Nodes", value=miso_tree.number_of_nodes(), delta="High Virality", delta_color="inverse")
            col2.metric(label="Patient Zero", value=str(miso_logs.iloc[0]['User_ID']))
            col3.metric(label="Step 0 Burst Users", value=len(instant_sharers))
            col4.metric(label="Bot Clique Size", value=largest_clique_size, delta="Coordinated Attack", delta_color="inverse")
            
            st.divider()

            # --- NEW: ECHO CHAMBER CENTRALITY GRAPH ---
            st.subheader("🌐 Influencer Network Topology")
            st.markdown("This graph maps the top 100 most highly connected accounts (Viral Inflection Nodes). Red nodes represent accounts with the highest 'In-Degree Centrality'—meaning they have the most followers listening to them.")
            
            with st.spinner("Calculating network centrality and plotting echo chambers..."):
                # Reconstruct full graph to find influencers
                G = nx.from_pandas_edgelist(relations_df, source='Source_User_ID', target='Target_User_ID', create_using=nx.DiGraph())
                
                # Calculate centrality and filter top 100
                centrality = nx.in_degree_centrality(G)
                users_df['Centrality_Score'] = users_df['User_ID'].map(centrality)
                top_nodes = users_df.nlargest(100, 'Centrality_Score')['User_ID']
                subgraph = G.subgraph(top_nodes)
                
                # Plot the graph
                fig_echo, ax_echo = plt.subplots(figsize=(10, 6), dpi=150)
                pos = nx.spring_layout(subgraph, k=0.3, seed=42)
                
                # Color mapping based on score
                node_color = [users_df.loc[users_df['User_ID'] == node, 'Centrality_Score'].values[0] for node in subgraph.nodes()]
                
                nx.draw_networkx_nodes(subgraph, pos, node_size=180, node_color=node_color, cmap=plt.cm.coolwarm, ax=ax_echo)
                nx.draw_networkx_edges(subgraph, pos, alpha=0.3, edge_color='gray', arrows=True, ax=ax_echo)
                nx.draw_networkx_labels(subgraph, pos, font_size=8, font_family='sans-serif', ax=ax_echo)
                
                ax_echo.set_title("Botnet Echo Chambers & Viral Inflection Nodes", fontsize=14, fontweight='bold', pad=15)
                ax_echo.axis('off')
                
                st.pyplot(fig_echo)

            st.divider()

            # --- VISUALIZATION RENDERING (3-Panel) ---
            st.subheader("📈 Multi-Panel Cascade Visualization")
            with st.spinner("Rendering complex Matplotlib network graphs..."):
                fig, axes = plt.subplots(1, 3, figsize=(24, 7), dpi=150)
                fig.suptitle("Malicious Propaganda & Misinformation Cascade Analysis", fontsize=20, fontweight='bold', y=1.02)

                # Panel 1: Cascade Tree
                ax1 = axes[0]
                pos_tree = nx.kamada_kawai_layout(miso_tree)
                nx.draw_networkx_nodes(miso_tree, pos_tree, ax=ax1, node_size=15, node_color='#e74c3c', alpha=0.6)
                nx.draw_networkx_edges(miso_tree, pos_tree, ax=ax1, alpha=0.2, edge_color='#c0392b', arrows=True, arrowsize=6)
                ax1.set_title(f"1. Infection Cascade Tree\n({miso_tree.number_of_nodes()} Infected Nodes)", fontsize=13, fontweight='bold')
                ax1.axis('off')

                # Panel 2: Velocity Curve
                ax2 = axes[1]
                bot_timeline = merged_logs[(merged_logs['Action'] == 'retweeted') & (merged_logs['Account_Type'].str.lower() == 'bot')].groupby('Step').size().cumsum()
                normal_timeline = merged_logs[(merged_logs['Action'] == 'retweeted') & (merged_logs['Account_Type'].str.lower() == 'normal')].groupby('Step').size().cumsum()
                ax2.plot(bot_timeline.index, bot_timeline.values, label='Bot Amplification', color='#e74c3c', linewidth=3, marker='o')
                ax2.plot(normal_timeline.index, normal_timeline.values, label='Normal Sharing', color='#3498db', linewidth=3, marker='s')
                ax2.set_title("2. Propagation Velocity Curve", fontsize=13, fontweight='bold')
                ax2.set_xlabel("Time Interval (Step)", fontsize=11)
                ax2.set_ylabel("Cumulative Retweets", fontsize=11)
                ax2.grid(True, linestyle='--', alpha=0.5)
                ax2.legend(fontsize=10, loc='upper left')

                # Panel 3: Step 0 Burst
                ax3 = axes[2]
                pos_burst = nx.spring_layout(subgraph_instant, k=0.5, seed=42)
                node_colors = ['#2ecc71' if n == 'd70d2129' else '#95a5a6' for n in subgraph_instant.nodes()]
                node_sizes = [250 if n == 'd70d2129' else 40 for n in subgraph_instant.nodes()]
                nx.draw_networkx_nodes(subgraph_instant, pos_burst, ax=ax3, node_size=node_sizes, node_color=node_colors, alpha=0.9)
                nx.draw_networkx_edges(subgraph_instant, pos_burst, ax=ax3, alpha=0.15, edge_color='gray')
                labels = {node: node if node == 'd70d2129' else '' for node in subgraph_instant.nodes()}
                nx.draw_networkx_labels(subgraph_instant, pos_burst, labels=labels, ax=ax3, font_size=9, font_weight='bold', font_color='black')
                ax3.set_title("3. Step 0 Blast Structure", fontsize=13, fontweight='bold')
                ax3.axis('off')

                plt.tight_layout()
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Render Error detail: {e}")