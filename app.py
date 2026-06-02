import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Churn Dashboard", layout="wide")

# 🔥 PROFESSIONAL DARK BLUE GLASSMORPHISM
st.markdown("""
<style>
/* DARK BLUE GLASSMORPHISM THEME */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }
.main .block-container {
    background: 
        linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%),
        radial-gradient(circle at 20% 80%, rgba(59,130,246,0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(99,102,241,0.1) 0%, transparent 50%);
    min-height: 100vh;
    color: white;
}

/* PREMIUM GLASS CARDS */
.glass-card {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(30px) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 24px !important;
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.3),
        0 0 0 1px rgba(255, 255, 255, 0.05),
        inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
}

.glass-card:hover {
    transform: translateY(-8px) !important;
    box-shadow: 
        0 30px 60px rgba(0, 0, 0, 0.4),
        0 0 0 1px rgba(59, 130, 246, 0.3) !important;
    background: rgba(255, 255, 255, 0.12) !important;
}

/* METRICS */
.metric-value { 
    font-size: 2.8rem !important; 
    font-weight: 700 !important; 
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.metric-label { 
    font-size: 0.95rem !important; 
    opacity: 0.8; 
    font-weight: 500;
    letter-spacing: 0.5px;
}

/* CHARTS */
.plotly-chart-container {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(20px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

/* SIDEBAR */
.sidebar .sidebar-content {
    background: rgba(15, 23, 42, 0.95) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(59, 130, 246, 0.2) !important;
}

/* BUTTONS */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(59, 130, 246, 0.3) !important;
    border-radius: 16px !important;
    color: white !important;
    font-weight: 600 !important;
    box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3) !important;
}

/* INPUTS */
.stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 16px !important;
    color: white !important;
    padding: 16px !important;
}

/* TITLES */
h1 { 
    color: white !important; 
    font-size: 2.8rem !important; 
    font-weight: 700 !important; 
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 3rem;
}
</style>
""", unsafe_allow_html=True)

# Navigation
with st.sidebar:
    st.markdown('<h2 style="color: #3b82f6; margin-bottom: 2rem;">🚀 Churn Dashboard</h2>', unsafe_allow_html=True)
    page = st.selectbox("Select Page:", ["📊 Overview", "📈 Analytics", "👥 Customers", "⚙️ Settings"], index=0)

# OVERVIEW
if page == "📊 Overview":
    st.markdown('<h1>Executive Dashboard</h1>', unsafe_allow_html=True)
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4, gap="2rem")
    with col1:
        st.markdown("""
        <div class="glass-card" style="padding: 2.5rem;">
            <div class="metric-value">$247K</div>
            <div class="metric-label">Total Revenue</div>
            <div style="color: #10b981; font-weight: 600;">+18.2%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card" style="padding: 2.5rem;">
            <div class="metric-value">12,847</div>
            <div class="metric-label">Active Customers</div>
            <div style="color: #10b981; font-weight: 600;">+9.4%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="glass-card" style="padding: 2.5rem;">
            <div class="metric-value">92%</div>
            <div class="metric-label">Retention Rate</div>
            <div style="color: #10b981; font-weight: 600;">+2.1%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="glass-card" style="padding: 2.5rem;">
            <div class="metric-value">8.2%</div>
            <div class="metric-label">Churn Rate</div>
            <div style="color: #ef4444; font-weight: 600;">-0.8%</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns([2.5, 1])
    with col1:
        fig = px.line(x=['Jan','Feb','Mar','Apr','May','Jun'], 
                     y=[185, 210, 245, 238, 265, 287], 
                     markers=True,
                     title="Monthly Revenue Growth")
        fig.update_layout(height=450, font_color='white', showlegend=False, 
                         plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="glass-card" style="padding: 2rem; height: 450px;">'
                   '<h3 style="margin-bottom: 1.5rem;">Quick Actions</h3>'
                   '<div style="color: #10b981; margin-bottom: 1rem;">✅ Send retention emails</div>'
                   '<div style="color: #f59e0b; margin-bottom: 1rem;">⚠️ Review at-risk</div>'
                   '<div style="color: #ef4444;">❌ Churn analysis</div>'
                   '</div>', unsafe_allow_html=True)

# ANALYTICS
elif page == "📈 Analytics":
    st.markdown('<h1>Advanced Analytics</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(x=['Active','At Risk','Churned'], y=[10847, 1890, 1110],
                     color_discrete_sequence=['#10b981', '#f59e0b', '#ef4444'])
        fig1.update_layout(height=450, font_color='white', title="Customer Status Distribution")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.pie(values=[84.5, 14.7, 8.2], names=['Retained','At Risk','Churned'],
                     color_discrete_sequence=['#10b981', '#f59e0b', '#ef4444'])
        fig2.update_layout(height=450, font_color='white', title="Churn Risk Breakdown")
        st.plotly_chart(fig2, use_container_width=True)

# CUSTOMERS
elif page == "👥 Customers":
    st.markdown('<h1>Customer Intelligence</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("🔍 Search customers", placeholder="Name, email, or ID...")
        st.markdown("""
        <div class="glass-card" style="padding: 2rem;">
            <h3>Customer Directory (12,847 total)</h3>
            <div style="margin: 1rem 0;">John Smith • john@company.com • Active • $299/mo</div>
            <div style="margin: 1rem 0; color: #f59e0b;">Sarah Wilson • sarah@biz.com • At Risk • $89/mo</div>
            <div style="margin: 1rem 0;">Mike Johnson • mike@startup.com • Active • $499/mo</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card" style="padding: 2rem; height: 400px;">
            <h3>Health Score</h3>
            <div style="font-size: 2.5rem; color: #10b981;">92%</div>
            <div style="opacity: 0.8;">Overall</div>
        </div>
        """, unsafe_allow_html=True)

# SETTINGS
elif page == "⚙️ Settings":
    st.markdown('<h1>Configuration</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="glass-card" style="padding: 2rem;"><h3>Account</h3></div>', unsafe_allow_html=True)
        st.text_input("Company", "TechCorp Inc.")
    
    with col2:
        st.markdown('<div class="glass-card" style="padding: 2rem;"><h3>Alerts</h3></div>', unsafe_allow_html=True)
        threshold = st.slider("Churn Threshold", 5, 25, 10)
    
    with col3:
        st.markdown("""
        <div class="glass-card" style="padding: 2rem; text-align: center;">
            <h3>Billing</h3>
            <div style="font-size: 2.5rem; color: #3b82f6;">$2,990/mo</div>
            <div>Enterprise</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center; color:rgba(255,255,255,0.6); font-size:0.9rem;'>© 2026 Enterprise Churn Analytics</div>", unsafe_allow_html=True)
 



    
    
