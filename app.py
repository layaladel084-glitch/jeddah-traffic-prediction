import streamlit as st

st.set_page_config(page_title="التنبؤ بالازدحام المروري في جدة", page_icon="🚗", layout="wide")
st.title("🚦 نظام التنبؤ بالازدحام المروري في جدة")
st.write("نظام تجريبي للمساعدة في توقع مستوى الازدحام المروري.")
st.divider()

st.subheader("أدخل بيانات الطريق")
area = st.selectbox("منطقة الطريق", ["شمال جدة", "جنوب جدة", "شرق جدة", "غرب جدة", "وسط جدة"])
hour = st.slider("الساعة", 0, 23, 8)
day = st.selectbox("حالة اليوم", ["يوم عمل", "عطلة نهاية الأسبوع"])

if st.button("عرض التوقع"):
    if hour in range(7, 10) or hour in range(16, 20):
        result = "ازدحام مرتفع"
    elif hour in range(10, 16) or hour in range(20, 23):
        result = "ازدحام متوسط"
    else:
        result = "ازدحام منخفض"

    st.subheader("نتيجة التوقع")
    st.write("المنطقة:", area)
    st.success("مستوى الازدحام المتوقع: " + result)
    st.caption(
        "هذه نتيجة تجريبية مبنية على أوقات افتراضية، "
        "وليست ناتجة عن نموذج تعلم آلة مدرّب."
    )
